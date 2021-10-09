from models import Estado, Municipio, Casos
from sqlalchemy import func

def getStateUFId(state_name):
    state_dict = {11: 'Rondonia', 12: 'Acre', 13: 'Amazonas', 14: 'Roraima', 15: 'Para', 16: 'Amapa', 17: 'Tocantins', 21: 'Maranhao', 22: 'Piaui', 23: 'Ceara', 24: 'Rio Grande do Norte', 25: 'Paraiba', 26: 'Pernambuco', 27: 'Alagoas', 28: 'Sergipe', 29: 'Bahia', 31: 'Minas Gerais', 32: 'Espirito Santo', 33: 'Rio de Janeiro', 35: 'Sao Paulo', 41: 'Parana', 42: 'Santa Catarina', 43: 'Rio Grande do Sul', 50: 'Mato Grosso do Sul', 51: 'Mato Grosso', 52: 'Goias', 53: 'Distrito Federal'}
    state_id = 0
    for key, value in state_dict.items():
        if value == state_name:
            state_id = key
    return state_id

def getStatesPopulation():
    population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).first()
    if population:
        return population[0]
    else: 
        return 0

def getSpecificStatePopulation(state_name):
    population = Estado.query.join(Municipio, Municipio.estado_id == Estado.id).with_entities(func.sum(Municipio.populacao)).filter(Estado.nome == state_name).first()
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