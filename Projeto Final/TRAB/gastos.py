import requests
import json	
from unidecode import unidecode


Url = "https://servicodados.ibge.gov.br/api/v3/agregados/1414/periodos/2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018/variaveis/314|1411|1502?localidades=N1[all]&classificacao=11070[all]"
gastos = requests.get(Url).json()

salario = []
for i in range(50):
    salario.append(gastos[0]['resultados'][i]['series'][0]['serie'])

fgts = []
for i in range(50):
    fgts.append(gastos[1]['resultados'][i]['series'][0]['serie'])

indenizacao = []
for i in range(50):
    indenizacao.append(gastos[2]['resultados'][i]['series'][0]['serie'])
