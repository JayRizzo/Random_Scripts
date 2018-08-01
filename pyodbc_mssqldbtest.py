#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Jeromie Kirchoff
# Created Date: Mon July 31 22:32:00 PDT 2018
# FILENAME: db.py
# =============================================================================
"""The Module Has Been Build for Interaction with MSSQL DBs To Test the con."""
# =============================================================================
# Answer to an SO question: https://stackoverflow.com/q/42433408/1896134

import pyodbc


def runningwithqueries(query):
    """The Module Has Been Build to {Open, Run & Close} query connection."""
    print("\nRunning Query: " + str(query) + "\nResult:\n")
    crsr = cnxn.execute(query)
    for row in crsr.fetchall():
        print(row[0])
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

"""
To RUN
python3 ~/your/path/here/db.py

OUTPUT SHOULD LOOK LIKE:


Your Connection String:
# DRIVER={ODBC Driver 17 for SQL Server};SERVER=yourservername;UID=yourusername;PWD=yourforgottencomplicatedpassword;DSN=MSSQL-PYTHON;DATABASE=yourdatabase;

SELECT * FROM INFORMATION_SCHEMA.COLUMNS;

Running Query: SELECT @@VERSION;
Result:

Microsoft SQL Server 2017 (RTM-CU3-GDR) (KB4052987) - 14.0.3015.40 (X64)
    Dec 22 2017 16:13:22
    Copyright (C) 2017 Microsoft Corporation
    Express Edition (64-bit) on Windows Server 2012 R2 Standard 6.3 <X64> (Build 9600: ) (Hypervisor)


Running Query: SELECT * FROM sys.schemas;
Result:

dbo
guest
INFORMATION_SCHEMA
sys
db_owner
db_accessadmin
db_securityadmin
db_ddladmin
db_backupoperator
db_datareader
db_datawriter
db_denydatareader
db_denydatawriter

Running Query: SELECT * FROM INFORMATION_SCHEMA.TABLES;
Result:


Running Query: SELECT * FROM INFORMATION_SCHEMA.COLUMNS;
Result:


Running Query: SELECT * FROM INFORMATION_SCHEMA.CHECK_CONSTRAINTS;
Result:


Running Query: EXEC sp_databases;
Result:

master
msdb
rdsadmin
tempdb
TestDB

Running Query: EXEC sp_who2 'active';
Result:

1..49
94

"""

