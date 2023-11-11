from fastapi import FastAPI, Depends
import uvicorn
import json
from pydantic import BaseModel
from enum import Enum


class CategoryEnum(str, Enum):
    wellBeing = 'Well-being'
    physicalActivity = 'Physical Activity'
    workAndStudying = 'Work and Studying'
    relationships = 'Relationships'
    socialConnections = 'Social Connections'

app = FastAPI()

QUESTIONS = []
with open("questions.json", 'r', encoding='utf-8') as json_file:
        QUESTIONS =  json.load(json_file)

@app.get(path="/get_questions")
def get_questions():
    return QUESTIONS

class Answer(BaseModel):
    category: str
    question: str
    impact: int

@app.post(path="/apply_answers")
def apply_answers(answers: list[Answer]):
    for answer in answers:

        
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)