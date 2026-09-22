
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pymupdf
from storeinlist import liststorage
from pydantic import BaseModel
from chunks import createchunks
from embeddingmodelloading import loadembeddingmodel
from embeddingsCreation import createembeddings
from embeddingsStorage import storeEmbeddings
from queryembedding import createqueryembedding
from searchcontext import searchforcontext
import faiss
from llmcalling import callLLm


app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Chunks = []
embedding_model = loadembeddingmodel()
index = faiss.IndexFlatL2(384)

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    global Chunks
    global index
    documents = liststorage(file)
    Chunks = createchunks(documents)   
    embeddings = createembeddings(Chunks,embedding_model)
    index = storeEmbeddings(embeddings, index)

    return {
        "message": "File received successfully",
        "filename": file.file
    }


class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def query_rag(query: QueryRequest):
    global Chunks
    userQuery = query.query.strip()
    if not userQuery:
        return{
            "number":0,
            "errors" : "Please Enter a Query"
        }
    else:
        if not Chunks:
            return{
                "number": 0,
                "errors" : "No Documents Found to Proceed"
            }
        else:
            global index
            query_embedding = createqueryembedding(userQuery, embedding_model)
            context = searchforcontext(Chunks, query_embedding,  index)
            answer = callLLm(userQuery, context)
            print("successfully fetched data")

            return{
                "query" : userQuery,
                "answer": answer
            }
            

   

