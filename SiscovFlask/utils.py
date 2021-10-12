from models import Estado, Municipio, Casos, Noticias, noticias_estado, noticias_municipio
from sqlalchemy import func

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
        print("region_data: ", region_data)
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
    region_data['variantCases']=False
    return region_data

def getRegionNews(id):
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

def colorCalculation(population, total_cases):
    if population:
        calculation = total_cases/population
    else:
        calculation = 0
    color = ''
    if calculation >= 0 and calculation < 0.35:
        # Blue
        color = '#0377fc'
    elif calculation >= 0.35 and calculation < 75:
        # Yellow
        color = '#dce650'
    elif calculation >= 75:
        # Red
        color = '#cf4040'
    return color