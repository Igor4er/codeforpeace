from fastapi import FastAPI, Depends
import uvicorn
import json

app = FastAPI()


@app.get(path="/get_questions")
def get_questions():
    with open("questions.json", 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

@app.post(path="/apply_answers")
def apply_answers():
    pass

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)