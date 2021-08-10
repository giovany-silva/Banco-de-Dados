import requests
import json	
from unidecode import unidecode

Url = "https://servicodados.ibge.gov.br/api/v3/agregados/1411/periodos/2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018/variaveis/1449|1500|1450|1451?localidades=N1[all]&classificacao=11070[all]"
estoque = requests.get(Url).json()

total = []
for i in range(50):
    total.append(estoque[0]['resultados'][i]['series'][0]['serie'])

produtos = []
for i in range(50):
    produtos.append(estoque[1]['resultados'][i]['series'][0]['serie'])

materiaPrima = []
for i in range(50):
    materiaPrima.append(estoque[2]['resultados'][i]['series'][0]['serie'])

materiaEmbalagem = []
for i in range(50):
    materiaEmbalagem.append(estoque[3]['resultados'][i]['series'][0]['serie'])