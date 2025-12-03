from pydantic_ai import Agent
from dotenv import load_dotenv


load_dotenv ()

restaurant_agent = Agent(model="google-gla:gemini-2.5-flash", system_prompt= "Give me five restaurants")