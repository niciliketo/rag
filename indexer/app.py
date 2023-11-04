from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from index_data import index_handler
from ask import ask_handler
from answer_questionnaire import answer_questionnaire_handler

app = FastAPI()

origins = [
    "*",  # FastAPI server
    # add more origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {
        "message": "Make a post request to /ask to ask questions about the data"
    }

@app.get("/index_data")
def index_data():
    return index_handler()

@app.post("/ask")
def ask(query: str):
    return ask_handler(query)

@app.post("/answer_questionnaires")
def answer_questionnaires():
    file_path = answer_questionnaire_handler()
    return FileResponse(file_path)


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
