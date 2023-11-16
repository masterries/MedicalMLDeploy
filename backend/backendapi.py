from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Willkommen zur FastAPI-Anwendung! - 2"}