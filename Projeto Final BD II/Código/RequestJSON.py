import requests
import json
from unidecode import unidecode
# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

##ativos tangiveis
Url = "https://servicodados.ibge.gov.br/api/v3/agregados/1415/periodos/2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018/variaveis/1517|1518?localidades=N1[all]&classificacao=11070[all]"
ativos = requests.get(Url).json()

setor = []
anos = []
##definindo todos os setores
i=0
for i in range(50):
   setor.append(unidecode(str(list(ativos[0]['resultados'][i]['classificacoes'][0]['categoria'].values()))))


i = 2007
##definindo todos os anos
while(i <= 2018):
    anos.append(i)
    i=i+1

##definindo aquisicao de ativos
aquisicao = []
for i in range(50):
    aquisicao.append(ativos[0]['resultados'][i]['series'][0]['serie'])
    #print(aquisicao[i])

#definindo baixa de ativos
baixa = []
for i in range(50):
    baixa.append(ativos[1]['resultados'][i]['series'][0]['serie'])
    #print(baixa[i])
