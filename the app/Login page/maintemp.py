import os

import openai
from flask import Flask, redirect, render_template, request, url_for

# app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


# @app.route("/", methods=("GET", "POST"))
# def index():
def openai_index():
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        sex = request.form["sex"]
        interests = request.form["interests"]
        nationality = request.form["nationality"]
        humor_type = request.form["humor_type"]
        initialmeetingplace = request.form["initialmeetingplace"]
        
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(name, age, sex, interests, nationality, humor_type, initialmeetingplace),
            temperature=0.6,
            max_tokens=500,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(name, age, sex, interests, nationality, humor_type, initialmeetingplace):
    prompt = f"I'm talking to {name} for the first time. They are {age} years old, {sex}, interested in {interests}, have a {humor_type} humor, and has a ethnic background of {nationality}. I want to get to know her and vice versa. What kind of story should I tell? I want to draw her in to the story slowly, and then make her laugh. I want to make them feel comfortable. Additionally, provide a one line opening line to start me of as well. I want to sound/be casual. I don't want to act as if I already know her. I don't to be attention seeking."
    return prompt
