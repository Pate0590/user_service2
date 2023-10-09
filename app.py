# user_service.py

from flask import Flask, jsonify, request
users = {
        '1': {'name': 'Alice', 'email': 'alice@example.com'},
        '2': {'name': 'Bob', 'email': 'bob@example.com'}
}

app = Flask(__name__)

@app.route('/user/<id>')
def user(id):

    user_info = users.get(id, {})
    print(user_info)
    return jsonify(user_info)

@app.route('/user', methods=['POST'])
def create_user():
    new_user = request.get_json()
    
    # Define a list of required keys
    required_keys = ['name', 'email']

    # Check if all required keys exist in the request data
    if all(key in new_user for key in required_keys):
        users[str(len( users.keys()) + 1)] = new_user
        print( users)
        return jsonify({"success":True})
    else:
        return jsonify({"success":False, "msg": "Please pass all the data"})
    
@app.route('/user/<id>', methods=['PUT'])
def update_user(id):
    # Check if the user ID exists
    if id in  users:
        updated_user = request.get_json()

        # Check if the required keys are present in the request data
        required_keys = ['name', 'email']
        if all(key in updated_user for key in required_keys):
            users[id] = updated_user
            print( users)
            return jsonify({"success": True, "msg": "user updated successfully"})
        else:
            return jsonify({"success": False, "msg": "Please pass all the required data for update"}), 400
    else:
        return jsonify({"success": False, "msg": "user not found"}), 404
    
@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    if id in  users:
        # If the user with the given ID exists, delete it
        del  users[id]
        return jsonify({"success": True, "msg": "user deleted successfully"})
    else:
        return jsonify({"success": False, "msg": "user not found"}), 404





if __name__ == '__main__':
    app.run()