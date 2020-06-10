import datetime as dt
import numpy as np
import pandas as pd  
import json
from sqlalchemy import create_engine 
from sqlHelper import SQLHelper
from flask import Flask, jsonify



#################################################
# Flask Setup
#################################################
app = Flask(__name__)

sqlHelper = SQLHelper()

#################################################
# Flask Routes
#################################################

@app.route("/")
def home(): 
    return (
        f"Welcome to Hawaii's Climate Analysis<br/> Click below to see available routes:<br/>"
       
        f"""
        <ul>
            <li><a target="_blank" href = '/api/v1.0/precipitation'>Prior year rain totals</></li>
            <li><a target="_blank" href = '/api/v1.0/stations'>Station Id and names</></li>
            <li><a target="_blank" href = '/api/v1.0/tobs'>Prior year temperatures for most active stations</></li>
            <li><a target="_blank" href = '/api/v1.0/temperature/2017-08-17'>Get temperature for date</></li>
            <li><a target="_blank" href = '/api/v1.0/temperature/2017-08-17/2017-08-26'>Get temperature for date range</></li>
        </ul>
        """
    )

@app.route("/api/v1.0/precipitation")
def prcp_page():
        prcp_data = sqlHelper.getPrcp()
        return(jsonify(json.loads(prcp_data.to_json(orient='records')))) 

@app.route("/api/v1.0/stations") 
def stations_page():
        station_data = sqlHelper.getstations()
        return(jsonify(json.loads(station_data.to_json(orient='records')))) 

@app.route("/api/v1.0/tobs") 
def tobs_page():
        temp_data = sqlHelper.gettemp()
        return(jsonify(json.loads(temp_data.to_json(orient='records')))) 

@app.route("/api/v1.0/temperature/<start>") 
def startDate_page(start):
        start_data = sqlHelper.getStartDate(start)
        return(jsonify(json.loads(start_data.to_json(orient='records')))) 
   
@app.route("/api/v1.0/temperature/<start>/<end>") 
def dateRange_page(start, end):
        range_data = sqlHelper.getDateRange(start, end)
        return(jsonify(json.loads(range_data.to_json(orient='records')))) 

if __name__ =="__main__":
        app.run(debug=True)