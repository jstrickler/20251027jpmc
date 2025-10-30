from enum import Enum
from typing import Annotated
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

class CountryCode(str, Enum):
    us = "US"
    canada = "CA"
    england = "UK"


class Zombie(BaseModel):
    name: str
    speed: int

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/zombie")
async def create_zombie(zombie: Zombie):
    # add this zombie to the database (or whatever...)
    # new_zombie = DBZombie()
    # new_zombie.name = zombie.name
    # new_zombie.speed = zombie.speed
    # new_zombie.save()
    return zombie

@app.get("/zombie/{country}/{zombie_id}")
async def zombie(
    country: CountryCode, 
    zombie_id: Annotated[int, Path(description="Integer zombie id (range 1-9999)", title="Zombie-ID", gt=0, le=9999)], 
    is_dead: bool=True, 
    details: str="full", 
    diet: str="Brains"
):
    return {
        "id": zombie_id, 
        "country": country,
        "details": details,
        "is_dead": is_dead,
        "diet": diet,
    }