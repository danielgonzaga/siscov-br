import pandas as pd
from csvUrls import urls
from createDatabase import connect_to_db
import numpy as np

col_names = ['id', 'dataNotificacao', 'dataInicioSintomas', 'condicoes', 'estado', 'municipio', 'idade', 'evolucaoCaso', 'classificacaoFinal']

def insertIntoTable(conn, cursor, dataset, tableCasos, tableEstado, tableMunicipio):
    for row in dataset.index:
        #transform NaN age values
        if np.isnan(dataset['idade'][row]):
            dataset['idade'][row] = 0
        
        stateName = (dataset['estado'][row])
        #estado
        cursor.execute("INSERT INTO estado(nome) VALUES (%s) ON CONFLICT DO NOTHING", (stateName,))
        cursor.execute("SELECT CURRVAL(pg_get_serial_sequence('estado', 'id'))")
        idEstado = cursor.fetchone()
        
        #municipio
        cursor.execute("INSERT INTO municipio(nome, idEstado) VALUES (%s, %s) ON CONFLICT DO NOTHING", ((dataset['municipio'][row]), idEstado))
        cursor.execute("SELECT CURRVAL(pg_get_serial_sequence('municipio', 'id'))")
        idMun = cursor.fetchone()

        #casos
        cursor.execute(
            "INSERT INTO casos VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING", (dataset['id'][row], dataset['dataNotificacao'][row], dataset['dataInicioSintomas'][row], dataset['idade'][row], dataset['condicoes'][row], dataset['evolucaoCaso'][row], dataset['classificacaoFinal'][row], idMun)
        )
        
        print(row)

    conn.commit()

def defineTypes(df):
    df[["idade"]] = df[["idade"]].apply(pd.to_numeric)

    return df 

if __name__ == '__main__':
    dbVar = connect_to_db("casos_covid")
    connection = dbVar[0]
    cursor = dbVar[1]


    for key,value in urls.items():
        tp = pd.read_csv('./datasets/'+ key + '.csv', skiprows=1, names=col_names, encoding="UTF-8", sep='\t', engine='python', chunksize=10000, iterator=True)

        df = pd.concat(tp)
        df = defineTypes(df)
        print("Inserting: ", key)
        insertIntoTable(connection, cursor, df, 'Casos', 'Estado', 'Municipio')
        print(key, " sucessfully inserted!!")
        
