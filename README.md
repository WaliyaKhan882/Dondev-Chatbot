# 🚀 DonDev Assistant - AI-Powered Business Consultant

## About
DonDev Assistant is an intelligent chatbot that represents DonDev (dondev.live), a software services startup specializing in automated solutions. This AI assistant helps potential clients learn about services, technologies, and how automation can transform their business.

## Features
- 🤖 Powered by GROQ's Llama 3.3 70B model
- 💼 Professional business consultant personality
- 🎨 Modern, user-friendly Gradio interface
- 🔒 Secure API key management
- 📱 Responsive design

## Local Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your GROQ API key:
```bash
# Windows PowerShell
$env:GROQ_API_KEY="your-api-key-here"

# Linux/Mac
export GROQ_API_KEY="your-api-key-here"
```

3. Run the application:
```bash
python app.py
```

## Deployment on Hugging Face Spaces

1. Create a new Space on [Hugging Face](https://huggingface.co/spaces)
2. Choose "Gradio" as the SDK
3. Upload `app.py` and `requirements.txt`
4. Go to Settings → Repository secrets
5. Add `GROQ_API_KEY` with your API key value

## Technologies Used
- **Gradio**: UI framework for ML/AI applications
- **GROQ**: Fast LLM inference API
- **Llama 3.3 70B**: Advanced language model
- **Python**: Backend programming

## About DonDev
DonDev provides cutting-edge automated solutions for modern businesses, specializing in custom software development, AI integration, and workflow automation.

Website: [dondev.live](https://dondev.live)
