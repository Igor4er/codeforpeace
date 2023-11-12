from fastapi import FastAPI, Depends
import uvicorn
import json
from pydantic import BaseModel, TypeAdapter
from enum import Enum
from typing import List
from models import Answer as DBAnswer
from auth import JWTBearer
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware

class CategoryEnum(str, Enum):
    wellBeing = 'wellBeing'
    physicalActivity = 'physicalActivity'
    workAndStudying = 'workAndStudying'
    relationships = 'relationships'
    socialConnections = 'socialConnections'
    stress = 'stress'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
    impact_on: CategoryEnum
    impact: int

class UsrAns(BaseModel):
    user: str
    answers: List[UsersAnswer]

class User(BaseModel):
    name: str

@app.post(path="/apply_answers")
def apply_answers(uanswers: UsrAns, user: Annotated[User, Depends(JWTBearer())],):
    myd = {key: 0 for key in CategoryEnum}
    ansl = {key: 0 for key in CategoryEnum}
    answers = uanswers.answers
    for answer in answers:
        myd[answer.impact_on] += answer.impact
        ansl[answer.impact_on] += 1
    for key in myd.keys():
        if ansl[key] == 0:
            myd[key] = 0
        else:
            myd[key] /= ansl[key]
            if ansl[key] < 3:
                myd[key] = 0

    DBAnswer.create(
        user=user.name,
        well_being=myd[CategoryEnum.wellBeing],
        physical_activity=myd[CategoryEnum.physicalActivity],
        stress=myd[CategoryEnum.stress],
        social_connections=myd[CategoryEnum.socialConnections],
        work_and_studying=myd[CategoryEnum.workAndStudying],
    )
    return myd


@app.get(path="/get_statistics")
def get_statistics(user: str):
    data = []
    records = DBAnswer.select().where(user==user)
    for record in records:
        data.append({"well_being": record.well_being,
                    "physical_activity": record.physical_activity,
                    "stress": record.stress,
                    "social_connections": record.social_connections,
                    "work_and_studying": record.work_and_studying,
                    "month": record.date.month,
                    "day": record.date.day,
                    "weekday": record.date.weekday()})
    return data


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)