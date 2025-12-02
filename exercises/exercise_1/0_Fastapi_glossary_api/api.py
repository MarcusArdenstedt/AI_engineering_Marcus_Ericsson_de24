from data_processing import load_data, GlossaryModel
from fastapi import FastAPI, Query



glossaries = load_data("fastapi_glossary.json")

app = FastAPI()

# get all the word and meaning
@app.get("/glossary")
async def read_glossary():
    return glossaries

#Path parameter
@app.get("/glossary/{word}")
async def path_glossary_word(word: str):
    return [glossary for glossary in glossaries if glossary.word.lower() == word.lower()] 


#Query parameter
@app.get("/filter/")
async def filter_glossary(
    word: str = Query(description="filtered by word that are related to FastAPI")):
    
    filter_glossaries = glossaries
    
    if word:
        filter_glossaries = [
            glossary for glossary in filter_glossaries
            if word.casefold() in glossary.word.casefold()]
        
    return filter_glossaries
    
    
# Create a new glossary
@app.post("/glossary/create_word")
async def create_word(word: GlossaryModel):
    new_word = GlossaryModel.model_validate(word)
    
    glossaries.append(new_word)
    
    return new_word

# update glossary
@app.put("/glossary/update")
async def update_glossary(update_glossary: GlossaryModel):
    for i, glossary in enumerate(glossaries):
        if glossary.id == update_glossary.id:
            glossaries[i] = update_glossary
            
    return update_glossary
             
# Delete glossary
@app.delete("/glossary/delete")
async def delete_glossary(id: int):
    for i, glossary in enumerate(glossaries):
        if glossary.id == id:
            del glossaries[i]
            break