from fastapi import FastAPI
from routers import words , validate

app = FastAPI()

app.include_router(words.router, prefix="/api")
app.include_router(validate.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Worddee API running"}