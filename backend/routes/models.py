from settings import app
from flask import jsonify
import nltk

@app.route ('/models')
def models():

    return jsonify({"models": ["sentiment_model", "chatbot_model"]})


print("hello world")