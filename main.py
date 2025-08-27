from fastapi import FastAPI

app = FastAPI(title="Hello API", version="1.0.0")

@app.get("/")
def hello():
    return {"message": "Hello, World!"}
