# 🚀 Building NaijaVote AI: A Cloud-Native Assistant for Nigerian Elections 🇳🇬

I'm incredibly excited to share **NaijaVote AI**, a production-ready web application I've built to help educate citizens on the Nigerian election process! 

At its core, it's designed to be an accessible, lightning-fast guide for voter registration, polling unit verification, and civic responsibilities. But what I'm most proud of is the architecture running under the hood.

Here are a few technical highlights from the build:
✅ **AI Integration & Context Memory:** Powered by Google's `gemini-2.5-flash` model via a `FastAPI` backend. I engineered a session-based memory system so the AI dynamically remembers the context of your ongoing conversation.
✅ **Robust Exception Handling:** AI APIs inevitably experience traffic spikes and rate limits (like `503` or `429` errors). Instead of crashing, the backend implements an **exponential backoff retry mechanism** to automatically recover from temporary outages. If limits persist, it degrades gracefully to keep the user experience seamless.
✅ **Premium Vanilla UI:** Completely bypassed heavy frontend frameworks to build a custom, glassmorphism UI using purely Vanilla JavaScript and CSS. Complete with smooth micro-animations and an auto-resizing text interface.
✅ **Cloud-Native:** The entire stack is containerized with Docker and deployed serverless on **Google Cloud Run**, allowing it to scale securely from zero to thousands of users.

I learned so much about robust API error handling and cloud deployments while building this. This application not only meets the requirements but exceeds them by handling edge cases (like the API rate limits) gracefully. A huge thank you to the HNG DevOps track for the continuous inspiration to build scalable, production-ready systems!

🔗 **Check out the live demo:** https://naijavote-ai-797322343792.us-central1.run.app
💻 **GitHub Repo:** https://github.com/Yemmmyc/election-ai-assistant

#DevOps #FastAPI #CloudRun #GoogleCloud #GeminiAI #WebDevelopment #SoftwareEngineering #HNG11 #Nigeria
