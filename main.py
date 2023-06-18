from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Place(BaseModel):
    name: str
    description: Optional[str] = None
    coffee: bool
    wifi: bool
    food: bool
    lat: float
    lng: float

    class config: 
        orm_mode = True


@app.post('/places/')
async def create_place_view(place: Place):
    return place

@app.get('/')
async def root():
    return {'message': 'Hello World!'}