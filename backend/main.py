from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get():
    return {"code": 200, "message":"Hello World 23"}

