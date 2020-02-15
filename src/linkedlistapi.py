import flask
from flask import request

import service

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/link',methods=['POST'])
def create():
    req = request.get_json()
    res = service.create(req['name'],req['birthyear'])
    return res, 201

@app.route('/api/link/<int:listid>', methods=['PUT'])
def push(listid):
    req = request.get_json()
    res = service.push(listid,req['name'],req['birthyear'])
    if(res is None):
        return 'Linked List with ID : '+str(listid)+' not found.', 404
    return res, 200

@app.route('/api/link/pop/<int:listid>', methods=['GET'])
def pop(listid):
    res = service.pop(listid)
    if (res is None):
        return 'Linked List with ID : '+str(listid)+' not found or is Empty.', 404
    return res, 200

@app.route('/api/link/remove/<int:listid>', methods=['POST'])
def remove(listid):
    req = request.get_json()
    res = service.remove(listid,req['name'],req['birthyear'])
    if (res is None):
        return 'Linked List with ID : '+str(listid)+' not found.', 404
    return res, 200

@app.route('/api/link/<int:listid>', methods=['GET'])
def list(listid):
    res = service.list(listid)
    if (res is None):
        return 'Linked List with ID : '+str(listid)+' not found.', 404
    return res, 200

@app.route('/api/link/reverse/<int:listid>', methods=['GET'])
def reverse(listid):
    res = service.reverse(listid)
    if (res is None):
        return 'Linked List with ID : '+str(listid)+' not found.', 404
    return res, 200

@app.route('/api/link/<int:listid>', methods=['DELETE'])
def delete(listid):
    res = service.delete(listid)
    if (res is None):
        return 'Linked List with ID : '+str(listid)+' not found.', 404
    return '', 204

app.run()