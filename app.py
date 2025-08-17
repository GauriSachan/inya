from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/agent-webhook", methods=["POST"])
def agent_webhook():
    data = request.json
    user_message = data.get("message", "")
    reply = f"You said: {user_message}. (Reply from my Flask agent)"
    return jsonify({"reply": reply})

if __name__ == "_main_":
    app.run(host="0.0.0.0", port=5000, debug=True)