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

if __name__ == '__main__':
    
    for key,value in urls.items():
        print(key, ':', value)
        dataset = download_csv(value)
        print("Download Completed!")
        dataset.to_csv('./datasets/' + key + ".csv", sep='\t', index=False)
  
    
