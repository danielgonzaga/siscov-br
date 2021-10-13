from models import *
from sqlalchemy import func
from linkpreview import link_preview

state_schema = EstadoSchema()
states_schema = EstadoSchema(many=True)
region_schema = RegionSchema()
regions_schema = RegionSchema(many=True)
county_schema = CountySchema()
counties_schema = CountySchema(many=True)
news_schema = NoticiasSchema()

def getStateUFId(state_name):
    state_dict = {11: 'RONDÔNIA', 12: 'ACRE', 13: 'AMAZONAS', 14: 'RORAIMA', 15: 'PARÁ', 16: 'AMAPÁ', 17: 'TOCANTINS', 21: 'MARANHÃO', 22: 'PIAUÍ', 23: 'CEARÁ', 24: 'RIO GRANDE DO NORTE', 25: 'PARAÍBA', 26: 'PERNAMBUCO', 27: 'ALAGOAS', 28: 'SERGIPE', 29: 'BAHIA', 31: 'MINAS GERAIS', 32: 'ESPÍRITO SANTO', 33: 'RIO DE JANEIRO', 35: 'SÃO PAULO', 41: 'PARANÁ', 42: 'SANTA CATARINA', 43: 'RIO GRANDE DO SUL', 50: 'MATO GROSSO DO SUL', 51: 'MATO GROSSO', 52: 'GOIÁS', 53: 'DISTRITO FEDERAL'}
    state_id = 0
    for key, value in state_dict.items():
        if value == state_name:
            state_id = key
    return state_id

def getStateNameUsingUF(state_uf):
    state_dict = {11: 'RONDÔNIA', 12: 'ACRE', 13: 'AMAZONAS', 14: 'RORAIMA', 15: 'PARÁ', 16: 'AMAPÁ', 17: 'TOCANTINS', 21: 'MARANHÃO', 22: 'PIAUÍ', 23: 'CEARÁ', 24: 'RIO GRANDE DO NORTE', 25: 'PARAÍBA', 26: 'PERNAMBUCO', 27: 'ALAGOAS', 28: 'SERGIPE', 29: 'BAHIA', 31: 'MINAS GERAIS', 32: 'ESPÍRITO SANTO', 33: 'RIO DE JANEIRO', 35: 'SÃO PAULO', 41: 'PARANÁ', 42: 'SANTA CATARINA', 43: 'RIO GRANDE DO SUL', 50: 'MATO GROSSO DO SUL', 51: 'MATO GROSSO', 52: 'GOIÁS', 53: 'DISTRITO FEDERAL'}
    state_name = ''
    for key, value in state_dict.items():
        if key == state_uf:
            state_name = value
    return state_name

def getStatesPopulation():
    population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).first()
    if population:
        return population[0]
    else: 
        return 0

def getSpecificStatePopulation(state_id):
    population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).filter(Estado.id == state_id).first()
    if population:
        return population[0]
    else: 
        return 0

def getSpecificCountyPopulation(county_id):
    population = Municipio.query.with_entities(Municipio.populacao).filter(Municipio.id == county_id).first()
    if population:
        return population[0]
    else: 
        return 0

def getSpecificRegionPopulation(region_id):
    if region_id == 1:
        population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).filter((Estado.nome == "ACRE") | (Estado.nome == "AMAPÁ") | (Estado.nome == "AMAZONAS") | (Estado.nome == "PARÁ") | (Estado.nome == "RONDÔNIA") | (Estado.nome == "RORAIMA") | (Estado.nome == "TOCANTINS")).first()
    if region_id == 2:
        population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).filter((Estado.nome == "ALAGOAS") | (Estado.nome == "BAHIA") | (Estado.nome == "CEARÁ") | (Estado.nome == "MARANHÃO") | (Estado.nome == "PARAÍBA") | (Estado.nome == "PIAUÍ") | (Estado.nome == "PERNAMBUCO") | (Estado.nome == "RIO GRANDE DO NORTE") | (Estado.nome == "SERGIPE")).first()
    if region_id == 3:
        population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).filter((Estado.nome == "ESPÍRITO SANTO") | (Estado.nome == "MINAS GERAIS") | (Estado.nome == "RIO DE JANEIRO") | (Estado.nome == "SÃO PAULO")).first()
    if region_id == 4:
        population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).filter((Estado.nome == "PARANÁ") | (Estado.nome == "SANTA CATARINA") | (Estado.nome == "RIO GRANDE DO SUL")).first()
    if region_id == 5:
        population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).filter((Estado.nome == "GOIÁS") | (Estado.nome == "MATO GROSSO") | (Estado.nome == "MATO GROSSO DO SUL") | (Estado.nome == "DISTRITO FEDERAL")).first()
    return population[0]

def consultRegions():
    norte_json = getRegionData(1)
    nordeste_json = getRegionData(2)
    sudeste_json = getRegionData(3)
    sul_json = getRegionData(4)
    centro_oeste_json = getRegionData(5)

    result = (centro_oeste_json, nordeste_json, norte_json, sudeste_json, sul_json)

    return result

def consultStates(query):
    result = states_schema.dump(query)

    for state in result:
        state['isState']=True
        state['isRegion']=False
        state['isCounty']=False
        state['isSelected']=False
    
        # We need news table to set variant cases 
        state['variantCases']=getStateVariantAlert(state['id'])

        # Getting total cases per State
        total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter(Estado.nome==state['nome']).count()
        state['totalCases']=total_cases

        # Getting total deaths per State
        total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter(Estado.nome==state['nome']).filter(Casos.evolucaoCaso=='Óbito').count()
        state['totalDeaths']=total_deaths

        population=getSpecificStatePopulation(state['id'])
        state['population']=population
        
        state['color']=colorCalculation(population, total_cases)

    return result

def consultCounties(query):
    result = counties_schema.dump(query)

    for county in result:
        county['isState']=False
        county['isRegion']=False
        county['isCounty']=True
        county['isSelected']=False
        county['variantCases']=getCountyVariantAlert(county['id'])

        total_cases = Municipio.query.join(Casos, Municipio.id == Casos.municipio_id).filter(Municipio.id==county['id']).count()
        county['totalCases']=total_cases

        total_deaths = Municipio.query.join(Casos, Municipio.id == Casos.municipio_id).filter(Municipio.id==county['id']).filter(Casos.evolucaoCaso=='Óbito').count()
        county['totalDeaths']=total_deaths

        population = getSpecificCountyPopulation(county['id'])
        county['population']=population
        
        county['color']=colorCalculation(population, total_cases)
    
    return result

def getRegionData(id):
    region_id = int(id)
    region_data = {}
    if region_id == 1:
        # Norte
        total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "ACRE") | (Estado.nome == "AMAPÁ") | (Estado.nome == "AMAZONAS") | (Estado.nome == "PARÁ") | (Estado.nome == "RONDÔNIA") | (Estado.nome == "RORAIMA") | (Estado.nome == "TOCANTINS")).count()
        total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "ACRE") | (Estado.nome == "AMAPÁ") | (Estado.nome == "AMAZONAS") | (Estado.nome == "PARÁ") | (Estado.nome == "RONDÔNIA") | (Estado.nome == "RORAIMA") | (Estado.nome == "TOCANTINS")).filter(Casos.evolucaoCaso=='Óbito').count()
        population=getSpecificRegionPopulation(1)
        region_data["nome"]="Norte"
        region_data["totalCases"]=total_cases
        region_data["totalDeaths"]=total_deaths
        region_data["population"]=population
        region_data["color"]=colorCalculation(population, total_cases)
        #print("region_data: ", region_data)
    elif region_id == 2:
        # Nordeste
        total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "ALAGOAS") | (Estado.nome == "BAHIA") | (Estado.nome == "CEARÁ") | (Estado.nome == "MARANHÃO") | (Estado.nome == "PARAÍBA") | (Estado.nome == "PIAUÍ") | (Estado.nome == "PERNAMBUCO") | (Estado.nome == "RIO GRANDE DO NORTE") | (Estado.nome == "SERGIPE")).count()
        total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "ALAGOAS") | (Estado.nome == "BAHIA") | (Estado.nome == "CEARÁ") | (Estado.nome == "MARANHÃO") | (Estado.nome == "PARAÍBA") | (Estado.nome == "PIAUÍ") | (Estado.nome == "PERNAMBUCO") | (Estado.nome == "RIO GRANDE DO NORTE") | (Estado.nome == "SERGIPE")).filter(Casos.evolucaoCaso=='Óbito').count()
        population=getSpecificRegionPopulation(2)
        region_data["nome"]="Nordeste"
        region_data["totalCases"]=total_cases
        region_data["totalDeaths"]=total_deaths
        region_data["population"]=population
        region_data["color"]=colorCalculation(population, total_cases)
    elif region_id == 3:
        # Sudeste
        total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "ESPÍRITO SANTO") | (Estado.nome == "MINAS GERAIS") | (Estado.nome == "RIO DE JANEIRO") | (Estado.nome == "SÃO PAULO")).count()
        total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "ESPÍRITO SANTO") | (Estado.nome == "MINAS GERAIS") | (Estado.nome == "RIO DE JANEIRO") | (Estado.nome == "SÃO PAULO")).filter(Casos.evolucaoCaso=='Óbito').count()
        population=getSpecificRegionPopulation(3)
        region_data["nome"]="Sudeste"
        region_data["totalCases"]=total_cases
        region_data["totalDeaths"]=total_deaths
        region_data["population"]=population
        region_data["color"]=colorCalculation(population, total_cases)
    elif region_id == 4:
        # Sul
        total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "PARANÁ") | (Estado.nome == "SANTA CATARINA") | (Estado.nome == "RIO GRANDE DO SUL")).count()
        total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "PARANÁ") | (Estado.nome == "SANTA CATARINA") | (Estado.nome == "RIO GRANDE DO SUL")).filter(Casos.evolucaoCaso=='Óbito').count()
        population=getSpecificRegionPopulation(4)
        region_data["nome"]="Sul"
        region_data["totalCases"]=total_cases
        region_data["totalDeaths"]=total_deaths
        region_data["population"]=population
        region_data["color"]=colorCalculation(population, total_cases)
    elif region_id == 5:
        # Centro-Oeste
        total_cases = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "GOIÁS") | (Estado.nome == "MATO GROSSO") | (Estado.nome == "MATO GROSSO DO SUL") | (Estado.nome == "DISTRITO FEDERAL")).count()
        total_deaths = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).join(Casos, Casos.municipio_id == Municipio.id).filter((Estado.nome == "GOIÁS") | (Estado.nome == "MATO GROSSO") | (Estado.nome == "MATO GROSSO DO SUL") | (Estado.nome == "DISTRITO FEDERAL")).filter(Casos.evolucaoCaso=='Óbito').count()
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
    region_data['variantCases']=getRegionAlert(region_id)
    return region_data

def getNewsFromRegion(id):
    region_id = int(id)
    #region_data = {}
    if region_id == 1:
        # Norte
        news_query = Noticias.query.join(noticias_estado, noticias_estado.c.noticia_id == Noticias.id).join(Estado, noticias_estado.c.estado_id == Estado.id).filter((Estado.id == 11) | (Estado.id == 12) | (Estado.id == 13) | (Estado.id == 14) | (Estado.id == 15) | (Estado.id == 16) | (Estado.id == 17)).all()
        
        
    elif region_id == 2:
        # Nordeste
        news_query = Noticias.query.join(noticias_estado, noticias_estado.c.noticia_id == Noticias.id).join(Estado, noticias_estado.c.estado_id == Estado.id).filter((Estado.id == 21) | (Estado.id == 22) | (Estado.id == 23) | (Estado.id == 24) | (Estado.id == 25) | (Estado.id == 26) | (Estado.id == 27) | (Estado.id == 28) | (Estado.id == 29)).all()

    elif region_id == 3:
        # Sudeste
        news_query = Noticias.query.join(noticias_estado, noticias_estado.c.noticia_id == Noticias.id).join(Estado, noticias_estado.c.estado_id == Estado.id).filter((Estado.id == 31) | (Estado.id == 32) | (Estado.id == 33) | (Estado.id == 35)).all()

    elif region_id == 4:
        # Sul
        news_query = Noticias.query.join(noticias_estado, noticias_estado.c.noticia_id == Noticias.id).join(Estado, noticias_estado.c.estado_id == Estado.id).filter((Estado.id == 41) | (Estado.id == 42) | (Estado.id == 43)).all()

    elif region_id == 5:
        # Centro-Oeste
        news_query = Noticias.query.join(noticias_estado, noticias_estado.c.noticia_id == Noticias.id).join(Estado, noticias_estado.c.estado_id == Estado.id).filter((Estado.id == 50) | (Estado.id == 51) | (Estado.id == 52) | (Estado.id == 53)).all()

    return news_query

def formatNews(result):
    for news in result:
        try:
            meta_url = link_preview(news['url'])

            news['title'] = meta_url.title
            news['description'] = meta_url.description
            news['image'] =  meta_url.image
            news['force_title'] = meta_url.force_title
            news['absolute_image'] = meta_url.absolute_image
        except: 
            print('Unable to get metadata from url')
    return result

def getRegionAlert(region_id):
    if region_id == 1:
        # Norte
        has_variant_cases = Noticias.query.join(noticias_estado, noticias_estado.c.noticia_id == Noticias.id).join(Estado, noticias_estado.c.estado_id == Estado.id).filter((Estado.nome == "ACRE") | (Estado.nome == "AMAPÁ") | (Estado.nome == "AMAZONAS") | (Estado.nome == "PARÁ") | (Estado.nome == "RONDÔNIA") | (Estado.nome == "RORAIMA") | (Estado.nome == "TOCANTINS")).first()
    elif region_id == 2:
        # Nordeste
        has_variant_cases = Noticias.query.join(noticias_estado, noticias_estado.c.noticia_id == Noticias.id).join(Estado, noticias_estado.c.estado_id == Estado.id).filter((Estado.nome == "ALAGOAS") | (Estado.nome == "BAHIA") | (Estado.nome == "CEARÁ") | (Estado.nome == "MARANHÃO") | (Estado.nome == "PARAÍBA") | (Estado.nome == "PIAUÍ") | (Estado.nome == "PERNAMBUCO") | (Estado.nome == "RIO GRANDE DO NORTE") | (Estado.nome == "SERGIPE")).first()
    elif region_id == 3:
        # Sudeste
        has_variant_cases = Noticias.query.join(noticias_estado, noticias_estado.c.noticia_id == Noticias.id).join(Estado, noticias_estado.c.estado_id == Estado.id).filter((Estado.nome == "ESPÍRITO SANTO") | (Estado.nome == "MINAS GERAIS") | (Estado.nome == "RIO DE JANEIRO") | (Estado.nome == "SÃO PAULO")).first()
      
    elif region_id == 4:
        # Sul
        has_variant_cases = Noticias.query.join(noticias_estado, noticias_estado.c.noticia_id == Noticias.id).join(Estado, noticias_estado.c.estado_id == Estado.id).filter((Estado.nome == "PARANÁ") | (Estado.nome == "SANTA CATARINA") | (Estado.nome == "RIO GRANDE DO SUL")).first()
    elif region_id == 5:
        # Centro-Oeste
        has_variant_cases = Noticias.query.join(noticias_estado, noticias_estado.c.noticia_id == Noticias.id).join(Estado, noticias_estado.c.estado_id == Estado.id).filter((Estado.nome == "GOIÁS") | (Estado.nome == "MATO GROSSO") | (Estado.nome == "MATO GROSSO DO SUL") | (Estado.nome == "DISTRITO FEDERAL")).first()
    
    if has_variant_cases:
        return True
    return False 

def getStateVariantAlert(state_id):
    has_variant_cases = Noticias.query.join(noticias_estado, noticias_estado.c.noticia_id == Noticias.id).join(Estado, noticias_estado.c.estado_id == Estado.id).filter(Estado.id == state_id).first()

    if has_variant_cases:
        return True
    return False 

def getCountyVariantAlert(county_id):
    has_variant_cases = Noticias.query.join(noticias_municipio, noticias_municipio.c.noticia_id == Noticias.id).join(Municipio, noticias_municipio.c.municipio_id == Municipio.id).filter(Municipio.id == county_id).first()

    if has_variant_cases:
        return True
    return False

def colorCalculation(population, total_cases):
    if population:
        calculation = total_cases * (100000)/population
    else:
        calculation = 0
    color = ''
    if calculation >= 0 and calculation < 6000:
        # Blue
        color = '#0377fc'
    elif calculation >= 6000 and calculation < 12000:
        # Yellow
        color = '#F6C146'
    elif calculation >= 12000:
        # Red
        color = '#cf4040'
    return color