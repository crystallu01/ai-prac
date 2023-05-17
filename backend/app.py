from flask import Flask, jsonify
from markov_with_positions import Markov
from haiku1 import generate_haiku
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/poem/<theme>/')
def get_poem(theme):
    haiku_structure = [5, 7, 5]
    with open("haiku_data.txt") as f:
        lines = [line.strip() for line in f]
    model = Markov(lines)
    return jsonify(results=generate_haiku(model, haiku_structure, theme))
