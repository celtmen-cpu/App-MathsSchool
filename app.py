from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Base de réponses simples
RESPONSES = {
    "bonjour": ["Salut ! Comment puis-je t’aider en maths aujourd’hui ?", "Bonjour ! Pose-moi une question."],
    "merci": ["Avec plaisir !", "De rien !"],
    "addition": ["Pour additionner, ajoute simplement les nombres.", "Exemple : 2 + 3 = 5"],
    "soustraction": ["Soustraction = retrancher un nombre d'un autre.", "Exemple : 5 - 2 = 3"],
    "multiplication": ["Multiplication = répéter un nombre plusieurs fois.", "Exemple : 4 * 3 = 12"],
    "division": ["Division = partager un nombre en parts égales.", "Exemple : 12 / 4 = 3"],
}

# Fonction simple pour choisir une réponse
def get_response(message):
    msg = message.lower()
    for key in RESPONSES:
        if key in msg:
            return random.choice(RESPONSES[key])
    # Sinon réponse générique
    generic_responses = [
        "Intéressant, peux-tu préciser ?",
        "Je ne suis pas sûr, peux-tu reformuler ?",
        "Hmm… parlons de maths ! Quelle question as-tu ?"
    ]
    return random.choice(generic_responses)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = get_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run()