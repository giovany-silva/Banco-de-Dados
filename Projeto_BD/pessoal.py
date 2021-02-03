import requests
import json	
from unidecode import unidecode

Url = "https://servicodados.ibge.gov.br/api/v3/agregados/1417/periodos/2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018/variaveis/310|631?localidades=N1[all]&classificacao=11070[all]"
pessoal = requests.get(Url).json()

numEmpresas = []
for i in range(50):
    numEmpresas.append(pessoal[0]['resultados'][i]['series'][0]['serie'])

pessoalOcupado = []
for i in range(50):
    pessoalOcupado.append(pessoal[1]['resultados'][i]['series'][0]['serie'])