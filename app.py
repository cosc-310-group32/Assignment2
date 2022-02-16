# Cteate simple chatbot with flask


from flask import Flask, request, render_template, jsonify
import json
import os

app = Flask(__name__, template_folder='template')

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.form["user_input"]
    chatbot_response = chat_bot_response(user_input)
    return jsonify({"chatbot_response": chatbot_response})

def chat_bot_response(user_input: str) -> str:
    with open(os.path.join(os.path.dirname(__file__), "data.json"), "r") as f:
        data = json.load(f)
    for item in data["items"]:
        if item["question"] == user_input:
            return item["answer"]
    return "Sorry, I don't understand what you mean"

if __name__ == "__main__":
    app.run(debug=True)