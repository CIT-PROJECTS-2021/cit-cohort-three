from flask import Blueprint, jsonify, request

errors = Blueprint('errors', __name__)

# 404 - Not Found
@errors.app_errorhandler(404)
def not_found(error):
    return jsonify({'message': f"Resource at {request.path} not found"}), 404