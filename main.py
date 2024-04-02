from fastapi import FastAPI
import subprocess
import sys

app = FastAPI()
robot_process = None

@app.get("/start_robot/{start_number:int}")
async def start_robot(start_number: int = 0):
    global robot_process
    if robot_process is None or robot_process.poll() is not None:
        robot_process = subprocess.Popen(["python", "robot.py", "run", str(start_number)])
        return {"message": "Robot starts", "pid": robot_process.pid, "start_number": start_number}
    else:
        return {"message": "Robot is already start"}


@app.get("/stop_robot")
async def stop_robot():
    global robot_process
    if robot_process is not None and robot_process.poll() is None:
        robot_process.terminate()
        return {"message": "Robot stop"}
    else:
        return {"message": "Robot is npt start"}

