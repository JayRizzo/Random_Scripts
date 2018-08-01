#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Jeromie Kirchoff
# Created Date: Mon July 31 22:32:00 PDT 2018
# FILENAME: db.py
# =============================================================================
"""The Module Has Been Build for Interaction with MSSQL DBs To Test the con."""
# =============================================================================
# Thanks to this post for headers https://stackoverflow.com/q/12704305/1896134
# Answer to an SO question: https://stackoverflow.com/q/42433408/1896134

import pyodbc


def runningwithqueries(query):
    """The Module Has Been Build to {Open, Run & Close} query connection."""
    print("\nRunning Query: " + str(query) + "\nResult :\n")
    crsr = cnxn.execute(query)
    columns = [column[0] for column in crsr.description]
    print(columns)
    for row in crsr.fetchall():
        print(row)
    crsr.close()

# set variables needed for server connection
server = 'yourusername'
username = 'yourusername'
password = 'yourforgottencomplicatedpassword'
database = 'yourdatabase'

connStr = (r'DRIVER={ODBC Driver 17 for SQL Server};' +
           # r"Integrated Security=true;" +
           r'SERVER=' + server +
           r';UID=' + username +
           r';PWD=' + password +
           r';DSN=MSSQL-PYTHON' +
           r';DATABASE=' + database + ';'
           )

print("Your Connection String:\n" + str(connStr) + "\n\n")

# CONNECT TO THE DB
cnxn = pyodbc.connect(connStr, autocommit=True)

# SET QUERIES TO VARIABLES
SQLQUERY1 = ("SELECT @@VERSION;")
SQLQUERY2 = ("SELECT * FROM sys.schemas;")
SQLQUERY3 = ("SELECT * FROM INFORMATION_SCHEMA.TABLES;")
SQLQUERY4 = ("SELECT * FROM INFORMATION_SCHEMA.COLUMNS;")
SQLQUERY5 = ("SELECT * FROM INFORMATION_SCHEMA.CHECK_CONSTRAINTS;")
SQLQUERY6 = ("EXEC sp_databases;")
SQLQUERY7 = ("EXEC sp_who2 'active';")
# SQLQUERY8 = ("EXEC sp_monitor;") # DENIED FOR AWS RDS


print(SQLQUERY4)
# RUN QUERIES
# YOU CAN RUN AS MANY QUERIES AS LONG AS THE CONNECTION IS OPEN TO THE DB
runningwithqueries(SQLQUERY1)
runningwithqueries(SQLQUERY2)
runningwithqueries(SQLQUERY3)
runningwithqueries(SQLQUERY4)
runningwithqueries(SQLQUERY5)
runningwithqueries(SQLQUERY6)
runningwithqueries(SQLQUERY7)
# runningwithqueries(SQLQUERY8)

# CLOSE THE CONNECTION TO THE DB
cnxn.close()
