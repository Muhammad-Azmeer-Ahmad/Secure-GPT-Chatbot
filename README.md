# 🤖 Secure GPT Chatbot

A **secure AI-powered chatbot** built using **Django** and **OpenAI’s GPT API**, designed to demonstrate **AI integration**, **frontend-backend communication**, and **secure data handling** within a modern web environment. 💬🔐

![Image Alt](https://github.com/user-attachments/assets/8ae5ac39-2afd-47a8-93d1-6b7bf9530b90)
![Image Alt](https://github.com/user-attachments/assets/c4e21d69-b86e-49b4-8dfa-5188004148ba)



---

## ⚠️ Important Note

This project is **not connected to any live OpenAI API** at the moment.
It is intended **for educational and portfolio purposes** 🧠 — demonstrating how to integrate a chatbot frontend with a Django backend securely.

🛠️ **You can:**
* Clone and explore the structure
* Connect your own OpenAI API key later
* Modify and deploy for testing or learning

✅ Perfect for **students**, **junior developers**, and **cybersecurity learners** exploring **AI & Django integration**!

---

## 🚀 Features

* **Frontend Chat Interface**: Clean, animated chat UI with a starry background ✨
* **Django Backend**: Handles user messages and communicates with the AI endpoint.
* **Secure Design**: Uses environment variables (`.env`) for keys and sensitive data 🔐
* **Static Files Setup**: Includes CSS, JS, and media integration for easy customization.
* **Modular App Structure**: Clearly separated `chatbot` app for better scalability.

---

## 📦 Clone & Run Locally

### 1️⃣ Clone the repository

```bash
git clone [https://github.com/muhammadazmeerahmad/SecureGPTChatbot](https://github.com/muhammadazmeerahmad/SecureGPTChatbot)
cd SecureGPTChatbot
```
### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```
### 3️⃣ Activate it
Windows:
```bash
venv\Scripts\activate
```
Linux:
```bash
source venv/bin/activate
```
### 4️⃣ Install dependencies 
```bash
pip install -r requirements.txt
```
### 5️⃣ Create your .env file
Inside the root folder (next to manage.py), create a file named .env:
```bash
DJANGO_SECRET_KEY=your-secret-django-key
DEBUG=True
OPENAI_API_KEY=sk-xxxxxxx  # optional if available
```
### 6️⃣ Run the Server
```bash
python manage.py runserver
```

# Project Structure:
``` bash
SecureGPTChatbot/
│
├── manage.py
├── requirements.txt
├── .env                      # Environment variables file
│
├── secure_gpt_chatbot/       # Main Django project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── chatbot/                  # Chatbot Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   └── static/
│       ├── script.js
│       ├── styles.css
│       ├── starry-background.css
│       └── astro.jpeg
│
├── static/                   # Global static assets
│   ├── script.js
│   ├── styles.css
│   ├── starry-background.css
│   └── astro.jpeg
│
├── templates/                # HTML templates (global)
│   ├── base.html
│   └── index.html
│
├── utils/                    # Helper utilities
│   ├── __init__.py
│   └── utils.py
│
├── db.sqlite3
└── venv/                     # Virtual environment (auto-generated)
    ├── bin/
    ├── lib/
    ├── include/
    └── pyvenv.cfg
```
## 🛠️ Technologies Used

* 🐍 **Python 3.13**
* 🌐 **Django**
* 💬 **OpenAI GPT API** (optional)
* 🎨 **HTML, CSS, JavaScript**

## 🧠 Learning Outcomes

By exploring this project, you’ll learn:

* **Django app structure** and static management
* **API endpoint creation** and routing
* **Secure environment variable handling**
* **Frontend-to-backend chat data flow**

---

## ✨ Future Improvements

* Integrate real GPT responses using **OpenAI API**
* Add encrypted chat history storage (**Fernet AES**)
* Deploy publicly on **Render / Vercel / Railway**
