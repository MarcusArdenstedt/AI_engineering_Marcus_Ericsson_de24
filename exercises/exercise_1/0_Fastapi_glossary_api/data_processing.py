from constants import DATA_PATH
import json
from pydantic import BaseModel
from pprint import pprint


def read_data(filename: str):
    with open(DATA_PATH / filename, "r") as file:
        data = json.load(file)
    return data


class GlossaryModel(BaseModel):
    id: int
    word: str
    meaning: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 15,
                "word": "parsed",
                "meaning": """omvandlar från text till Python-objekt enligt schema. 
            Det gör om texten till riktigt objekt som man sen kan använda.""",
            }
        }
    }


def load_data(filename):
    json_data = read_data(filename)
    return [GlossaryModel(**item) for item in json_data]


if __name__ == "__main__":

    # pprint(read_data("fastapi_glossary.json"))
    pprint(load_data("fastapi_glossary.json"))
