from flask import Flask, render_template, request, jsonify
import pip._vendor.requests as req
from models import *
from sqlalchemy import func

# Routes
# /region -> traz todas as regioes
# /region/<region_id>  -> traz uma regiao em especifico
# /state -> traz todos os estados
# /state/<state_id> -> traz um estado em especifico
# /state/<state_id>/county -> traz todos os municipios de um estado em especifico
# /state/<state_id>/county/<county_id> -> traz um municipio em especifico de um estado em especifico

# Noticias:
# /region/<region_id>/news -> Traz as notícias de uma Região em específico
# /state/<state_id>/news -> Traz as notícias de um Estado em específico
# /state/<state_id>/county/<county_id>/news -> Traz as notícias de um Município em específico 

# Init schemas
state_schema = EstadoSchema()
states_schema = EstadoSchema(many=True)
region_schema = RegionSchema()
regions_schema = RegionSchema(many=True)

@app.route('/region')
def findAllRegions():
    if request.method == 'GET':
        norte_json = getRegionData(1)
        nordeste_json = getRegionData(2)
        sudeste_json = getRegionData(3)
        sul_json = getRegionData(4)
        centro_oeste_json = getRegionData(5)

    return jsonify(norte_json, nordeste_json, sudeste_json, sul_json, centro_oeste_json)

#get region by id
@app.route('/region/<region_id>')
def findRegionById(region_id):
    if request.method == 'GET':
        all_states = Estado.query.all()
        result = states_schema.dump(all_states)
        for state in result:
            state['isState']=False
            state['isRegion']=True
            state['isCounty']=False
            state['isSelected']=False

            # We need news table to set variant cases 
            state['variantCases']=False

            # Getting total cases per State
            total_cases = getRegionData(region_id)
            state['totalCases']=total_cases

            # Getting total deaths per State

        jsonified_result = jsonify(result)
        return jsonify(result)

@app.route("/state")
def findAllStates():
    if request.method == 'GET':
        all_states = Estado.query.all()
        result = states_schema.dump(all_states)
        for state in result:
            state['isState']=True
            state['isRegion']=False
            state['isCounty']=False
            state['isSelected']=False

            # We need news table to set variant cases 
            state['variantCases']=False
    
            # Getting total cases per State
            total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter(Estado.nome==state['nome']).count()
            state['totalCases']=total_cases

            # Getting total deaths per State
            total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter(Estado.nome==state['nome']).filter(Casos.evolucaoCaso=='Óbito').count()
            state['totalDeaths']=total_deaths

            state_id = getStateId(state['nome'])
            population=0
            if state_id != 0:
                population=getStatesPopulation(state_id)
            state['population']=population
            
            state['color']=colorCalculation(population, total_cases)
            
        jsonified_result = jsonify(result)
        return jsonify(result)

#specific state
@app.route("/state/<state_id>")
def findStateByName(state_id):
    result = Estado.query.filter(Estado.nome == state_id).first()
    return result

#all counties from state
@app.route("/state/<state_id>/county")
def findCounties(state_id):
    result = Municipio.query.join(Estado, Municipio.estado_id == Estado.id).filter(Estado.id == state_id).all()

    return result

#get specific county
@app.route("/state/<state_id>/county/<county_id>")
def findCountyByName(state_id, county_id):
    result = Municipio.query.join(Estado, Municipio.estado_id == Estado.id).filter(Estado.nome == state_id).filter(Municipio.nome == county_id).all()
    return result


def getStatesPopulation():
    population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).first()
    return population[0]

def getSpecificStatePopulation(state_id):
    population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).filter(Estado.id == state_id).first()

    return population[0]

def getRegionData(id):
    region_data = {}
    if id == 1:
        # Norte
        total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Acre") | (Estado.nome == "Amapa") | (Estado.nome == "Amazonas") | (Estado.nome == "Para") | (Estado.nome == "Rondonia") | (Estado.nome == "Roraima") | (Estado.nome == "Tocantins")).count()
        total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Acre") | (Estado.nome == "Amapa") | (Estado.nome == "Amazonas") | (Estado.nome == "Para") | (Estado.nome == "Rondonia") | (Estado.nome == "Roraima") | (Estado.nome == "Tocantins")).filter(Casos.evolucaoCaso=='Óbito').count()
        region_data["nome"]="Norte"
        region_data["totalCases"]=total_cases
        region_data["totalDeaths"]=total_deaths
    elif id == 2:
        # Nordeste
        total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Alagoas") | (Estado.nome == "Bahia") | (Estado.nome == "Ceara") | (Estado.nome == "Maranhao") | (Estado.nome == "Paraiba") | (Estado.nome == "Piaui") | (Estado.nome == "Pernambuco") | (Estado.nome == "Rio Grande do Norte") | (Estado.nome == "Sergipe")).count()
        total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Alagoas") | (Estado.nome == "Bahia") | (Estado.nome == "Ceara") | (Estado.nome == "Maranhao") | (Estado.nome == "Paraiba") | (Estado.nome == "Piaui") | (Estado.nome == "Pernambuco") | (Estado.nome == "Rio Grande do Norte") | (Estado.nome == "Sergipe")).filter(Casos.evolucaoCaso=='Óbito').count()
        region_data["nome"]="Nordeste"
        region_data["totalCases"]=total_cases
        region_data["totalDeaths"]=total_deaths
    elif id == 3:
        # Sudeste
        total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Espirito Santo") | (Estado.nome == "Minas Gerais") | (Estado.nome == "Rio de Janeiro") | (Estado.nome == "Sao Paulo")).count()
        total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Espirito Santo") | (Estado.nome == "Minas Gerais") | (Estado.nome == "Rio de Janeiro") | (Estado.nome == "Sao Paulo")).filter(Casos.evolucaoCaso=='Óbito').count()
        region_data["nome"]="Sudeste"
        region_data["totalCases"]=total_cases
        region_data["totalDeaths"]=total_deaths
    elif id == 4:
        # Sul
        total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Parana") | (Estado.nome == "Santa Catarina") | (Estado.nome == "Rio Grande do Sul")).count()
        total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Parana") | (Estado.nome == "Santa Catarina") | (Estado.nome == "Rio Grande do Sul")).filter(Casos.evolucaoCaso=='Óbito').count()
        region_data["nome"]="Sul"
        region_data["totalCases"]=total_cases
        region_data["totalDeaths"]=total_deaths
    elif id == 5:
        # Centro-Oeste
        total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Goias") | (Estado.nome == "Mato Grosso") | (Estado.nome == "Mato Grosso do Sul") | (Estado.nome == "Distrito Federal")).count()
        total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Parana") | (Estado.nome == "Santa Catarina") | (Estado.nome == "Rio Grande do Sul")).filter(Casos.evolucaoCaso=='Óbito').count()
        region_data["nome"]="Centro-Oeste"
        region_data["totalCases"]=total_cases
        region_data["totalDeaths"]=total_deaths
    
    region_data["isRegion"]=True
    region_data["isState"]=False
    region_data["isCounty"]=False
    region_data['isSelected']=False
    region_data['variantCases']=False
    return region_data

def getStateId(state_name):
    state_dict = {11: 'Rondonia', 12: 'Acre', 13: 'Amazonas', 14: 'Roraima', 15: 'Para', 16: 'Amapa', 17: 'Tocantins', 21: 'Maranhao', 22: 'Piaui', 23: 'Ceara', 24: 'Rio Grande do Norte', 25: 'Paraiba', 26: 'Pernambuco', 27: 'Alagoas', 28: 'Sergipe', 29: 'Bahia', 31: 'Minas Gerais', 32: 'Espirito Santo', 33: 'Rio de Janeiro', 35: 'Sao Paulo', 41: 'Parana', 42: 'Santa Catarina', 43: 'Rio Grande do Sul', 50: 'Mato Grosso do Sul', 51: 'Mato Grosso', 52: 'Goias', 53: 'Distrito Federal'}
    state_id = 0
    for key, value in state_dict.items():
        if value == state_name:
            state_id = key
    return state_id

def colorCalculation(population, total_cases):
    calculation = total_cases/population
    color = ''
    print("calculation: ", calculation)
    if calculation >= 0 and calculation < 0.35:
        color = 'blue'
    elif calculation >= 0.35 and calculation < 75:
        color = 'yellow'
    elif calculation >= 75:
        color = 'red'
    return color

if __name__ == '__main__':
    app.run()
