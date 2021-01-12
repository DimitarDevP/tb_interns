from flask import jsonify, request, abort
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from config import app, jwt

@app.route('/get_token')
def create_token():
    if "id" not in request.args:
        abort(400)
    
    _id = request.args["id"]
    
    token = create_access_token(identity=_id)
    return jsonify({
        "token" : token
    })
    
@app.route('/test_token', methods=["GET", "POST"])
@jwt_required
def auth_token():
    token = get_jwt_identity()
    return jsonify({
        "token" : token
    })