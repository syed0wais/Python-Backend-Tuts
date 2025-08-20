from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create app
app = FastAPI()

# Fake database
users = [
    {"id": 1, "name": "Owais"},
    {"id": 2, "name": "Sarthak"}
]

# Define how input should look like (schema)
class User(BaseModel):
    name: str

# 1. GET all users
@app.get("/users")
def get_users():
    return users

# 2. GET single user by id
@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

# 3. POST (create a new user)
@app.post("/users", status_code=201)
def create_user(user: User):
    new_user = {"id": len(users) + 1, "name": user.name}
    users.append(new_user)
    return new_user

# 4. PUT (update user)
@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user["name"] = updated_user.name
    return user

# 5. DELETE user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users
    users = [u for u in users if u["id"] != user_id]
    return {"message": "User deleted"}
