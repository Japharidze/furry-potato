import requests
from datetime import datetime

import pickledb
from fastapi import FastAPI

app = FastAPI()
db = pickledb.load('times.db', True)


@app.get("/gists/{user_id}")
async def root(user_id: str):
    """
    Fetch the public gists for the provided users

    - **user_id**: github user
    """
    last_request = db.get(user_id)
    url = f"https://api.github.com/users/{user_id}/gists"
    params = {'since' : last_request or ''}
    response = requests.get(url, params=params)
    update_timestamp(user_id)
    return {"message": response.json()}
    
@app.get("/reset_times")
async def reset_db():
    """Resets the saved timestamps for all users"""
    db.deldb()

def update_timestamp(user_id: str):
    db.set(user_id, datetime.now().isoformat())
