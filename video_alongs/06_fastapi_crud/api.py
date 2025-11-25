from fastapi import FastAPI
from data_processing import library_data
from pprint import pprint


library = library_data("library.json")
books = library.books

pprint(books)

app = FastAPI()

@app.get("/books")
async def read_books():
    return books