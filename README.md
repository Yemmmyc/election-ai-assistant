# NaijaVote AI - Nigerian Election Assistant 🇳🇬

**🔗 Live Demo: [https://naijavote-ai-797322343792.us-central1.run.app](https://naijavote-ai-797322343792.us-central1.run.app)**

A production-ready, cloud-native AI chatbot designed to educate and assist voters in Nigeria. Built with a modern, glassmorphism UI and powered by Google's Gemini AI, this application provides accurate, neutral civic information regarding voter registration, polling units, and election dates.

---

## 🎯 Submission Overview

### 1. Chosen Vertical
**Election Process Education**
The mission of this project is to create an interactive AI assistant that helps users navigate the complexities of the Nigerian election process. It serves as an accessible guide for voter registration, polling unit navigation, and civic responsibilities.

### 2. Approach and Logic
The solution is designed with a **"Clean & Constrained"** logic model:
- **System Instructions:** The Gemini API is strictly instructed to adopt the persona of a neutral, official Nigerian Election Assistant. This constrains the AI from answering non-civic questions and ensures the information remains focused and relevant to the user context.
- **Robust Fallbacks & Exception Handling:** AI models often face rate limits and traffic spikes (e.g., 503 UNAVAILABLE or 429 RESOURCE_EXHAUSTED exceptions). The backend features an exponential backoff retry mechanism to automatically recover from temporary outages. If the quota limit persists, it serves a graceful fallback message, preventing server crashes and ensuring a seamless user experience.
- **Premium User Experience:** The frontend logic completely bypasses heavy frameworks in favor of high-performance Vanilla JavaScript and CSS glassmorphism, ensuring accessibility and extremely fast load times.

### 3. How the Solution Works
- **Frontend Layer:** A dark-themed web interface captures user queries and displays real-time typing indicators. It communicates via async `fetch` requests to a REST API.
- **Backend Layer:** A Python-based `FastAPI` server processes the incoming requests and maintains in-memory conversation history sessions.
- **Google Services Integration:** The backend securely routes the query to Google's `gemini-2.5-flash` model using the latest `google-genai` SDK.
- **Deployment:** The entire application is containerized using Docker and deployed as a serverless web app on **Google Cloud Run**, ensuring it can scale from zero to millions of users automatically.

### 4. Assumptions Made
- **Assumption 1 (Language):** It is assumed that the primary interactions will be in English or Pidgin English, which the Gemini model is inherently capable of processing.
- **Assumption 2 (Connectivity):** The UI assumes users might have varying connection speeds, hence the implementation of asynchronous loading indicators.
- **Assumption 3 (Cloud Quotas):** It is assumed that the production environment will utilize a paid Google Cloud billing account to handle high traffic without hitting free-tier constraints.

---

## 🚀 Features
- **Intelligent Assistant:** Powered by the latest `gemini-2.5-flash` model via the `google-genai` SDK.
- **Contextual Memory:** Maintains session-based chat history, allowing the AI to remember the context of your ongoing conversation.
- **Premium User Interface:** Custom, dark-themed vanilla JavaScript frontend featuring glassmorphism, auto-resizing text inputs, and smooth micro-animations.
- **Robust Error Handling:** Features exponential backoff retry logic and gracefully handles API rate limits without crashing the server.
- **Cloud-Native Deployment:** Fully Dockerized for Google Cloud Run.

## 🛠️ Tech Stack
- **Frontend:** Vanilla HTML5, CSS3, JavaScript
- **Backend:** Python, FastAPI, Uvicorn
- **AI Integration:** Google Gemini API (`google-genai`)
- **Containerization:** Docker
- **Cloud Platform:** Google Cloud Run

## 💻 Local Development Setup

### Prerequisites
- Python 3.10+
- A Google Gemini API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Yemmmyc/election-ai-assistant.git
   cd election-ai-assistant
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Environment Variables**
   Create a `.env` file in the root directory and add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

4. **Run the server**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the App**
   Open your browser and navigate to `http://localhost:8000`

## 🐳 Docker Deployment

To build and test the Docker container locally:
```bash
docker build -t naijavote-ai .
docker run -p 8080:8080 --env-file .env naijavote-ai
```

## 📝 License
This project is open-source and available under the MIT License.
