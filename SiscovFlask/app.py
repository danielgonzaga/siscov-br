from flask import Flask, render_template, request, jsonify
import pip._vendor.requests as req
from models import *

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

@app.route('/region')
def findNational():
    all_states = Estado.query.all()
    result = states_schema.dump(all_states)

    total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).count()

    return jsonify(result)

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
            total_cases = getRegionsStates(region_id)
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
    result = Municipio.query.join(Estado, Municipio.estado_id == Estado.id).filter(Estado.nome == state_id).all()

    return result

#get specific county
@app.route("/state/<state_id>/county/<county_id>")
def findCountyByName(state_id, county_id):
    result = Municipio.query.join(Estado, Municipio.estado_id == Estado.id).filter(Estado.nome == state_id).filter(Municipio.nome == county_id).all()
    
    return result

#testando pegar dado externo da api do ibge
#@app.route('/api/teste')
def getStatesPopulation(state_id):
    #Obtém a projecao da população para as localidades: Brasil (código BR ou 0), Grandes Regiões (códigos de 1 a 5) e Unidades da Federação (código numérico).
    #1 - Norte, 2 - Nordeste, 3 - Sudeste, 4 - Sul, 5 - Centro-Oeste
    #populacao do Norte do país
    result = req.get('https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/{}'.format(state_id))
    data = result.json()
    return data.get('projecao').get('populacao')

def getRegionsStates(id):
    #TO DO: replicar pras demais regioes 
    if id == 1:
        #amazonas, roraima, amapa, para, tocantins, rondonia, acre
        print('norte')
        region_total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "Amazonas") | (Estado.nome == "Roraima") | (Estado.nome == "Amapa") | (Estado.nome == "Tocantins") | (Estado.nome == "Acre")).count()
        return region_total_cases
    elif id == 2:
        #maranhao, piaui, ceara, rio grande do norte, pernambuco, paraiba, sergipe, alagoas, bahia
        print('nordeste')
    elif id == 3:
        #sao paulo, rio de janeiro, minas gerais, espirito santo
        print("sudeste")
    elif id == 4:
        #rio grande do sul, parana, santa catarina
        print("sul")
    elif id == 5:
        #goias, mato grosso, mato grosso do sul
        print("centro-oeste")

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
