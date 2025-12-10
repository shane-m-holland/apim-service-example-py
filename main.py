from fastapi import FastAPI

app = FastAPI(title="Hello API", version="1.0.0")

@app.get("/hello")
def hello():
    return {"message": "Hello, World!"}

@app.get("/goodbye")
def goodbye():
    return {"message": "Goodbye, World!"}