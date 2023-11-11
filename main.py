from fastapi import FastAPI, Depends
import uvicorn

app = FastAPI()


@app.get(path="/get")
def get():
    return "0"


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)