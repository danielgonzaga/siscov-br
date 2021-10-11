from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pip._vendor.requests as req
from models import *
from utils import *

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
@cross_origin()
def findAllRegions():
    if request.method == 'GET':
        norte_json = getRegionData(1)
        nordeste_json = getRegionData(2)
        sudeste_json = getRegionData(3)
        sul_json = getRegionData(4)
        centro_oeste_json = getRegionData(5)
    return jsonify(centro_oeste_json, nordeste_json, norte_json, sudeste_json, sul_json)
    #return jsonify(norte_json, nordeste_json, sudeste_json, sul_json, centro_oeste_json)

@app.route('/region/<region_id>')
@cross_origin()
def findRegionById(region_id):
    if request.method == 'GET':
        region_json = getRegionData(region_id)
    return jsonify(region_json)

@app.route("/state")
@cross_origin()
def findAllStates():
    if request.method == 'GET':
        all_states = Estado.query.order_by(Estado.nome).all()
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

            population=getSpecificStatePopulation(state['id'])
            state['population']=population
            
            state['color']=colorCalculation(population, total_cases)
            
        return jsonify(result)

#specific state
@app.route("/state/<state_id>")
@cross_origin()
def findStateById(state_id):
    if request.method == 'GET':
        state_query = Estado.query.filter(Estado.id == state_id).first()
        state = state_schema.dump(state_query)

        state['isState']=True
        state['isRegion']=False
        state['isCounty']=False
        state['isSelected']=False
        state['id'] = state['id']

        # We need news table to set variant cases 
        state['variantCases']=False

        # Getting total cases per State
        total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter(Estado.nome==state['nome']).count()
        state['totalCases']=total_cases

        # Getting total deaths per State
        total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter(Estado.nome==state['nome']).filter(Casos.evolucaoCaso=='Óbito').count()
        state['totalDeaths']=total_deaths

        # state_id = getStateId(state['nome'])
        # if state_id != 0:
        population=0
        population=getSpecificStatePopulation(state['nome'])
        state['population']=population

        state['color']=colorCalculation(population, total_cases)
        
        return jsonify(state)

@app.route("/state/<state_name>/id")
@cross_origin()
def findStateByName(state_name):
    if request.method == 'GET':
        state_query = Estado.query.filter(Estado.nome == state_name).first()
        state = state_schema.dump(state_query)

        state['id'] = state['id']
        state['nome'] = state['nome']
        
        return jsonify(state)

@app.route("/state/<state_id>/county")
@cross_origin()
def findAllCounties(state_id):
    if request.method == 'GET':
        all_counties = Municipio.query.order_by(Municipio.nome).join(Estado, Municipio.estado_id == Estado.id).filter(Estado.id == state_id).all()
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
@cross_origin()
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

if __name__ == '__main__':
    app.run()
