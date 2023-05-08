import os
import random
import openai
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/start", methods=["GET"])
def start_chat():
    prompt = f"Return the initial statement:Hi, I'm Alice and we at Reli AI understand that dating is complicated. We want to help. What is your name?"

    response = openai.Completion.create(
        model="text-curie-001", # or whichever model you're using
        prompt=prompt,
        max_tokens=500,
    )

    return jsonify({
        "message": response.choices[0].text.strip()
    })

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json['message']

    # Here, you should write the logic for generating a prompt based on the user's message
    # For now, let's just use the user's message as the prompt
    prompt = user_message

    #response = openai.Completion.create(
    #    model="text-curie-001",
    #    prompt=prompt,
    #    max_tokens=60,
    #)

    #return jsonify({
    #    "message": response.choices[0].text.strip()
    #})

def get_openai_response(prompt):
    # Your code for generating the response using the OpenAI API
    pass



if __name__ == "__main__":
    app.run(debug=True)
