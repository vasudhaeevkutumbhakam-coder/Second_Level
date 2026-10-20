from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
app=FastAPI()
@app.get("/")
def root():
    return "WELCOME TO FASTAPI"
