from fastapi import FastAPI, HTTPException

app = FastAPI()

# In-memory storage
members = {}

@app.post("/api/members")
def create_member(member: dict):
    member_id = member["member_id"]
    if member_id in members:
        raise HTTPException(status_code=400, detail={"message": f"member with id: {member_id} already exists"})
    
    if member["age"] < 12:
        raise HTTPException(status_code=400, detail={"message": f"invalid age: {member['age']}, must be 12 or older"})
    
    members[member_id] = {
        "member_id": member_id,
        "name": member["name"],
        "age": member["age"],
        "has_borrowed": False
    }
    return members[member_id]