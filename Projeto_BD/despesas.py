import requests
import json	
from unidecode import unidecode

##ativos tangiveis
Url = "https://servicodados.ibge.gov.br/api/v3/agregados/1401/periodos/2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018/variaveis/1402|1403|1404|1405|1001406|1407?localidades=N1[all]&classificacao=11070[all]"
despesas = requests.get(Url).json()

##definindo aluguel de despesas
aluguel = []
for i in range(50):
    aluguel.append(despesas[0]['resultados'][i]['series'][0]['serie'])

##definindo terceiro de despesas
terceiro = []
for i in range(50):
    terceiro.append(despesas[1]['resultados'][i]['series'][0]['serie'])

##definindo comunicacao de despesas
comunicacao = []
for i in range(50):
    comunicacao.append(despesas[2]['resultados'][i]['series'][0]['serie'])

##definindo agua, energia e esgoto de despesas
aguaEnergiaEsgoto = []
for i in range(50):
    aguaEnergiaEsgoto.append(despesas[3]['resultados'][i]['series'][0]['serie'])

##definindo imposto de despesas
imposto = []
for i in range(50):
    imposto.append(despesas[4]['resultados'][i]['series'][0]['serie'])

##definindo outras de despesas
outras = []
for i in range(50):
    outras.append(despesas[5]['resultados'][i]['series'][0]['serie'])