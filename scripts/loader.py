import pandas as pd
from csvUrls import urls
from createDatabase import connect_to_db
import numpy as np

def insertIntoTable(conn, cursor, dataset, tableCasos, tableEstado, tableMunicipio):
    for row in dataset.index:
        #transform NaN age values
        if np.isnan(dataset['idade'][row]):
            dataset['idade'][row] = 0
        
        #estado
        cursor.execute("INSERT INTO " + tableEstado + " (nome) VALUES (%s)", (dataset['estado'][row]))
        cursor.execute("SELECT id FROM Estado  WHERE nome='(%s)'", (dataset['estado'][row]))
        idEstado = cursor.fetchone()
        
        #municipio
        cursor.execute("INSERT INTO " + tableMunicipio + " (nome, idEstado) VALUES (%s, %s)", (dataset['municipio'][row]), idEstado)
        cursor.execute("SELECT id FROM Municipio  WHERE nome='($s)'", (dataset['municipio'][row]))
        idMun = cursor.fetchone()

        #casos
        cursor.execute(
            "INSERT INTO " + tableCasos + " VALUES (%s, %s, %s, %s, %s, %s, %s)", (dataset['id'][row], dataset['dataNotificacao'][row], dataset['dataInicioSintomas'][row], dataset['idade'][row], dataset['condicoes'][row], dataset['evolucaoCaso'][row], dataset['classificacaoFinal'][row], idMun)
        )

    conn.commit()

if __name__ == '__main__':
    dbVar = connect_to_db(None)
    connection = dbVar[0]
    cursor = dbVar[1]


    for key,value in urls.items():
        print(key, ':', value)
        tp = pd.read_csv('./'+ key + '.csv', skiprows=1, usecols=['id', 'dataNotificacao', 'dataInicioSintomas', 'estado', 'municipio', 'idade', 'condicoes', 'evolucaoCaso', 'classificacaoFinal'], encoding="ISO-8859-1", sep='\t', engine='python', chunksize=10000, iterator=True)

        df = pd.concat(tp)

        insertIntoTable(connection, cursor, df, 'Casos', 'Estado', 'Municipio')
        