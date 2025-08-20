from flask import Flask, jsonify, request

app = Flask(__name__)

# Fake database - list of dictionaries
users = [
    {"id": 1, "name": "Owais"},
    {"id": 2, "name": "Sarthak"}
]       


# 1. GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


# 2. GET single user by id
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

# 3. POST (create a new user)
@app.route("/users", methods=["POST"])
def create_user():
     new_user = request.json
     new_user["id"] = len(users) + 1
     users.append(new_user)
     return jsonify(new_user), 201


# 4. PUT (update user)
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next(( u for u in users if u["id"] == user_id),None)
    if not user:
        return jsonify({"error": "no user found"}), 404
    
    data = request.json
    user.update(data)
    return jsonify(user)


# 5. DELETE User
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users 
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message":"user deleted successfully"})

if __name__ == "__main__":
    app.run(debug = True)


