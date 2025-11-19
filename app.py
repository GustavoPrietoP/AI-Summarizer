import os
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-cnn"

API_TOKEN= "{YOUR-API-KEY}"

headers = {"Authorization": f"Bearer {API_TOKEN}"}


def summarize_text(text):
    payload = {"inputs": text}

    response = requests.post(API_URL, headers=headers, json=payload)

    # Raise error if API call failed
    response.raise_for_status()

    data = response.json()

    # Hugging Face returns a list with dict
    return data[0]["summary_text"]


@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    error = ""
    user_text = ""

    if request.method == "POST":
        user_text = request.form.get("input_text", "").strip()

        if len(user_text) < 30:
            error = "Please enter text with at least 30 characters."
        else:
            try:
                summary = summarize_text(user_text)
            except Exception as e:
                error = f"An error occurred: {e}"

    return render_template("index.html", summary=summary, error=error, input_text=user_text)


if __name__ == "__main__":
    app.run(debug=True)
