from pydantic import BaseModel, Field

class Movie(BaseModel):
    title: str
    year: int = Field(gt= 1970)
    genre: str = Field(description= "genre of the movie, if there are many genres, take the dominat one")
    rating: int = Field(gt= 0, lt= 6, description="higher rating the better, keeps rating realistics")
    
    
    
    
class Prompt(BaseModel):
    prompt: str = Field(description=""""
                        Prompt from user find a movie, try to find closets movie even if the user prompts something else""")