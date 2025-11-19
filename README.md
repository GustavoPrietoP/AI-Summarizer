# 🧠 AI Text Summarizer

A simple and professional AI-powered text summarization web app built
with **Python**, **Flask**, and the **Hugging Face Inference API**.


------------------------------------------------------------------------

## 🚀 Features

-   ✨ Summarize long text into concise, readable summaries
-   ⚡ Powered by Hugging Face `facebook/bart-large-cnn` model
-   🌐 Flask backend with clean routing and error handling
-   🎨 Modern responsive UI with custom CSS
-   🔑 Secure environment variable support for API keys
-   📦 Easy to deploy on Render, Railway, or Vercel

------------------------------------------------------------------------

## 📁 Project Structure

    .
    ├── app.py
    ├── templates/
    │   └── index.html
    ├── static/
    │   └── style.css
    └── README.md

------------------------------------------------------------------------

## 🛠️ Installation & Setup

### 1. Clone the repository

``` bash
git clone https://github.com/GustavoPrietoP/AI-Summarizer.git
cd AI-Summarizer
```

### 2. Create a virtual environment (optional but recommended)

``` bash
python3 -m venv venv

source venv/bin/activate       # macOS / Linux

venv\Scripts\activate          # Windows
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🔑 API Key Setup

Create a token at:\
https://huggingface.co/settings/tokens

In ```app.py``` Replace the 
```
API_TOKEN= "{YOUR-API-KEY}" 
```
With the key generated.


------------------------------------------------------------------------

## ▶️ Run the App

``` bash
python app.py
```

Visit:

    http://127.0.0.1:5000/

------------------------------------------------------------------------

## 📌 Technologies Used

-   Python 3
-   Flask
-   Hugging Face Router Inference API
-   HTML5
-   CSS3

------------------------------------------------------------------------

## ⭐ Support

If you found this project helpful, please give it a **star ⭐** on
GitHub!
