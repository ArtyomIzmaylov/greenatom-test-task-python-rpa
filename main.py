from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/start_robot")
async def start_robot():
    subprocess.Popen(["python", "robot.py"])
    return {"message": "Start Robot"}

@app.get("/stop_robot")
async def stop_robot():
    return {"message": "Stop Robot"}