from models import db, Estado, EstadoSchema, Municipio, CountySchema, Casos
from utils import consultStates, consultCounties, consultRegions
import json

states_schema = EstadoSchema(many=True)
counties_schema = CountySchema(many=True)

def getAllStateIds():
    all_states = Estado.query.with_entities(Estado.id).order_by(Estado.id).all()
    states_id = states_schema.dump(all_states)
    return states_id

def cacheRegions():
    cache_file = './json/{}.json'.format("regions")
    result = consultRegions()
    
    with open(cache_file, 'w', encoding='utf8') as json_file:
            json.dump(result, json_file, ensure_ascii=False)
    print('Cached all regions sucessfully!')

def cacheStates():
    cache_file = './json/{}.json'.format("states")
    all_states = Estado.query.order_by(Estado.nome).all()
    result = consultStates(all_states)
    
    with open(cache_file, 'w', encoding='utf8') as json_file:
            json.dump(result, json_file, ensure_ascii=False)
    print('Cached all states sucessfully!')

def cacheStateCounties():
    states_id = getAllStateIds()

    for state in states_id:
        state_uf = state['id']
        cache_file = './json/{}.json'.format(state_uf)
        all_counties = Municipio.query.order_by(Municipio.nome).join(Estado, Municipio.estado_id == Estado.id).filter(Estado.id == state_uf).all()
        result = consultCounties(all_counties)
            
        with open(cache_file, 'w', encoding='utf8') as json_file:
            json.dump(result, json_file, ensure_ascii=False)

        print('Cached state {} sucessfully!'.format(state_uf))

if __name__ == '__main__':
    cacheRegions()
    cacheStates()
    #cacheStateCounties()