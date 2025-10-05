import sys

import flask
import sqlite3
from flask import Flask, render_template
import mysql.connector




def get_db_connection():
    conn = mysql.connector.connect(
        user="raspberry",
        password="YjzRR10mDrNtho3n",
        host="scada71.ru",
        port=3306,
        database="pribor"

    )

    return conn


def close_db_connection(conn):
    conn.close()





query = """
        SELECT * FROM  signal_in  WHERE id_main=51
        """

app = Flask(__name__)
@app.route('/')
def index():
    conn=get_db_connection()
    mcursor=conn.cursor(buffered=True)
    mcursor.execute(query)
    upd_in_id  =  mcursor.lastrowid
    posts=mcursor.fetchall()
    
    conn.close()
    return render_template('index.html',posts=posts)

if __name__ == '__main__':
    app.run()