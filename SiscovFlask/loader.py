import pandas as pd
from csvUrls import urls
import numpy as np
from models import Estado, Municipio, database_name, db
from utils import getStateUFId, getStateNameUsingUF
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

col_names = ['id', 'dataNotificacao', 'dataInicioSintomas', 'condicoes', 'estado', 'municipio', 'idade', 'evolucaoCaso', 'classificacaoFinal']

counties_names = ['UF', 'nome', 'populacao', 'codigoIBGE']
counties_csv = pd.read_csv('./utils/municipios_dados.csv', skiprows=1, encoding="UTF-8", names=counties_names, sep=';')

'''def insertIntoTable(dataset, state_name):
    # States
    #insertAllStatesAndCounties()
    print("Inserting {} cases...".format(state_name))
    for row in dataset.index:
        # Declare variables
        age = dataset['idade'][row]
        county_name = dataset['municipio'][row]
        case_id = dataset['id'][row]
        notification_date = dataset['dataNotificacao'][row]
        symptoms_date = dataset['dataInicioSintomas'][row]
        conditions = dataset['condicoes'][row]
        case_evolution = dataset['evolucaoCaso'][row]
        final_classification = dataset['classificacaoFinal'][row]
        
        # Transform NaN age values
        if np.isnan(age):
            age = 0
        
        # Transform NaN county values
        if county_name != county_name:
            county_name = "Desconhecido"

        if(row % 10000 == 0):
            print("row:", row)
        #print("row:", row)

        # Casos
        county_id = getCountyId(county_name)
        exist_case = existCase(case_id)

        # Insert only if not exists, county_id is valid and is a confirmed case
        if exist_case == False and county_id != -1 and final_classification=='Confirmado Laboratorial':
            insertCase(case_id, notification_date, symptoms_date, age, conditions, case_evolution, final_classification, county_id)
   '''     
def existState(state_name, state_uf):
    state = Estado.query.filter_by(id=state_uf).first()    
    if not state:
        insertState(state_name, state_uf)

def insertState(state_name, state_uf):
    state_to_be_created = Estado(id = state_uf, nome=state_name)
    db.session.add(state_to_be_created)
    db.session.commit()

def insertAllStatesAndCounties():
    for row in counties_csv.index:
        county = counties_csv['nome'][row]
        print(county)
        codIBGE = counties_csv['codigoIBGE'][row]
        state_uf = counties_csv['UF'][row].tolist()
        print(state_uf)
        state_name = getStateNameUsingUF(state_uf)
        print(state_name)

        existState(state_name, state_uf)
        existCounty(county, state_uf, state_name, codIBGE)

def getStateId(state_name):
    return Estado.query.filter_by(nome=state_name).first().id

def existCounty(county_name, state_id, state_name, codIBGE):
    county = Municipio.query.join(Estado, Municipio.estado_id == Estado.id).filter(Municipio.nome==county_name).filter(Estado.id==state_id).first()
    if not county:
        population = getCountyPopulation(county_name, state_name)
        if population != 0:
            insertCounty(county_name, state_id, population, codIBGE)

def getCountyPopulation(county_name, state_name):
    state_uf = getStateUFId(state_name)
    #filter rows which uf is equals state
    state_counties = counties_csv[counties_csv['UF'].astype(int) == state_uf]
    #get population from county 
    populationCounty = list(state_counties[state_counties['nome'] == county_name]['populacao'])
    
    #if is an existent county for that state, returns the population, otherwise returns 0
    if(populationCounty):
        return int(populationCounty[0])
    else:
        return 0

def insertCounty(county_name, state_id, population, codIBGE):
    codIBGE = "mun_"+str(codIBGE)
    county_to_be_created = Municipio(nome=county_name,populacao=population, codIBGE=codIBGE, estado_id=state_id)
    db.session.add(county_to_be_created)
    db.session.commit()

def getCountyId(county_name):
    county =  Municipio.query.filter_by(nome=county_name).first()
    if county:
        return county.id
    else:
        return -1

'''def existCase(case_id):
    case = Casos.query.filter_by(id=case_id).first()
    if not case:
        return False
    else:
        return True'''

'''def insertCase(case_id, notification_date, symptoms_date, age, conditions, case_evolution, final_classification, county_id):
    case_to_be_created = Casos(id=case_id, dataNotificacao=notification_date, dataInicioSintomas=symptoms_date, idade=age, condicoes=conditions, evolucaoCaso=case_evolution, classificacaoFinal=final_classification, municipio_id=county_id)
    db.session.add(case_to_be_created)
    db.session.commit()'''

def connect_to_db(databaseName):
    conn = psycopg2.connect(user="postgres",
                            password="siscov",
                            host="localhost",
                            port="5432",
                            database=databaseName 
                            )
    cursor = conn.cursor()
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
    
    return conn, cursor

if __name__ == '__main__':
    insertAllStatesAndCounties()
    #connecting to postgres
    dbVar = connect_to_db(database_name)
    conn = dbVar[0]
    cursor = dbVar[1]
    
    #create tmp table to copy the huge csv, this improve the insert speed
    tables = ("tmp")
    print("creating tmp table...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS {}
        (
            tmpId SERIAL NOT NULL,
            id VARCHAR(255) NOT NULL,
            "dataNotificacao" VARCHAR(255) NOT NULL,
            "dataInicioSintomas" VARCHAR(255),
            idade VARCHAR(20),
            condicoes VARCHAR(500),
            estado VARCHAR(255),
            municipio VARCHAR(500),
            "evolucaoCaso" VARCHAR(500),
            "classificacaoFinal" VARCHAR(255),
            PRIMARY KEY (tmpId)
        );
    '''.format(tables))

    for key,value in urls.items():

        for k, v in value.items():
            url = './datasets/'+ k + '.csv'
            
            with open(url, 'r', encoding='utf8') as f:
                next(f)    
                cmd = 'COPY tmp(id, "dataNotificacao", "dataInicioSintomas", condicoes, estado, municipio, idade, "evolucaoCaso", "classificacaoFinal") FROM STDIN WITH (FORMAT CSV, HEADER TRUE)'
                cursor.copy_from(f, 'tmp', columns=col_names, sep='\t')
                conn.commit()
            print("Copying: ", key)
        print("Inserting",key,"cases...")

        cursor.execute('''
                    INSERT INTO casos(id, "dataNotificacao", "dataInicioSintomas", idade, condicoes, "evolucaoCaso", 
                            "classificacaoFinal", municipio_id)
                        SELECT tmp.id, tmp."dataNotificacao", tmp."dataInicioSintomas", tmp.idade, tmp.condicoes, tmp."evolucaoCaso",
                        tmp."classificacaoFinal", municipio.id FROM tmp 
                        JOIN  municipio on tmp.municipio = municipio.nome 
                        JOIN estado on UPPER(estado.nome) = UPPER(tmp.estado)
                        WHERE tmp."classificacaoFinal"='Confirmado Laboratorial' 
                        AND tmp.estado='{}' OR tmp.estado='{}'
                        ON CONFLICT DO NOTHING;
                '''.format(key, key.upper()))

        print(key, "cases sucessfully updated!")
    print("removing tmp table")
    cursor.execute('DROP TABLE tmp')

