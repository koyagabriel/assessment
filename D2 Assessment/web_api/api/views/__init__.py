from flask import jsonify

def index():
    return jsonify({
        "status": True,
        "message": "Welcome to Flask Homepage"
    })
