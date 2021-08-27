import pandas as pd
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import math

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


def create_table(cursor):
    regions = ("casos_sudeste", "casos_nordeste", "casos_norte", "casos_sul", "casos_centro_oeste")

    for table in regions:
        cursor.execute('''
            CREATE TABLE {}
            (
                id VARCHAR(255) UNIQUE NOT NULL,
                "dataNotificacao" VARCHAR(255) NOT NULL,
                "dataInicioSintomas" VARCHAR(255),
                estado VARCHAR(50) NOT NULL,
                municipio VARCHAR(255),
                idade integer,
                condicoes VARCHAR(255),
                "evolucaoCaso" VARCHAR(255),
                "classificacaoFinal" VARCHAR(255),
                PRIMARY KEY (id)
            );
        '''.format(table))
    
if __name__ == '__main__':
    #connecting to postgres
    dbVar = connect_to_db("casos_covid")
    connection = dbVar[0]
    cursor = dbVar[1]

    #creating database if not already exists
    #create_db(connection, cursor, "casos_covid")

    #create tables
    create_table(cursor)

