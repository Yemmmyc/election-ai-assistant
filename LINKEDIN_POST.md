# LinkedIn Post Draft

*(Copy and paste this into LinkedIn. Feel free to add your specific GitHub repo link and tag relevant technologies!)*

---

🚀 **Excited to share my latest full-stack project: NaijaVote AI!** 🇳🇬

With elections and civic duties being such a critical part of our society, I wanted to build a tool that makes finding accurate, neutral voting information as easy as sending a text. 

I just finished architecting and deploying **NaijaVote AI**, a cloud-native election assistant powered by Google's Gemini AI!

Here’s a breakdown of what I built and the tech stack I used:

🎨 **The Frontend:** I completely bypassed heavy frameworks and built a custom, premium "glassmorphism" UI using pure Vanilla HTML, CSS, and JavaScript. It features ambient background glows, smooth typing micro-animations, and a fully responsive dark mode.

⚙️ **The Backend:** Built a highly performant API using Python and **FastAPI**. I integrated the brand new `google-genai` SDK to hook into the `gemini-2.0-flash` model, ensuring lightning-fast AI responses. 

🛡️ **Robust Engineering:** One of the most interesting challenges was handling external API constraints. I implemented strict backend error handling to gracefully catch quota limits (429 RESOURCE_EXHAUSTED) and authentication drops. Instead of the server crashing, the UI cleanly informs the user of the temporary bottleneck. 

☁️ **The Deployment:** I Dockerized the entire application and successfully deployed it serverless to **Google Cloud Run** using the Google Cloud CLI. 

This project was an incredible deep-dive into full-stack development, API integration, and cloud deployment! 

Check out the code on my GitHub below! 👇

🔗 GitHub Repo: [Insert Your GitHub Link Here]
🔗 Live Demo: [Insert Your Cloud Run Link Here]

#SoftwareEngineering #FastAPI #Python #GoogleCloud #GeminiAI #WebDevelopment #CivicTech #Docker
