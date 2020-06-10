import datetime as dt
import numpy as np
import pandas as pd 
import sqlalchemy 
from sqlalchemy import create_engine 

class SQLHelper():

    def __init__(self):
        self.connection_string = "sqlite:///Resources/hawaii.sqlite"
        self.engine = create_engine(self.connection_string)

    def getPrcp(self):
        query_date = f"""
                SELECT
                    date,
                    sum(prcp) as total_precipitation
                FROM
                    measurement
                GROUP BY
                    date
                ORDER BY
                    date ASC;

        """

        conn = self.engine.connect()
        df = pd.read_sql(query_date, conn)
        conn.close()

        return df

    def getstations(self):
        query_station = f"""
                SELECT
                    station as station_Id,
                    name as station_Name,
                    latitude,
                    longitude,
                    elevation          
                FROM
                    station
                ORDER BY
                    Station_Id ASC;    

        """

        conn = self.engine.connect()
        df = pd.read_sql(query_station, conn)
        conn.close()

        return df

    def gettemp(self):

        query_temp = f"""
                SELECT
                    station,
                    date,
                    tobs as temperature                
                FROM
                    measurement
                WHERE
                    station = 'USC00519281' AND
                    date > '2016-08-23'
                ORDER BY
                    date ASC;

        """

        conn = self.engine.connect()
        df = pd.read_sql(query_temp, conn)
        conn.close()

        return df

    def getStartDate(self, date):
        query_start = f"""
                SELECT 
                    date,
                    min(tobs) as min_temp,
                    max(tobs) as max_temp,
                    avg(tobs) as avg_temp
                FROM
                    measurement
                WHERE
                    date = '{date}'
        """


        conn = self.engine.connect()
        df = pd.read_sql(query_start, conn)
        conn.close()

        return df

    def getDateRange(self, start, end):
        query_range = f"""
                SELECT 
                    min(tobs) as min_temp,
                    max(tobs) as max_temp,
                    avg(tobs) as avg_temp
                FROM
                    measurement
                WHERE
                    date >= '{start}' 
                    AND date < '{end}'
        """


        conn = self.engine.connect()
        df = pd.read_sql(query_range, conn)
        conn.close()

        return df