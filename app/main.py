from fastapi import FastAPI
from pydantic import BaseModel
from app.langchain_bot import ask_bot

app = FastAPI()
class UserInput(BaseModel):
    input: str
    
@app.post("/ask")
async def ask(user_input: UserInput):
        response = ask_bot(user_input.input)
        return {"response": response} 

@app.get("/")
async def root():
    return {"message": "Welcome to the LangChain Bot API. Use the POST /ask endpoint to interact with the bot."}