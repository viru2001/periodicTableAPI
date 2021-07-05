from flask import Flask,jsonify,Response
import json

app = Flask(__name__)

f = open('data.json')
data =json.load(f)


# @app.route('/')
# def index():
#     elements = []
#     for element in data:
#         elements.append(element)

#     return jsonify(elements)

@app.route('/',methods = ['GET'])
def index():
    elements = []
    for element in data:
        elements.append(element)

    js = json.dumps(elements)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Credentials"] = True
    return resp
    

if __name__ == "__main__":
    app.run(debug=False)