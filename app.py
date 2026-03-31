from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    
    # Pour l'instant : il répète juste
    response = user_message

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run()