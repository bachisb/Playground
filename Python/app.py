
from flask import Flask

app = Flask(__name__)

# POST /store data: {name}
@app.route('/store', methods=['POST'])
def creat_store():
    pass

# GET /store/<<string:name>>
@app.route('/store/<<string:name>>', methods=['GET'])
def get_store(name):
    return "Hello world"

# GET /store
@app.route('/store', methods=['GET'])
def get_store():
    pass

# POST /store data: {name}
@app.route('/store/<<string:name>>/item', methods=['POST'])
def creat_item_in_store(name):
    pass

# GET /store
@app.route('/store/<<string:name>>/item', methods=['GET'])
def get_items_in_store():
    pass

app.run(port=5000)
