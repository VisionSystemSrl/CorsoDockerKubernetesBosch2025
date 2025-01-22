from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from chromadb.config import Settings
import chromadb

# Configura ChromaDB
client = chromadb.HttpClient(host="chroma", port=8000)

# Crea un'istanza di FastAPI
app = FastAPI()

# Carica il modello locale
model = SentenceTransformer('all-MiniLM-L6-v2')

# Inizializza una collezione
collection = client.get_or_create_collection(name="embeddings")

# Definisci la struttura del corpo della richiesta
class Document(BaseModel):
    id: str
    text: str

# Endpoint per aggiungere un documento
@app.post("/add")
def add_document(document: Document):
    embedding = get_embedding(document.text)
    collection.add(
        ids=[document.id],
        documents=[document.text],
        embeddings=[embedding],
    )
    return {"message": f"Document {document.id} added successfully."}

# Endpoint per ricerca semantica
@app.get("/search")
def search(query: str):
    embedding = get_embedding(query)
    results = collection.query(
        query_embeddings=[embedding],
        n_results=5,
    )
    return results

# Funzione per calcolare embedding usando il modello locale
def get_embedding(text: str):
    return model.encode(text).tolist()
