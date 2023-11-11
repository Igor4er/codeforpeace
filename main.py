from fastapi import FastAPI, Depends
import uvicorn
import json
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    category = str
    question = str
    answers = list(Answer)

class Answer(BaseModel):
    option = str
    impact = Impact

class Impact(BaseModel):
    category = str
    value = int

QUESTIONS = []
with open("questions.json", 'r', encoding='utf-8') as json_file:
        QUESTIONS =  json.load(json_file)

@app.get(path="/get_questions")
def get_questions():
    return QUESTIONS


@app.post(path="/apply_answers")
def apply_answers():
    pass

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)