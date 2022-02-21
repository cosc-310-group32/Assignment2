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
    
    max_item = {
        "value": 0,
        "answer": None
    }
    for item in data["items"]:
        cnt = 0
        for keyword in item["keywords"]:
            if keyword in user_input.lower():
                cnt += 1
        if cnt > max_item["value"]:
            max_item = {
                "value": cnt,
                "answer": item["answer"]
            }
    
    print(max_item)
    if max_item["value"] == 0:
        return "Sorry, I don't understand what you mean. Can you ask another question?"
    return max_item["answer"]

if __name__ == "__main__":
    app.run(debug=True)