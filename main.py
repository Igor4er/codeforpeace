from fastapi import FastAPI, Depends
import uvicorn
import json

app = FastAPI()


@app.get(path="/get_questions")
def get_questions():
    with open("questions.json", 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


if __name__ == "__main__":
    # json_data = {"questions": [1, 2, 3]}
    # with open("questions.json", 'w') as json_file:
    #     json.dump(json_data, json_file, indent=2)

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)