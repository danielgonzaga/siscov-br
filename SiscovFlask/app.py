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

#get region
@app.route('/region/<region_id>')
def findRegion(region_id):
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

        jsonified_result = jsonify(result)
        return jsonify(result)


#testando pegar dado externo da api do ibge
#@app.route('/api/teste')
def getExternal():
    #Obtém a projecao da população para as localidades: Brasil (código BR ou 0), Grandes Regiões (códigos de 1 a 5) e Unidades da Federação (código numérico).
    #1 - Norte, 2 - Nordeste, 3 - Sudeste, 4 - Sul, 5 - Centro-Oeste
    #populacao do Norte do país
    result = req.get('https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/1')
    data = result.json()
    print(data)
    print(data.get('projecao').get('populacao'))
    return data

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

if __name__ == '__main__':
    app.run()
