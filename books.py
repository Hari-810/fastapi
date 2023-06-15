from fastapi import FastAPI

app = FastAPI()

@app.get("/api-endpoint") # creating a api endpoint using decorator
async def first_api():  # by default FastAPI take function as Asyncoronus here we giving explicitly
    return {"message" : "Hello World"}


#to view this api run the file and visit " 127.0.0.1:8000/api-endpoint "