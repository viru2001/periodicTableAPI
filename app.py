import re
from flask import Flask, jsonify, Response, request
import json

app = Flask(__name__)

f = open('data.json')
data = json.load(f)


def makeResponse(js):
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Credentials"] = "true"
    resp.headers["Access-Control-Allow-Methods"] = "GET"
    return resp


@app.route('/elements')
def allElements():

    elements = []
    for element in data:
        elements.append(element)

    js = json.dumps(elements)
    resp = makeResponse(js)
    return resp


@app.route("/elements/block/<string:blockName>")
def block(blockName):
    elements = []
    blocks = ["s", "d", "p", "f"]

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


@app.route("/elements/state/<string:state>")
def state(state):
    elements = []
    states = ['liquid', 'unknown', 'solid', 'gas']

    if state in states:
        for element in data:
            if element['standardState'] == state:
                elements.append(element)

        js = json.dumps(elements)
        resp = makeResponse(js)
        return resp
    else:
        message = "data does not exist"
        js = json.dumps(message)
        resp = makeResponse(js)
        return resp


@app.route("/element/atomicNumber/<int:ano>")
def atomicNumber(ano):
    elements = []

    if ano in range(1, 119):
        for element in data:
            if element['atomicNumber'] == ano:
                elements.append(element)
                break
        js = json.dumps(elements)
        resp = makeResponse(js)
        return resp

    else:
        message = "data does not exist"
        js = json.dumps(message)
        resp = makeResponse(js)
        return resp


@app.route("/element/atomicName/<string:aname>")
def atomicName(aname):
    elements = []

    for element in data:
        if element['name'].lower() == aname.lower():
            elements.append(element)
            break
    else:
        message = "data does not exist"
        js = json.dumps(message)
        resp = makeResponse(js)
        return resp

    js = json.dumps(elements)
    resp = makeResponse(js)
    return resp


@app.route("/element/symbol/<string:symbol>")
def symbol(symbol):
    elements = []

    for element in data:
        if element['symbol'] == symbol:
            elements.append(element)
            break
    else:
        message = "data does not exist"
        js = json.dumps(message)
        resp = makeResponse(js)
        return resp
    js = json.dumps(elements)
    resp = makeResponse(js)
    return resp


@app.route("/element/electronicConfiguration/<int:ano>")
def electronicConfiguration(ano):

    for element in data:
        if element['atomicNumber'] == ano:
            element = {"configuration": element['electronicConfiguration']}
            break
    else:
        message = "data does not exist"
        js = json.dumps(message)
        resp = makeResponse(js)
        return resp
    js = json.dumps(element)
    resp = makeResponse(js)
    return resp


@app.route("/elements/bondingType/<string:bType>")
def bondingType(bType):
    elements = []
    bondingTypes = ['unknown', 'metallic',
                    'atomic', 'covalent network', 'diatomic']

    if bType in bondingTypes:
        for element in data:
            if element['bondingType'] == bType:
                elements.append(element)

        js = json.dumps(elements)
        resp = makeResponse(js)
        return resp
    else:
        message = "data does not exist"
        js = json.dumps(message)
        resp = makeResponse(js)
        return resp


@app.route("/elements/type/<string:type>")
def groupBlock(type):
    elements = []
    groupBlocks = ['metal', 'alkali metal', 'actinoid', 'halogen', 'alkaline earth metal',
                   'lanthanoid', 'metalloid', 'nonmetal', 'transition metal', 'noble gas', 'post-transition metal']

    if type in groupBlocks:
        for element in data:
            if element['groupBlock'] == type:
                elements.append(element)

        js = json.dumps(elements)
        resp = makeResponse(js)
        return resp
    else:
        message = "data does not exist"
        js = json.dumps(message)
        resp = makeResponse(js)
        return resp


@app.route("/elements/group/<int:no>")
def group(no):
    elements = []

    if no in range(1, 19):
        for element in data:
            if element['group'] == no:
                elements.append(element)
        
        js = json.dumps(elements)
        resp = makeResponse(js)
        return resp

    else:
        message = "data does not exist"
        js = json.dumps(message)
        resp = makeResponse(js)
        return resp

@app.route("/elements/period/<int:no>")
def period(no):
    elements = []

    if no in range(1, 8):
        for element in data:
            if element['period'] == no:
                elements.append(element)
        
        js = json.dumps(elements)
        resp = makeResponse(js)
        return resp

    else:
        message = "data does not exist"
        js = json.dumps(message)
        resp = makeResponse(js)
        return resp

if __name__ == "__main__":
    app.run(debug=True)
