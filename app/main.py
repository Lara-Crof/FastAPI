from datetime import datetime
from enum import Enum
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title ="Trading_App"
)


fake_users =[
    {"id":1, "role":"admin", "name":"Bob"},
    {"id":2, "role":"investor", "name":"Bo b2"},
    {"id":3, "role":"trader", "name":"Stiv"},
    {"id":4, "role":"goueset", "name":"Jakke", "degree":[{ "id":1, "create_at":"22022-01-01T00:00:00", "type_degree": "expert"}
    ]},
]

class DegreeType(Enum):
    newbie ="newbie"
    expert ="expert"


class Degree(BaseModel):
    id: int
    create_at: str
    type_degree: str

class User(BaseModel):
    id: int
    role: str
    name: str
    degree:Optional[List[Degree]]= []

@app.get("/user/{user_id}", response_model=List[User])
def get_url(user_id: int):
    return [user for user in fake_users if user.get("id")== user_id]

fake_trader =[
    {"id":1, "user_id":1, "currency":"BTC", "side":"buy", "price":123, "autom":2.12},
    {"id":2, "user_id":3, "currency":"BTC", "side":"sell", "price":1233, "autom":2.52},
 ]

@app.get("/tradws")
def get_trades(limit: int = 1, offset: int= 0):
    return fake_trader[offset:][:limit]


fake_user2 =[
    {"id":1, "role":"admin", "name":"Bosb"},
    {"id":2, "role":"investor", "name":"Bo b2"},
    {"id":3, "role":"trader", "name":"Stiv"},
    {"id":4, "role":"goueset", "name":"Jakke"},
]

@app.post("/user/{user_id}") 
def change_user_name( user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id")== user_id,  fake_user2))[0]
    current_user["name"]= new_name
    return{ "status": 200, "data":current_user}

class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field( max_length=5)
    side: str
    price: float = Field(ge=0)
    ammount: float

@app.post("/trades")
def add_trades( trades: List[Trade]):
    fake_trader.extend(trades)
    return{'status':200, "data": fake_trader}