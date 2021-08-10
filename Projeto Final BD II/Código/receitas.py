import requests
import json	
from unidecode import unidecode

##ativos tangiveis
Url = "https://servicodados.ibge.gov.br/api/v3/agregados/1410/periodos/2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018/variaveis/863|642|643?localidades=N1[all]&classificacao=11070[all]"
receitas = requests.get(Url).json()

total = []
for i in range(50):
    total.append(receitas[0]['resultados'][i]['series'][0]['serie'])

deducao = []
for i in range(50):
    deducao.append(receitas[1]['resultados'][i]['series'][0]['serie'])

liquida = []
for i in range(50):
    liquida.append(receitas[2]['resultados'][i]['series'][0]['serie'])
print(liquida[2]['2010'])