import requests
import json	
from unidecode import unidecode

##ativos tangiveis
Url = "https://servicodados.ibge.gov.br/api/v3/agregados/1411/periodos/2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018/variaveis/1443|504|1444|1445?localidades=N1[all]&classificacao=11070[all]"
compra = requests.get(Url).json()

##definindo total de compras
total = []
for i in range(50):
    total.append(compra[0]['resultados'][i]['series'][0]['serie'])

##definindo total de compras
revenda = []
for i in range(50):
    revenda.append(compra[1]['resultados'][i]['series'][0]['serie'])

##definindo total de compras
materiaPrima = []
for i in range(50):
    materiaPrima.append(compra[2]['resultados'][i]['series'][0]['serie'])

##definindo total de compras
materiaEmbalagem = []
for i in range(50):
    materiaEmbalagem.append(compra[3]['resultados'][i]['series'][0]['serie'])