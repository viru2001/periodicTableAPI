import re
from flask import Flask,jsonify,Response,request
import json

app = Flask(__name__)

f = open('data.json')
data =json.load(f)

def makeResponse(js):
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Credentials"] = "true"
    resp.headers["Access-Control-Allow-Methods"] = "GET"
    return resp
    
@app.route('/')
def allElements():
   
        elements = []
        for element in data:
            elements.append(element)

        js = json.dumps(elements)
        resp = makeResponse(js)
        return resp
        
@app.route("/block")
def block():
    elements = []
    blocks = ["s","d","p","f"]
    if "block" in request.args:
        blockName = request.args['block']
        if blockName in blocks:
            for element in data:
                if element['block'] == blockName:
                    elements.append(element)

            js = json.dumps(elements)
            resp = makeResponse(js)
            return resp
        else:
            message = "data does not exist"
            js = json.dumps(message)
            resp = makeResponse(js)
            return resp
    else:
        message = "data does not exist"
        js = json.dumps(message)
        resp = makeResponse(js)
        return resp






if __name__ == "__main__":
    app.run(debug=False)