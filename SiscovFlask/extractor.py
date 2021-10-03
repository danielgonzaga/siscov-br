import pandas as pd
import psycopg2
import math
import numpy as np
from csvUrls import urls

col_names = ['id', 'dataNotificacao', 'dataInicioSintomas', 'dataNascimento', 'sintomas', 'profissionalSaude', 'cbo', 'condicoes', 'estadoTeste', 'dataTeste', 'tipoTeste', 'resultadoTeste', 'paisOrigem', 'sexo', 'estado', 'estadoIBGE', 'municipio', 'municipioIBGE', 'origem', 'estadoNotificacao', 'estadoNotificacaoIBGE', 'municipioNotificacao', 'municipioNotificacaoIBGE', 'excluido', 'validado', 'idade', 'dataEncerramento', 'evolucaoCaso', 'classificacaoFinal']

def download_csv(url):
    tp = pd.read_csv(url, skiprows=1, names=col_names, usecols=['id', 'dataNotificacao', 'dataInicioSintomas', 'estado', 'municipio', 'idade', 'condicoes', 'evolucaoCaso', 'classificacaoFinal'], encoding="ISO-8859-1", sep=';', engine='python', chunksize=10000, iterator=True)

    df = pd.concat(tp)

    return df
'''
def insertIntoTable(conn, cursor, dataset, table):
    for row in dataset.index:
        #transform NaN age values
        if np.isnan(dataset['idade'][row]):
            dataset['idade'][row] = 0
        cursor.execute(
            "INSERT INTO " + table + " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (dataset['id'][row], dataset['dataNotificacao'][row], dataset['dataInicioSintomas'][row], dataset['estado'][row], dataset['municipio'][row], dataset['idade'][row], dataset['condicoes'][row], dataset['evolucaoCaso'][row], dataset['classificacaoFinal'][row])
        )

    conn.commit()
'''
if __name__ == '__main__':
    
    for key,value in urls.items():
        print(key, ':', value)
        dataset = download_csv(value)
        print("Download Completed!")
        dataset.to_csv('./datasets/' + key + ".csv", sep='\t', index=False)
  
    #insert into table
    #insertIntoTable(dbConnection, dbCursor, dataset, "casos_norte")
    