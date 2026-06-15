# Synora-ai-chatbot

A Python AI chatbot with **live web search** powered by Claude claude-sonnet-4-6.  
Searches the internet and answers ANY question in real time.

---

## ⚡ Setup (3 steps)

### Step 1 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 2 — Set your Anthropic API key
Get your free key at: https://console.anthropic.com/

**Windows:**
```cmd
set ANTHROPIC_API_KEY=sk-ant-your-key-here
```

**Mac / Linux:**
```bash
export ANTHROPIC_API_KEY=sk-ant-your-key-here
```

### Step 3 — Run the chatbot
```bash
python app.py
```

Then open your browser at: **http://localhost:5000** 🎉

---

## 🗂 Project Structure

```
chatbot/
├── app.py              ← Python Flask backend (API calls, web search)
├── requirements.txt    ← Dependencies
├── README.md           ← This file
└── static/
    └── index.html      ← Frontend chat UI
```

---

## 🧠 What you learn from this project

| Skill | Where it's used |
|-------|----------------|
| Python | app.py — Flask server, Anthropic SDK |
| REST APIs | POST /chat endpoint, calling Anthropic API |
| JSON | Request/response handling between frontend and backend |
| Prompt Engineering | System prompt in app.py |
| LLMs | Claude claude-sonnet-4-6 via Anthropic SDK |
| Web Search | web_search tool in the agentic loop |
| Chatbot Dev | Multi-turn conversation history management |
| Flask | Backend web framework |

---

## 💡 How it works

```
User types question
      ↓
Frontend (index.html) sends POST /chat with JSON
      ↓
Backend (app.py) calls Anthropic API with web_search tool
      ↓
Claude searches the web → reads sources → writes answer
      ↓
Backend returns JSON response
      ↓
Frontend renders markdown answer with syntax highlighting
```
