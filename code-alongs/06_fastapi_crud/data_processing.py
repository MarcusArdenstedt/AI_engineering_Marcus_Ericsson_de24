from constants import DATA_PATH
import json
from pprint import pprint
from pydantic import BaseModel, Field

# convenience models
def read_json(filename: str):
    with open(DATA_PATH / filename, "r") as file:
        data = json.load(file)
        
    return data


# pydantic models
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int = Field(gt=1000, lt=2026, description="Year of when book is published")
    
# Validation models
class Library(BaseModel):
    name: str
    books: list[Book]
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 11,
                "title": "A really cool book",
                "author": "Coola Cooling",
                "year": 2025
            }
        }
    }
    
def library_data(filename):
    json_data = read_json(filename)
    return Library(**json_data)

# validation 
if __name__=="__main__":
    # pprint(read_json("library.json"))
    print(repr(library_data("library.json")))
