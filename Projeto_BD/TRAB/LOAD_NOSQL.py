import requests
import json	
from unidecode import unidecode

import pymongo
from pymongo import MongoClient

client=MongoClient("localhost",27017)
print("ok")
db=client.trabalho


#ativos
Url = "https://servicodados.ibge.gov.br/api/v3/agregados/1415/periodos/2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018/variaveis/1517|1518?localidades=N1[all]&classificacao=11070[all]"
ativos = requests.get(Url).json()
db.ativos.insert_many(ativos)

#compras
Url = "https://servicodados.ibge.gov.br/api/v3/agregados/1411/periodos/2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018/variaveis/1443|504|1444|1445?localidades=N1[all]&classificacao=11070[all]"
compras = requests.get(Url).json()
db.compras.insert_many(compras)

#depesas
Url = "https://servicodados.ibge.gov.br/api/v3/agregados/1401/periodos/2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018/variaveis/1402|1403|1404|1405|1001406|1407?localidades=N1[all]&classificacao=11070[all]"
depesas = requests.get(Url).json()
db.depesas.insert_many(depesas)

#empresas
Url = "https://servicodados.ibge.gov.br/api/v3/agregados/1415/periodos/2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018/variaveis/1517|1518?localidades=N1[all]&classificacao=11070[all]"
empresas = requests.get(Url).json()
db.empresas.insert_many(empresas)

#estoques
Url = "https://servicodados.ibge.gov.br/api/v3/agregados/1411/periodos/2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018/variaveis/1449|1500|1450|1451?localidades=N1[all]&classificacao=11070[all]"
estoques = requests.get(Url).json()
db.estoques.insert_many(estoques)

#gastos
Url = "https://servicodados.ibge.gov.br/api/v3/agregados/1414/periodos/2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018/variaveis/314|1411|1502?localidades=N1[all]&classificacao=11070[all]"
gastos = requests.get(Url).json()
db.gastos.insert_many(gastos)

#pessoal
Url = "https://servicodados.ibge.gov.br/api/v3/agregados/1417/periodos/2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018/variaveis/310|631?localidades=N1[all]&classificacao=11070[all]"
pessoal = requests.get(Url).json()
db.pessoal.insert_many(pessoal)

#receitas
Url = "https://servicodados.ibge.gov.br/api/v3/agregados/1410/periodos/2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018/variaveis/863|642|643?localidades=N1[all]&classificacao=11070[all]"
receitas = requests.get(Url).json()
db.receitas.insert_many(receitas)





