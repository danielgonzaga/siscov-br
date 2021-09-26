import pandas as pd
from createDatabase import connect_to_db

def create_table(cursor):
    tables = ("Casos", "Municipio", "Estado")
    
    #Estado
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS {}
            (
                id SERIAL NOT NULL,
                nome VARCHAR(50) NOT NULL,
                PRIMARY KEY (id)
            );
            '''.format(tables[2]))
    
    #Municipio
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS {}
            (
                id SERIAL NOT NULL,
                nome VARCHAR(50) NOT NULL,
                idEstado integer REFERENCES Estado(id),
                PRIMARY KEY (id)
            );
            '''.format(tables[1]))

    #Casos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS {}
        (
            id VARCHAR(255) UNIQUE NOT NULL,
            "dataNotificacao" VARCHAR(255) NOT NULL,
            "dataInicioSintomas" VARCHAR(255),
            idade integer,
            condicoes VARCHAR(255),
            "evolucaoCaso" VARCHAR(255),
            "classificacaoFinal" VARCHAR(255),
            idMunicipio integer REFERENCES Municipio(id),
            PRIMARY KEY (id)
        );
    '''.format(tables[0]))

    

if __name__ == '__main__':
    #connecting to database
    dbVar = connect_to_db("casos_covid")
    #connection = dbVar[0]
    cursor = dbVar[1]

    #create tables
    create_table(cursor)