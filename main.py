from fastapi import FastAPI
import subprocess


app = FastAPI()
robot_process = None

@app.get("/start_robot")
async def start_robot():
    global robot_process
    if robot_process is None or robot_process.poll() is not None:
        robot_process = subprocess.Popen(["python", "robot.py", "run"])
        return {"message": "Robot starts", "pid": robot_process.pid}
    else:
        return {"message": "Robot is already start"}

@app.get("/stop_robot")
async def stop_robot():
    global robot_process
    if robot_process is not None and robot_process.poll() is None:
        robot_process.terminate()
        return {"message": "Robot stop"}
    else:
        return {"message": "Robot is not start"}
