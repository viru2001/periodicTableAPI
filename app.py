from flask import Flask,jsonify
import json

app = Flask(__name__)

f = open('data.json')
data =json.load(f)


@app.route('/')
def index():
    elements = []
    for element in data:
        elements.append(element)

    return jsonify(elements)


if __name__ == "__main__":
    app.run(debug=False)