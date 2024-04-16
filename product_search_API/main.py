import uvicorn
from fastapi import FastAPI
from routes import index

app = FastAPI()

@app.get("/")
async def read_root():
  return {"message": "Hello, world!"}

app.include_router(index.router)