#!/usr/bin/env python

import sqlite3
from datetime import datetime
import os.path

class TemperatureLogger:
    def __init__(self, dbname = "temperature_data", path = "/home/david/data"):
        self.dbname = path + "/" + dbname + ".db"
        # if db does not exist, create
        if not os.path.exists(self.dbname):
            self.createDB()
        
    def createDB(self, dbname="temperature_data"):
        """Create a brand-new database and table for the data"""
        conn = sqlite3.connect(self.dbname)
        conn.execute("create table temperature (room_temperature,local_temperature,time)")
        conn.close()

    def log(self, room_temp, local_temp=None):
        """log temperature to sqlite3 database"""
        conn = sqlite3.connect(self.dbname)
        conn.execute(
                "insert into temperature Values (?,?,?)", 
                (room_temp,local_temp, datetime.now()))
        conn.commit()
        conn.close()
