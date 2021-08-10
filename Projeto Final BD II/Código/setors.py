import requests
import json	
from unidecode import unidecode

##ativos tangiveis
Url = "https://servicodados.ibge.gov.br/api/v3/agregados/1415/periodos/2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018/variaveis/1517|1518?localidades=N1[all]&classificacao=11070[all]"
ativos = requests.get(Url).json()

setor = []
##definindo todos os setores
i=0
for i in range(50):
    setor.append(unidecode(str(list(ativos[0]['resultados'][i]['classificacoes'][0]['categoria'].values()))))
