from flask import Flask
from flask import request
from flask_cors import CORS
import json

app = Flask(__name__)  
CORS(app)

@app.route("/")
def index():
    result = {}
    result['itens'] = ["Balass","Chocolate","Caramelo"]
    return json.dumps(result)

app.run(debug=True, host='0.0.0.0', port=5000)
