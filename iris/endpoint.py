from fastapi import FastAPI

app = FastAPI()

@app.post("/KNN")
async def KNN(arg1: float, arg2: float, arg3: float, arg4: float):
    result = arg1 + arg2 + arg3 + arg4
    return {"KNN_result": f"The sum of the four arguments is: {result}"}
