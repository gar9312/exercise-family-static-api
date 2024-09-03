"""
This module is responsible for starting the API server, loading the database, and adding the corresponding endpoints.
"""
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

# Initialize the Flask application
app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the Jackson family instance
jackson_family = FamilyStructure("Jackson")

# Handle errors and serialize them into JSON format
@app.errorhandler(APIException)
def handle_errors(error):
    return jsonify(error.to_dict()), error.status_code

# Generate the sitemap with all available endpoints
@app.route('/')
def show_sitemap():
    return generate_sitemap(app)

# Get all members of the family
@app.route('/members', methods=['GET'])
def get_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# Add a new member to the family
@app.route('/member', methods=['POST'])
def add_member():
    body = request.get_json()
    new_member = {
        "id": body.get("id", jackson_family._generate_id()),
        "first_name": body.get("first_name"),
        "last_name": body.get("last_name"),
        "age": body.get("age"),
        "lucky_numbers": body.get("lucky_numbers")
    }
    
    if new_member["last_name"] is not None:
        return jsonify({"error": "The last name is generated automatically. Do not send it in the body."}), 400
    
    for member in jackson_family._members:
        if new_member["id"] == member["id"]:
            return jsonify({"error": "The ID is already in use"}), 400
    
    accepted_member = jackson_family.add_member(new_member)
    return jsonify(accepted_member), 200

# Get a specific member by ID
@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    if member is None:
        return jsonify({"error": "Member not found"}), 404
    return jsonify(member), 200

# Delete a specific member by ID
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    deleted_member = jackson_family.delete_member(member_id)
    if deleted_member:
        return jsonify({"done": True}), 200
    return jsonify({"error": "Member not found"}), 404

# Run the server only if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
