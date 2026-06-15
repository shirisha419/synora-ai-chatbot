from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
import webbrowser

app = Flask(__name__, static_folder="static")
CORS(app)

# 🧠 MEMORY
chat_history = []

SYSTEM_PROMPT = """
You are Synora AI, an intelligent assistant.

IMPORTANT BEHAVIOR RULES:
- Understand user intent (short, detailed, or medium answer)
- If user asks simply → give short answer
- If user asks in detail → give deep explanation with examples
- If user says "brief / short" → respond in 2-4 lines
- If user says "detailed / explain" → respond in structured long form
- Always match user expectation automatically
- Be clear, natural, and helpful
"""
@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    global chat_history

    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # 🧠 store user message
    chat_history.append(f"User: {user_message}")

    # keep last 10 messages only
    history_text = "\n".join(chat_history[-10:])

    prompt = f"""
{SYSTEM_PROMPT}

Conversation history:
{history_text}

Answer only the latest question clearly and briefly.
"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:1b",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "num_predict": 150,
                    "temperature": 0.7
                }
            },
            timeout=120
        )

        result = response.json().get("response", "")

        # 🧠 store assistant reply
        chat_history.append(f"Assistant: {result}")

        return jsonify({"reply": result})

    except requests.exceptions.ConnectionError:
        return jsonify({
            "error": "Ollama is not running. Start it using: ollama serve"
        }), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("\n🤖 Synora AI")
    print("=" * 40)
    print("✅ Local AI chatbot running")
    print("✅ Model: gemma3:1b")
    print("\nOpen:")
    print("   http://localhost:5000")
    print("=" * 40 + "\n")

    webbrowser.open("http://localhost:5000")
    app.run(debug=False, port=5000)