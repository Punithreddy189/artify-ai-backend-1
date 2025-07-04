# Artify AI Backend 🧠

Flask backend server for Artify AI that connects to Replicate's style transfer model.

## Features
- CORS-enabled Flask API
- `/style-transfer` POST endpoint
- Uses Replicate API (img2img with prompt-based style)

## Setup

```bash
pip install -r requirements.txt
export REPLICATE_API_TOKEN=your_token_here
python app.py
```

## Deployment (Render)

1. Push this repo to GitHub
2. Go to [https://render.com](https://render.com)
3. Create a new Web Service → Connect this repo
4. Set environment variable `REPLICATE_API_TOKEN`
5. Done 🎉