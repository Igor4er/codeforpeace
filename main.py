from fastapi import FastAPI, Depends
import uvicorn
import json

app = FastAPI()


@app.get(path="/get")
def get():
    return "0"


if __name__ == "__main__":
    json_data = {"questions": [1, 2, 3]}
    with open("questions.json", 'w') as json_file:
        json.dump(json_data, json_file, indent=2)

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)