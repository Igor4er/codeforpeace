from fastapi import FastAPI, Depends
import uvicorn
import json
from pydantic import BaseModel, TypeAdapter
from enum import Enum
from typing import List

class CategoryEnum(str, Enum):
    wellBeing = 'Well-being'
    physicalActivity = 'Physical Activity'
    workAndStudying = 'Work and Studying'
    relationships = 'Relationships'
    socialConnections = 'Social Connections'
    stress = 'Stress'

app = FastAPI()

class Answer(BaseModel):
    option: str
    impact_on: str
    impact: int

class Question(BaseModel):
    category: CategoryEnum
    question: str
    answers: List[Answer]

QUESTIONS = []
with open("questions.json", 'r', encoding='utf-8') as json_file:
        users = json.load(json_file)
        ta = TypeAdapter(List[Question])
        QUESTIONS = ta.validate_python(users)

@app.get(path="/get_questions")
def get_questions():
    return QUESTIONS

class UsersAnswer(BaseModel):
    category: str
    question: str
    impact_on: str
    impact: int

@app.post(path="/apply_answers")
def apply_answers(answers: list[UsersAnswer]):
    myd = {}
    ansl = {}
    for answer in answers:
        if answer.impact_on not in myd:
            myd[answer.impact_on] = 0
        if answer.impact_on not in ansl:
            ansl[answer.impact_on] = 0

        myd[answer.impact_on] += answer.impact
        ansl[answer.impact_on] += 1
    return myd

        
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)