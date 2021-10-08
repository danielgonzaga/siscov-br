from flask import Flask, render_template, request, jsonify
import pip._vendor.requests as req
from models import *
from sqlalchemy import func

# Routes
# (OK) /region -> traz todas as regioes
# (OK) /region/<region_id>  -> traz uma regiao em especifico
# (OK) /state -> traz todos os estados
# (OK) /state/<state_id> -> traz um estado em especifico
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
county_schema = CountySchema()
counties_schema = CountySchema(many=True)

@app.route('/region')
def findAllRegions():
    if request.method == 'GET':
        norte_json = getRegionData(1)
        nordeste_json = getRegionData(2)
        sudeste_json = getRegionData(3)
        sul_json = getRegionData(4)
        centro_oeste_json = getRegionData(5)

    return jsonify(norte_json, nordeste_json, sudeste_json, sul_json, centro_oeste_json)

@app.route('/region/<region_id>')
def findRegionById(region_id):
    if request.method == 'GET':
        region_json = getRegionData(region_id)
    return jsonify(region_json)

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
                population=getSpecificStatePopulation(state_id)
            state['population']=population
            
            state['color']=colorCalculation(population, total_cases)
            
        return jsonify(result)

#specific state
@app.route("/state/<state_id>")
def findStateById(state_id):
    if request.method == 'GET':
        state_query = Estado.query.filter(Estado.id == state_id).first()
        state = state_schema.dump(state_query)

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
            population=getSpecificStatePopulation(state_id)
        state['population']=population

        state['color']=colorCalculation(population, total_cases)
        
        return jsonify(state)

@app.route("/state/<state_id>/county")
def findAllCounties(state_id):
    if request.method == 'GET':
        all_counties = Municipio.query.join(Estado, Municipio.estado_id == Estado.id).filter(Estado.id == state_id).all()
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
        return jsonify(result)

@app.route("/state/<state_id>/county/<county_id>")
def findCountyById(state_id, county_id):
    if request.method == 'GET':
        county_query = Municipio.query.join(Estado, Municipio.estado_id == Estado.id).filter(Estado.id == state_id).filter(Municipio.id == county_id).first()
        county = county_schema.dump(county_query)
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
        return jsonify(county)

def getStatesPopulation():
    population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).first()
    return population[0]

def getSpecificStatePopulation(state_id):
    population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).filter(Estado.id == state_id).first()
    return population[0]

def getSpecificCountyPopulation(county_id):
    population = Municipio.query.with_entities(Municipio.populacao).filter(Municipio.id == county_id)
    return population[0][0]

def getSpecificRegionPopulation(region_id):
    if region_id == 1:
        population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).filter((Estado.nome == "Acre") | (Estado.nome == "Amapa") | (Estado.nome == "Amazonas") | (Estado.nome == "Para") | (Estado.nome == "Rondonia") | (Estado.nome == "Roraima") | (Estado.nome == "Tocantins")).first()
    if region_id == 2:
        population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).filter((Estado.nome == "Alagoas") | (Estado.nome == "Bahia") | (Estado.nome == "Ceara") | (Estado.nome == "Maranhao") | (Estado.nome == "Paraiba") | (Estado.nome == "Piaui") | (Estado.nome == "Pernambuco") | (Estado.nome == "Rio Grande do Norte") | (Estado.nome == "Sergipe")).first()
    if region_id == 3:
        population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).filter((Estado.nome == "Espirito Santo") | (Estado.nome == "Minas Gerais") | (Estado.nome == "Rio de Janeiro") | (Estado.nome == "Sao Paulo")).first()
    if region_id == 4:
        population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).filter((Estado.nome == "Parana") | (Estado.nome == "Santa Catarina") | (Estado.nome == "Rio Grande do Sul")).first()
    if region_id == 5:
        population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).filter((Estado.nome == "Goias") | (Estado.nome == "Mato Grosso") | (Estado.nome == "Mato Grosso do Sul") | (Estado.nome == "Distrito Federal")).first()
    return population[0]



def getRegionData(id):
    region_id = int(id)
    region_data = {}
    if region_id == 1:
        # Norte
        total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Acre") | (Estado.nome == "Amapa") | (Estado.nome == "Amazonas") | (Estado.nome == "Para") | (Estado.nome == "Rondonia") | (Estado.nome == "Roraima") | (Estado.nome == "Tocantins")).count()
        total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Acre") | (Estado.nome == "Amapa") | (Estado.nome == "Amazonas") | (Estado.nome == "Para") | (Estado.nome == "Rondonia") | (Estado.nome == "Roraima") | (Estado.nome == "Tocantins")).filter(Casos.evolucaoCaso=='Óbito').count()
        population=getSpecificRegionPopulation(1)
        region_data["nome"]="Norte"
        region_data["totalCases"]=total_cases
        region_data["totalDeaths"]=total_deaths
        region_data["population"]=population
        region_data["color"]=colorCalculation(population, total_cases)
        print("region_data: ", region_data)
    elif region_id == 2:
        # Nordeste
        total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Alagoas") | (Estado.nome == "Bahia") | (Estado.nome == "Ceara") | (Estado.nome == "Maranhao") | (Estado.nome == "Paraiba") | (Estado.nome == "Piaui") | (Estado.nome == "Pernambuco") | (Estado.nome == "Rio Grande do Norte") | (Estado.nome == "Sergipe")).count()
        total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Alagoas") | (Estado.nome == "Bahia") | (Estado.nome == "Ceara") | (Estado.nome == "Maranhao") | (Estado.nome == "Paraiba") | (Estado.nome == "Piaui") | (Estado.nome == "Pernambuco") | (Estado.nome == "Rio Grande do Norte") | (Estado.nome == "Sergipe")).filter(Casos.evolucaoCaso=='Óbito').count()
        population=getSpecificRegionPopulation(2)
        region_data["nome"]="Nordeste"
        region_data["totalCases"]=total_cases
        region_data["totalDeaths"]=total_deaths
        region_data["population"]=population
        region_data["color"]=colorCalculation(population, total_cases)
    elif region_id == 3:
        # Sudeste
        total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Espirito Santo") | (Estado.nome == "Minas Gerais") | (Estado.nome == "Rio de Janeiro") | (Estado.nome == "Sao Paulo")).count()
        total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Espirito Santo") | (Estado.nome == "Minas Gerais") | (Estado.nome == "Rio de Janeiro") | (Estado.nome == "Sao Paulo")).filter(Casos.evolucaoCaso=='Óbito').count()
        population=getSpecificRegionPopulation(3)
        region_data["nome"]="Sudeste"
        region_data["totalCases"]=total_cases
        region_data["totalDeaths"]=total_deaths
        region_data["population"]=population
        region_data["color"]=colorCalculation(population, total_cases)
    elif region_id == 4:
        # Sul
        total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Parana") | (Estado.nome == "Santa Catarina") | (Estado.nome == "Rio Grande do Sul")).count()
        total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Parana") | (Estado.nome == "Santa Catarina") | (Estado.nome == "Rio Grande do Sul")).filter(Casos.evolucaoCaso=='Óbito').count()
        population=getSpecificRegionPopulation(4)
        region_data["nome"]="Sul"
        region_data["totalCases"]=total_cases
        region_data["totalDeaths"]=total_deaths
        region_data["population"]=population
        region_data["color"]=colorCalculation(population, total_cases)
    elif region_id == 5:
        # Centro-Oeste
        total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Goias") | (Estado.nome == "Mato Grosso") | (Estado.nome == "Mato Grosso do Sul") | (Estado.nome == "Distrito Federal")).count()
        total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Parana") | (Estado.nome == "Santa Catarina") | (Estado.nome == "Rio Grande do Sul")).filter(Casos.evolucaoCaso=='Óbito').count()
        population=getSpecificRegionPopulation(5)
        region_data["nome"]="Centro-Oeste"
        region_data["totalCases"]=total_cases
        region_data["totalDeaths"]=total_deaths
        region_data["population"]=population
        region_data["color"]=colorCalculation(population, total_cases)
    
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
    if population:
        calculation = total_cases/population
    else:
        calculation = 0
    color = ''
    if calculation >= 0 and calculation < 0.35:
        color = 'blue'
    elif calculation >= 0.35 and calculation < 75:
        color = 'yellow'
    elif calculation >= 75:
        color = 'red'
    return color

if __name__ == '__main__':
    app.run()
