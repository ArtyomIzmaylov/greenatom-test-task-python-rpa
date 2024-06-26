from fastapi import FastAPI
import subprocess
from database import create_connection, create_table, insert_run, update_duration
import datetime

app = FastAPI()
robot_process = None
global_conn = None
start_time = None
last_run_id = None

@app.on_event("startup")
async def startup_event():
    global global_conn
    global_conn = create_connection()
    create_table(global_conn)

@app.get("/start_robot/{start_number:int}")
async def start_robot(start_number: int = 0):
    global robot_process, start_time, last_run_id
    if robot_process is None or robot_process.poll() is not None:
        robot_process = subprocess.Popen(["python", "robot.py", "run", str(start_number)])
        start_time = datetime.datetime.now()
        duration = 0
        last_run_id = insert_run(global_conn, start_number, start_time.strftime("%Y-%m-%d %H:%M:%S"), duration)
        return {"message": "Robot starts", "pid": robot_process.pid, "start_number": start_number}
    else:
        return {"message": "Robot is already start"}

@app.get("/stop_robot")
async def stop_robot():
    global robot_process, start_time, last_run_id
    if robot_process is not None and robot_process.poll() is None:
        robot_process.terminate()
        duration = (datetime.datetime.now() - start_time).total_seconds()
        update_duration(global_conn, last_run_id, duration)
        return {"message": "Robot stop", "duration": duration}
    else:
        return {"message": "Robot is not start"}

@app.get("/runs")
async def get_runs():
    global global_conn
    cur = global_conn.cursor()
    cur.execute("SELECT * FROM runs")
    rows = cur.fetchall()
    runs = [{"id": row[0], "start_number": row[1], "start_time": row[2], "duration": row[3]} for row in rows]
    return {"runs": runs}
