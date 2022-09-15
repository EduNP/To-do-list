from flask import Flask
from flask import request
from flask_cors import CORS
from flask import request
import os
import json

app = Flask(__name__)  
CORS(app)

listToDo = []

@app.route("/clear")
def clearList():
    listToDo.clear()
    if os.path.exists("list.json"):
        os.remove("list.json")
    return "Limpo"

@app.route("/add")
def addItem():
    args = request.args.get('item', default='', type = str)
    listToDo.append(args)
    jsonList = json.dumps(listToDo)
    file = open("list.json", "w")
    file.write(jsonList)
    file.close()
    return jsonList
    

@app.route("/")
def index():
    result = {}
    result['itens'] = listToDo
    return json.dumps(result)

app.run(debug=True, host='0.0.0.0', port=5000)
