from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def greet():
    return " Hii there"