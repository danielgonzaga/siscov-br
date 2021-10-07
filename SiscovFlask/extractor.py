import pandas as pd
from csvUrls import urls

col_names = ['id', 'dataNotificacao', 'dataInicioSintomas', 'dataNascimento', 'sintomas', 'profissionalSaude', 'cbo', 'condicoes', 'estadoTeste', 'dataTeste', 'tipoTeste', 'resultadoTeste', 'paisOrigem', 'sexo', 'estado', 'estadoIBGE', 'municipio', 'municipioIBGE', 'origem', 'estadoNotificacao', 'estadoNotificacaoIBGE', 'municipioNotificacao', 'municipioNotificacaoIBGE', 'excluido', 'validado', 'idade', 'dataEncerramento', 'evolucaoCaso', 'classificacaoFinal']
 

def download_csv(url):
    csv_header = pd.read_csv(url, index_col=0, nrows=0, encoding="ISO-8859-1", sep=';', engine='python')
    new_header = ['id']
    for item in csv_header.items():
        new_header.append(item[0])
    tp = pd.read_csv(url, skiprows=1, names=new_header, usecols=['id', 'dataNotificacao', 'dataInicioSintomas', 'estado', 'municipio', 'idade', 'condicoes', 'evolucaoCaso', 'classificacaoFinal'], encoding="ISO-8859-1", sep=';', engine='python', chunksize=10000, iterator=True)
    df = pd.concat(tp)
    return df


if __name__ == '__main__':
    for key,value in urls.items():
        print(key, ':', value)
        for k, v in value.items():
            dataset = download_csv(v)
            dataset.to_csv('./datasets/' + k + ".csv", sep='\t', index=False)
            print("Download Completed!")
    