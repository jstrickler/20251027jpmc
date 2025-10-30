from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/zombie")
async def zombie():
    return {"diet": "BRAINSSSSSSS"}