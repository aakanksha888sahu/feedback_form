# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, request
from flask_cors import CORS
import snowflake.connector
app = Flask(__name__)
CORS(app)

def snowflake_connect(feedback_data):
    USER='aakanksha888'
    PASSWORD='Alyashanick123!'
    ACCOUNT='ow05112.ap-south-1.aws'
    WAREHOUSE='compute_wh'
    DATABASE='feedback'
    SCHEMA='public'
    conn = snowflake.connector.connect(
        user=USER,
        password=PASSWORD,
        account=ACCOUNT,
        warehouse=WAREHOUSE,
        database=DATABASE,
        schema=SCHEMA
    )
    ##print(conn.cursor().execute("select * from sample_feedback"))
    overall= feedback_data['overall']
    comp= feedback_data['comprehensiveness']
    query="insert into sample_feedback values ( '"+ overall+ '',''+comp+"')"
    print(query)
    try:
       conn.cursor().execute("insert into sample_feedback values ('abc', 'xyz')")
       ##conn.cursor().execute("select * from sample_feedback")
    finally:
        conn.close()


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
	return 'Hello World'

@app.route('/feedback',methods = ['POST'])
def feedback_form_data_ingestion():
        feedback_data=request.get_json()
        snowflake_connect(feedback_data)
        return ''


# main driver function
if __name__ == '__main__':
    app.run()
