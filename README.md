---

# 📘 REST + Flask + FastAPI — Beginner’s Guide

This guide explains the **basics of REST APIs**, followed by how to implement them in **Flask** and **FastAPI**.
It’s written for complete beginners who know Python basics.

---

## 🌍 What is REST?

* **REST** = **Representational State Transfer**
* An **architecture style** for building APIs.
* APIs built this way are called **RESTful APIs**.
* REST uses **HTTP protocol** to let software systems talk to each other.

---

## 🧩 Core Concepts of REST

1. **Resources**

   * Everything is a resource (users, posts, products, etc).
   * Each resource has a **URL (endpoint)**.

     ```
     /users      → all users
     /users/1    → user with id=1
     ```

2. **HTTP Methods (CRUD operations)**

   | HTTP Method | Purpose        | Example                         |
   | ----------- | -------------- | ------------------------------- |
   | GET         | Read           | `GET /users` → fetch all users  |
   | POST        | Create         | `POST /users` → create new user |
   | PUT         | Update         | `PUT /users/1` → update user 1  |
   | PATCH       | Partial Update | `PATCH /users/1`                |
   | DELETE      | Delete         | `DELETE /users/1`               |

3. **Stateless**

   * Each request must contain all required info.
   * Server does not "remember" previous requests.

---

## ⚙️ Building REST API with Flask

### 🔧 Setup

```bash
pip install flask
```

### 📝 app.py

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Fake database
users = [{"id": 1, "name": "Owais"}, {"id": 2, "name": "Sarthak"}]

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    new_user = request.json
    new_user["id"] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    user.update(data)
    return jsonify(user)

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(debug=True)
```

### 🚀 Run

```bash
python app.py
```

### 🔗 Endpoints

* `GET /users` → Get all users
* `GET /users/1` → Get user with ID 1
* `POST /users` → Create new user
* `PUT /users/1` → Update user with ID 1
* `DELETE /users/1` → Delete user with ID 1

---

## ⚡ Building REST API with FastAPI

### 🔧 Setup

```bash
pip install fastapi uvicorn
```

### 📝 main.py

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Fake database
users = [{"id": 1, "name": "Owais"}, {"id": 2, "name": "Sarthak"}]

# Input schema
class User(BaseModel):
    name: str

@app.get("/users")
def get_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users", status_code=201)
def create_user(user: User):
    new_user = {"id": len(users) + 1, "name": user.name}
    users.append(new_user)
    return new_user

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user["name"] = updated_user.name
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users
    users = [u for u in users if u["id"] != user_id]
    return {"message": "User deleted"}
```

### 🚀 Run

```bash
uvicorn main:app --reload
```

Server will run at 👉 `http://127.0.0.1:8000`

---

## 🧩 FastAPI Superpowers

* **Automatic Docs**:

  * Swagger UI 👉 `http://127.0.0.1:8000/docs`
  * ReDoc 👉 `http://127.0.0.1:8000/redoc`

* **Built-in validation** with Pydantic (`BaseModel`).

* **Async support** → much faster than Flask.

---

## 🔁 Quick Comparison (Flask vs FastAPI)

| Feature       | Flask                          | FastAPI 🚀                   |
| ------------- | ------------------------------ | ---------------------------- |
| Setup         | Minimal, you add more manually | Everything built-in for APIs |
| Type checking | Not strict                     | Uses `pydantic` validation   |
| Speed         | Slower (sync only)             | Much faster (async ready)    |
| Docs          | Need extra setup               | Auto-generated (Swagger)     |

---

## ✅ What You Learned

* Basics of REST architecture.
* CRUD operations with HTTP methods.
* How to build REST API with Flask.
* How to build REST API with FastAPI.
* Key differences between Flask & FastAPI.

---

👉 Save this as `README.md` in your project folder.
When revising, just read this doc — you’ll recall everything quickly.

Do you also want me to **add diagrams** (like request flow + CRUD mapping) into the README to make it even easier to visualize?
