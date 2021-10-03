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
        
        #transform nan county values
        if dataset['municipio'][row] != dataset['municipio'][row]:
            dataset['municipio'][row] = "Desconhecido"

        #estado
        stateName = (dataset['estado'][row])
        #insert if not exists an ocurrence
        stateExists = existState(cursor, stateName)

        if stateExists == False:
            cursor.execute("INSERT INTO estado(nome) VALUES (%s)", (stateName,))
        #cursor.execute("SELECT CURRVAL(pg_get_serial_sequence('estado', 'id'))")
        cursor.execute("SELECT id FROM estado WHERE nome = (%s)", (stateName,))
        idEstado = cursor.fetchone()[0]
        #print(idEstado)
        
        #municipio
        countyExists = existCounty(cursor, dataset['municipio'][row], idEstado)

        if countyExists == False:
            cursor.execute("INSERT INTO municipio(nome, idEstado) VALUES (%s, %s)", ((dataset['municipio'][row]), idEstado))
        #cursor.execute("SELECT CURRVAL(pg_get_serial_sequence('municipio', 'id'))")
        cursor.execute("SELECT municipio.id FROM municipio JOIN estado ON municipio.idestado = estado.id WHERE municipio.nome = (%s) AND estado.id = (%s)", ((dataset['municipio'][row]), idEstado))
        print("TESTE ", idEstado)
        print("TESTE ",dataset['municipio'][row])
        idMun = cursor.fetchone()[0]
        print(idMun)

        #casos
        caseExist = existCase(cursor, dataset['id'][row])
        #insert only if not exists
        if caseExist == False:
            cursor.execute(
                "INSERT INTO casos VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING", (dataset['id'][row], dataset['dataNotificacao'][row], dataset['dataInicioSintomas'][row], dataset['idade'][row], dataset['condicoes'][row], dataset['evolucaoCaso'][row], dataset['classificacaoFinal'][row], idMun)
            )
        
        print(row)

    conn.commit()

def defineType(df):
    df[["idade"]] = df[["idade"]].apply(pd.to_numeric)
    return df 

def existState(cursor, columnName):
    cursor.execute("SELECT count(id) FROM estado WHERE nome = (%s)", (columnName,))
    count = cursor.fetchone()[0]
    print("state : ", count)
    if count == 0:
        return False
    else:
        return True

def existCounty(cursor, columnName, idEstado):
    cursor.execute("SELECT count(municipio.id) FROM municipio JOIN estado ON municipio.idestado = estado.id WHERE municipio.nome = (%s) AND estado.id = (%s)", (columnName,idEstado))
    count = cursor.fetchone()[0]
    print("county : ", count)
    if count == 0:
        return False
    else:
        return True

def existCase(cursor, id):
    cursor.execute("SELECT count(id) FROM casos WHERE id = (%s)", (id,))
    count = cursor.fetchone()[0]
    print("county : ", count)
    if count == 0:
        return False
    else:
        return True

if __name__ == '__main__':
    dbVar = connect_to_db("casos_covid")
    connection = dbVar[0]
    cursor = dbVar[1]

    for key,value in urls.items():
        tp = pd.read_csv('./datasets/'+ key + '.csv', skiprows=1, names=col_names, encoding="UTF-8", sep='\t', engine='python', chunksize=10000, iterator=True)

        df = pd.concat(tp)
        df = defineType(df)
        print(df.dtypes)
        print("Inserting: ", key)
        insertIntoTable(connection, cursor, df, 'Casos', 'Estado', 'Municipio')
        print(key, " sucessfully inserted!!")
