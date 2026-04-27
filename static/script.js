document.addEventListener("DOMContentLoaded", () => {
    const chatForm = document.getElementById("chat-form");
    const userInput = document.getElementById("user-input");
    const chatArea = document.getElementById("chat-area");
    const sendButton = document.getElementById("send-button");
    const clearChatBtn = document.getElementById("clear-chat");
    
    let sessionId = sessionStorage.getItem("naijaVoteSessionId") || null;

    // Auto-resize textarea
    userInput.addEventListener("input", function() {
        this.style.height = "auto";
        this.style.height = (this.scrollHeight) + "px";
        if(this.value === "") {
            this.style.height = "auto";
        }
    });

    // Handle Enter to send, Shift+Enter for new line
    userInput.addEventListener("keydown", function(e) {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            if (this.value.trim() !== "") {
                chatForm.dispatchEvent(new Event("submit", {cancelable: true, bubbles: true}));
            }
        }
    });

    // Clear Chat functionality
    if (clearChatBtn) {
        clearChatBtn.addEventListener("click", () => {
            sessionId = null;
            sessionStorage.removeItem("naijaVoteSessionId");
            
            // Keep only the first bot message (intro)
            const messages = chatArea.querySelectorAll(".message");
            for (let i = 1; i < messages.length; i++) {
                messages[i].remove();
            }
            
            userInput.value = "";
            userInput.style.height = "auto";
            userInput.focus();
        });
    }

    function scrollToBottom() {
        chatArea.scrollTop = chatArea.scrollHeight;
    }

    function createMessageElement(text, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", sender === "user" ? "user-message" : "bot-message");

        const avatarDiv = document.createElement("div");
        avatarDiv.classList.add("avatar");
        const avatarInner = document.createElement("div");
        avatarInner.classList.add("avatar-inner");
        avatarInner.textContent = sender === "user" ? "ME" : "AI";
        avatarDiv.appendChild(avatarInner);

        const bubbleDiv = document.createElement("div");
        bubbleDiv.classList.add("message-bubble", "glass-panel");
        
        // Handle basic newlines
        const paragraphs = text.split('\n').filter(p => p.trim() !== '');
        paragraphs.forEach(pText => {
            const p = document.createElement("p");
            p.textContent = pText;
            bubbleDiv.appendChild(p);
        });

        messageDiv.appendChild(avatarDiv);
        messageDiv.appendChild(bubbleDiv);

        return messageDiv;
    }

    function addTypingIndicator() {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", "bot-message");
        messageDiv.id = "typing-indicator";

        const avatarDiv = document.createElement("div");
        avatarDiv.classList.add("avatar");
        const avatarInner = document.createElement("div");
        avatarInner.classList.add("avatar-inner");
        avatarInner.textContent = "AI";
        avatarDiv.appendChild(avatarInner);

        const bubbleDiv = document.createElement("div");
        bubbleDiv.classList.add("message-bubble", "glass-panel");
        
        const typingIndicator = document.createElement("div");
        typingIndicator.classList.add("typing-indicator");
        for (let i = 0; i < 3; i++) {
            const dot = document.createElement("div");
            dot.classList.add("dot");
            typingIndicator.appendChild(dot);
        }

        bubbleDiv.appendChild(typingIndicator);
        messageDiv.appendChild(avatarDiv);
        messageDiv.appendChild(bubbleDiv);

        chatArea.appendChild(messageDiv);
        scrollToBottom();
    }

    function removeTypingIndicator() {
        const indicator = document.getElementById("typing-indicator");
        if (indicator) {
            indicator.remove();
        }
    }

    async function handleSend(e) {
        e.preventDefault();
        
        const text = userInput.value.trim();
        if (!text) return;

        // Add user message
        const userMsg = createMessageElement(text, "user");
        chatArea.appendChild(userMsg);
        userInput.value = "";
        userInput.style.height = "auto"; // Reset height after sending
        
        // Disable input while waiting
        userInput.disabled = true;
        sendButton.disabled = true;
        
        scrollToBottom();
        addTypingIndicator();

        try {
            const response = await fetch("/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ 
                    message: text,
                    session_id: sessionId
                })
            });

            const data = await response.json();
            removeTypingIndicator();
            
            // Store the session ID returned from the server
            if (data.session_id) {
                sessionId = data.session_id;
                sessionStorage.setItem("naijaVoteSessionId", sessionId);
            }
            
            if (response.ok) {
                const botMsg = createMessageElement(data.response, "bot");
                chatArea.appendChild(botMsg);
            } else {
                throw new Error(data.detail || "Server returned an error");
            }
        } catch (error) {
            console.error("Error connecting to chat API:", error);
            removeTypingIndicator();
            const errorText = "Connection lost or server error. Please try again shortly.\n(Detail: " + error.message + ")";
            const botMsg = createMessageElement(errorText, "bot");
            chatArea.appendChild(botMsg);
        } finally {
            userInput.disabled = false;
            sendButton.disabled = false;
            userInput.focus();
            scrollToBottom();
        }
    }

    chatForm.addEventListener("submit", handleSend);
    userInput.focus();
});
