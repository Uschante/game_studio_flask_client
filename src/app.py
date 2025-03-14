from flask import request, url_for, jsonify
from flask_api import FlaskAPI
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = FlaskAPI(__name__)

# init openAI API client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

@app.route("/get_model_response", methods=["Post"])
def get_model_response():
    """
    Returns a model's reponse given the user prompt
    """
    prompt = request.json["prompt"]
    print(f"Got a new request with the following prompt: \n{prompt}")
    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="gpt-4o-mini"
    )
    response = completion.choices[0].message.content
    print(response)
    return jsonify(response)


@app.route("/get_echo", methods=["Post"])
def get_echo():
    """
    Returns the received message
    """
    response = request.json["message"]
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)