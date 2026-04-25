# NaijaVote AI - Nigerian Election Assistant 🇳🇬

A production-ready, cloud-native AI chatbot designed to educate and assist voters in Nigeria. Built with a modern, glassmorphism UI and powered by Google's Gemini AI, this application provides accurate, neutral civic information regarding voter registration, polling units, and election dates.

## 🚀 Features

- **Intelligent Assistant:** Powered by the latest `gemini-2.0-flash` model via the `google-genai` SDK.
- **Premium User Interface:** A custom, dark-themed vanilla JavaScript frontend featuring glassmorphism, smooth micro-animations, and ambient background glows.
- **Robust Error Handling:** Gracefully handles API rate limits (`429 RESOURCE_EXHAUSTED`) and authentication errors without crashing the server.
- **Cloud-Native Deployment:** Fully Dockerized and configured for seamless deployment to Google Cloud Run.

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
   git clone https://github.com/yourusername/election-ai-assistant.git
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

## ☁️ Google Cloud Run Deployment

This project includes a `.gcloudignore` and `Dockerfile` perfectly tuned for Google Cloud Run.

1. Ensure the Google Cloud CLI is installed and authenticated.
2. Run the deployment command from the project root:

```bash
gcloud run deploy naijavote-ai \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars="GEMINI_API_KEY=your_api_key_here"
```

## 📝 License
This project is open-source and available under the MIT License.
