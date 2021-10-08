import pandas as pd
from csvUrls import urls
import numpy as np
from models import Estado, Municipio, Casos, db
from utils import getStateUFId

col_names = ['id', 'dataNotificacao', 'dataInicioSintomas', 'condicoes', 'estado', 'municipio', 'idade', 'evolucaoCaso', 'classificacaoFinal']

counties_names = ['UF', 'nome', 'populacao']
counties_csv = pd.read_csv('./utils/PopulacaoMunicipios.csv', skiprows=1, encoding="UTF-8", names=counties_names, sep=';')

def insertIntoTable(dataset, state_name):
    # States
    existState(state_name)
    
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

        print("row:", row)
        
        # County
        state_id = getStateId(state_name)
        existCounty(county_name, state_id, state_name)

        # Casos
        county_id = getCountyId(county_name)
        exist_case = existCase(case_id)

        # Insert only if not exists and county_id is valid
        if exist_case == False and county_id != -1:
            insertCase(case_id, notification_date, symptoms_date, age, conditions, case_evolution, final_classification, county_id)
        
def existState(state_name):
    state = Estado.query.filter_by(nome=state_name).first()
    print("state query:", state)
    if not state:
        insertState(state_name)

def insertState(state_name):
    state_to_be_created = Estado(nome=state_name)
    db.session.add(state_to_be_created)
    db.session.commit()

def getStateId(state_name):
    return Estado.query.filter_by(nome=state_name).first().id


def existCounty(county_name, state_id, state_name):
    county = Municipio.query.join(Estado, Municipio.estado_id == Estado.id).filter(Municipio.nome==county_name).filter(Estado.id==state_id).first()
    if not county:
        population = getCountyPopulation(county_name, state_name)
        if population != 0:
            insertCounty(county_name, state_id, population)

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

def insertCounty(county_name, state_id, population):
    county_to_be_created = Municipio(nome=county_name,populacao=population,estado_id=state_id)
    db.session.add(county_to_be_created)
    db.session.commit()

def getCountyId(county_name):
    county =  Municipio.query.filter_by(nome=county_name).first()
    if county:
        return county.id
    else:
        return -1

def existCase(case_id):
    case = Casos.query.filter_by(id=case_id).first()
    if not case:
        return False
    else:
        return True

def insertCase(case_id, notification_date, symptoms_date, age, conditions, case_evolution, final_classification, county_id):
    case_to_be_created = Casos(id=case_id, dataNotificacao=notification_date, dataInicioSintomas=symptoms_date, idade=age, condicoes=conditions, evolucaoCaso=case_evolution, classificacaoFinal=final_classification, municipio_id=county_id)
    db.session.add(case_to_be_created)
    db.session.commit()

if __name__ == '__main__':
    for key,value in urls.items():
        for k, v in value.items():
            url = './datasets/'+ k + '.csv'
            csv_header = pd.read_csv(url, index_col=0, nrows=0, encoding="UTF-8", sep='\t', engine='python')
            new_header = ['id']
            for item in csv_header.items():
                new_header.append(item[0])
            tp = pd.read_csv(url, skiprows=1, names=new_header, encoding="UTF-8", sep='\t', engine='python', chunksize=10000, iterator=True)
            df = pd.concat(tp)
            print(df.dtypes)
            print("Inserting: ", key)
            insertIntoTable(df, key)
        print(key, "cases sucessfully updated!")
