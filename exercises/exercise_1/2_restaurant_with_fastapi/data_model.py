from pydantic import BaseModel, Field
from datetime import time


class Restaurant(BaseModel):
    name: str = Field(description="Name on the restaurant")
    type_of_food: str
    price_level: float = Field(description="Price based on how it is in Sweden")
    rating: float = Field(gt=0, lt= 10, description="Rate how good the restaurant is")
    short_description: str = Field(description="Short description about the restaurant")
    opening_hours: time = Field(description="Default time in Sweden for restaurants, opening and closing in HH:MM:SS format, e.g 11:00:00")
    longitude: float = Field(description= "write latitude")
    latitude: float = Field(description= "write latidude")
    

class Prompt(BaseModel):
    prompt: str 