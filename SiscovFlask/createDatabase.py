import pandas as pd
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def connect_to_db(databaseName):
    if databaseName:
        conn = psycopg2.connect(user="postgres",
                                password="siscov",
                                host="localhost",
                                port="5432",
                                database=databaseName 
                                )
    else:
        conn = psycopg2.connect(user="postgres",
                                password="siscov",
                                host="localhost",
                                port="5432")

    cursor = conn.cursor()
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
    
    return conn, cursor

def create_db(conn, cursor, databaseName):
    print(databaseName)
    cursor.execute("CREATE DATABASE {};".format(databaseName))

    
if __name__ == '__main__':
    #connecting to postgres
    dbVar = connect_to_db(None)
    connection = dbVar[0]
    cursor = dbVar[1]

    #creating database if not already exists
    create_db(connection, cursor, "casos_covid")


