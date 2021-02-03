from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect


#Criar uma interface para capturar o nome e senha do usuario para logar no banco
	
#chamar essa funcao de acordo com a senha e usuario digitadas
engine = create_engine("postgresql+psycopg2://mariab:mariab123@localhost:5432/Projeto_BD",echo=False)

# cria um objeto da classe declarative. Será o 'catálogo'
base = automap_base()

#mapeamento
base.prepare(engine,schema="public",reflect=True)
	

print(base.classes.keys())
	
#https://medium.com/jmeter/jmeter-af2d4c00cae0
#https://pt.slideshare.net/BeatrizMakiyamaCeles/treinamento-como-usar-o-jmeter-interpretar-resultados-e-otimizar-a-execuo-67476358