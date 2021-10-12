from flask import request, jsonify
from flask_cors import cross_origin
from models import *
from utils import *
import json, os.path

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
news_schema = NoticiasSchema(many=True)

@app.route('/region')
@cross_origin()
def findAllRegions():
    if request.method == 'GET':
        cache_file = './json/{}.json'.format("regions")
        cache_exists = os.path.exists(cache_file)
        
        if cache_exists:
            with open(cache_file, 'r', encoding='utf-8') as json_file:
                result = json.load(json_file)
        else:
            result = consultRegions()
            with open(cache_file, 'w', encoding='utf8') as json_file:
                json.dump(result, json_file, ensure_ascii=False)

    return jsonify(result)


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
        cache_file = './json/{}.json'.format("states")
        cache_exists = os.path.exists(cache_file)

        if cache_exists:
            with open(cache_file, 'r', encoding='utf-8') as json_file:
                result = json.load(json_file)
        else:
            all_states = Estado.query.order_by(Estado.nome).all()
            result = consultStates(all_states)
            with open(cache_file, 'w', encoding='utf8') as json_file:
                json.dump(result, json_file, ensure_ascii=False)

        return jsonify(result)

@app.route("/state/<state_id>")
@cross_origin()
def findStateById(state_id):
    if request.method == 'GET':
        state_query = Estado.query.filter(Estado.id == state_id).first()
        state = consultStates(state_query)
        
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
        cache_file = './json/{}.json'.format(state_id)
        cache_exists = os.path.exists(cache_file)

        if cache_exists:
            with open(cache_file, 'r', encoding='utf-8') as json_file:
                result = json.load(json_file)
        else:
            all_counties = Municipio.query.order_by(Municipio.nome).join(Estado, Municipio.estado_id == Estado.id).filter(Estado.id == state_id).all()
            result = consultCounties(all_counties)
           
            with open(cache_file, 'w', encoding='utf8') as json_file:
                json.dump(result, json_file, ensure_ascii=False)

        return jsonify(result)

@app.route("/state/<state_id>/county/<county_id>")
@cross_origin()
def findCountyById(state_id, county_id):
    if request.method == 'GET':
        county_query = Municipio.query.join(Estado, Municipio.estado_id == Estado.id).filter(Estado.id == state_id).filter(Municipio.id == county_id).first()
        county = consultCounties(county_query)

        return jsonify(county)

@app.route('/region/<region_id>/news')
@cross_origin()
def getRegionNews(region_id):
    if request.method == 'GET':
        news_query = getRegionNews(region_id)
        result = news_schema.dump(news_query)
      
        result = formatNews(result)
            
        return jsonify(result)

@app.route("/state/<state_id>/news")
@cross_origin()
def getStateNews(state_id):
    if request.method == 'GET':
        news_query = Noticias.query.join(noticias_estado, noticias_estado.c.noticia_id == Noticias.id).join(Estado, noticias_estado.c.estado_id == Estado.id).filter(Estado.id == state_id).all()

        result = news_schema.dump(news_query)
    
        result = formatNews(result)
           
        return jsonify(result)

@app.route("/state/<state_id>/county/<county_id>/news")
@cross_origin()
def getCountyNews(state_id, county_id):
    if request.method == 'GET':
        news_query = Noticias.query.join(noticias_municipio, noticias_municipio.c.noticia_id == Noticias.id).join(Municipio, noticias_municipio.c.municipio_id == Municipio.id).join(Estado, Municipio.estado_id == Estado.id).filter(Estado.id == state_id).filter(Municipio.id == county_id).all()
        result = news_schema.dump(news_query)
        
        result = formatNews(result)
           
        return jsonify(result)

if __name__ == '__main__':
    app.run()
