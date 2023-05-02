# main.py
# How do I find the perfect match?
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_openai_response(name, age, sex, interests, nationality, humor_type, initialmeetingplace):
    prompt = generate_prompt(name, age, sex, interests, nationality, humor_type, initialmeetingplace)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=500,
    )
    return response.choices[0].text

def generate_prompt(name, age, sex, interests, nationality, humor_type, initialmeetingplace):
    prompt = f"I'm talking to {name} for the first time. They are {age} years old, {sex}, interested in {interests}, have a {humor_type} humor, and has a ethnic background of {nationality}. I want to get to know her and vice versa. What kind of story should I tell? I want to draw her in to the story slowly, and then make her laugh. I want to make them feel comfortable. Additionally, provide a one line opening line to start me of as well. I want to sound/be casual. I don't want to act as if I already know her. I don't to be attention seeking. I want the opening line to be informal and non-presumptuous"
    return prompt
