from fastapi import FastAPI

app = FastAPI()

@app.get("/Hello")
def Hello():
    return {
        "message": "Hello Dhruv!"
    }

@app.get("/Goodbye")
def goodbye():
    return{
        "Message" : "Goodbye Dhruv!"
    }