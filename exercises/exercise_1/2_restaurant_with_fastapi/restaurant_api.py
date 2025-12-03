from fastapi import FastAPI
from pydantic_ai import Agent
from dotenv import load_dotenv
from utils import query_Duckdb
from data_model import Restaurant, Prompt


load_dotenv()

agent = Agent(
    model="google-gla:gemini-2.5-flash",
    output_type=list[Restaurant],
    system_prompt="Give me always 5 restaurants closet to the object",
)

app = FastAPI()


@app.get("/restaurant")
async def read_restaurnat():
    restaurnat = query_Duckdb("FROM restaurant;")

    return restaurnat.to_dict(orient="records")


@app.post("/restaurants")
async def create_restaurant(query: Prompt):
    result = await agent.run(query.prompt)
    restaurants = result.output


    for rests in restaurants:
        query_Duckdb(
            "INSERT INTO restaurant VALUES(?,?,?,?,?,?,?,?)",
            parameters=(
                rests.name,
                rests.type_of_food,
                rests.price_level,
                rests.rating,
                rests.short_description,
                rests.opening_hours,
                rests.longitude,
                rests.latitude
            ),
        )

    return restaurants
