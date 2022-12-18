from settings import app
from flask import jsonify


@app.route ('/models')
def models():

    return jsonify({"models": ["sentiment_model", "chatbot_model"]})


