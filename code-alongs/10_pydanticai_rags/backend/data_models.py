from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry
from dotenv import load_dotenv
from pydantic import Field, BaseModel


load_dotenv()

embedding_model = get_registry().get("gemini-text").create(name= "gemini-embedding-001")

EMBEDDING_DIM = 3072


class Article(LanceModel):
    """Represents a wikipedia article with its corrensponding embedding"""
    doc_id: str 
    filepath: str
    filename: str = Field(description= "stem of the file, without suffix")
    content: str = embedding_model.SourceField()
    embedding: Vector(EMBEDDING_DIM) = embedding_model.VectorField()


class Prompt(BaseModel):
    prompt: str = Field(description="prompt from user")
    
class RagResponse(BaseModel):
    filename: str = Field(description= "filename of retrienved without suffix")
    filepath: str = Field(description= "absolute path to retrieved file")
    answer: str = Field( description= "answer based retrieved file")

