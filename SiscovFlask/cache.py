from models import db, Estado, EstadoSchema, Municipio, CountySchema, Casos
from utils import getSpecificCountyPopulation, colorCalculation
import json

state_schema = EstadoSchema()
states_schema = EstadoSchema(many=True)
county_schema = CountySchema()
counties_schema = CountySchema(many=True)

def getAllStateIds():
    all_states = Estado.query.with_entities(Estado.id).order_by(Estado.id).all()
    states_id = states_schema.dump(all_states)
    #result = []
    #for state in states_id:
    #    print(state['id'])
    #print(type(result))
    #print(result)
    return states_id

def cacheStateCounties():
    states_id = getAllStateIds()

    for state in states_id:
        state_uf = state['id']
        cache_file = './json/{}.json'.format(state_uf)
        all_counties = Municipio.query.order_by(Municipio.nome).join(Estado, Municipio.estado_id == Estado.id).filter(Estado.id == state_uf).all()
        result = counties_schema.dump(all_counties)
            
        for county in result:
            county['isState']=False
            county['isRegion']=False
            county['isCounty']=True
            county['isSelected']=False
            county['variantCases']=False

            total_cases = Municipio.query.join(Casos, Municipio.id == Casos.municipio_id).filter(Municipio.id==county['id']).count()
            county['totalCases']=total_cases

            total_deaths = Municipio.query.join(Casos, Municipio.id == Casos.municipio_id).filter(Municipio.id==county['id']).filter(Casos.evolucaoCaso=='Óbito').count()
            county['totalDeaths']=total_deaths

            population = getSpecificCountyPopulation(county['id'])
            county['population']=population
            
            county['color']=colorCalculation(population, total_cases)

            with open(cache_file, 'w', encoding='utf8') as json_file:
                json.dump(result, json_file, ensure_ascii=False)

        print('Cached state {} sucessfully!'.format(state_uf))

if __name__ == '__main__':
    cacheStateCounties()