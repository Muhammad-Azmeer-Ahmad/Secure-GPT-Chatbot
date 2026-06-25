# Secure GPT Chatbot

A secure AI-powered chatbot built with **Django** and the **OpenAI GPT API**, demonstrating secure credential management, modular Django architecture, and real-time frontend-backend communication.

![Chat Interface](https://github.com/user-attachments/assets/8ae5ac39-2afd-47a8-93d1-6b7bf9530b90)
![Chatbot UI](https://github.com/user-attachments/assets/c4e21d69-b86e-49b4-8dfa-5188004148ba)

---

## Overview

Built for portfolio and educational purposes. The project shows how to wire a Django backend to an AI endpoint with proper secret management — no hardcoded keys, no committed credentials. Bring your own OpenAI key to go live; everything else works out of the box.

---

## Features

- Animated chat UI built in vanilla HTML/CSS/JS
- Django backend with clean URL routing and modular app structure
- Environment-based secret management via `.env`
- Pluggable OpenAI layer — connect a key and it's live

---

## Getting Started

**1. Clone**
```bash
git clone https://github.com/muhammadazmeerahmad/SecureGPTChatbot
cd SecureGPTChatbot
```

**2. Create a virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create a `.env` file** in the root (next to `manage.py`)
```env
DJANGO_SECRET_KEY=your-secret-django-key
DEBUG=True
OPENAI_API_KEY=sk-xxxxxxx
```

**5. Run**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000`

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.13 |
| Framework | Django |
| AI | OpenAI GPT API (optional) |
| Frontend | HTML, CSS, JavaScript |
| Config | `.env` / environment variables |

---

## Project Structure

```
SecureGPTChatbot/
├── manage.py
├── requirements.txt
├── .env
├── secure_gpt_chatbot/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── chatbot/
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   └── static/
│       ├── script.js
│       ├── styles.css
│       ├── starry-background.css
│       └── astro.jpeg
├── utils/
│   └── utils.py
└── db.sqlite3
```

---

## Roadmap

- [x] Secure environment variable configuration
- [x] Modular Django app structure
- [x] Animated chat UI
- [ ] Live GPT responses via OpenAI API
- [ ] Encrypted chat history (Fernet AES)
- [ ] Public deployment (Render / Railway)
- [ ] User auth + per-session conversation history
