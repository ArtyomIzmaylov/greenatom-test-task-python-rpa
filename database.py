import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('robot_runs.db')
        print(f'successful connection with sqlite version {sqlite3.version}')
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        sql_create_table = """ CREATE TABLE IF NOT EXISTS runs (
                                        id integer PRIMARY KEY,
                                        start_number integer NOT NULL,
                                        start_time text NOT NULL,
                                        duration integer NOT NULL
                                    ); """
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)

def insert_run(conn, start_number, start_time, duration):
    sql = ''' INSERT INTO runs(start_number,start_time,duration)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, (start_number, start_time, duration))
    return cur.lastrowid


def update_duration(conn, run_id, duration):
    sql = ''' UPDATE runs
              SET duration = ?
              WHERE id = ? '''
    cur = conn.cursor()
    cur.execute(sql, (duration, run_id))
    conn.commit()