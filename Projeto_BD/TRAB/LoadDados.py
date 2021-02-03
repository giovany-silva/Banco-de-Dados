import  ConexaoComBD
import ativo
import compra
import despesas
import empresas
import estoque
import gastos
import pessoal
import receitas

setor = empresas.setor
anos = []
con = ConexaoComBD
con.startConnection()
i=2007
while(i<=2018):
    anos.append(i)
    i=i+1

def PreencherSetores():
    for i in setor:
        for n in range(len(anos)):
            con.QueryTol("insert into setor(setor , ano) values ('"+ i.strip("[']") +"' , '"+str(anos[n])+"')")

#INSERT INTO receita (total, deducao, liquida, id_setor)
#VALUES (100, 90, 10, (select setor.id_setor from setor where setor.setor='1.Total' and setor.ano=2007));
deducao = receitas.deducao
liquida = receitas.liquida
total = receitas.total
def PreencherReceitas():
    for n in range(len(anos)):
        for i in range(50):
            con.QueryTol("insert into receita(total, deducao, liquida, id_setor) values ("+str(total[i][str(anos[n])])+","+str(deducao[i][str(anos[n])])+","+str(liquida[i][str(anos[n])])+","+"(select setor.id_setor from setor where setor.setor='"+str(setor[i].strip("[']"))+"' and setor.ano="+str(anos[n])+"));")

#INSERT INTO pessoal (numempresas, pessoalocupado, id_setor)
#VALUES (100, 90, (select setor.id_setor from setor where setor.setor='1.Total' and setor.ano=2007));
emp = pessoal.numEmpresas
ocupado = pessoal.pessoalOcupado
def PreencherPessoal():
    for n in range(len(anos)):
        for i in range(50):
            con.QueryTol("INSERT INTO pessoal (numsetors, pessoalocupado, id_setor) VALUES ("+str(emp[i][str(anos[n])])+","+str(ocupado[i][str(anos[n])])+","+
            "(select setor.id_setor from setor where setor.setor='"+str(setor[i].strip("[']"))+"' and setor.ano="+str(anos[n])+"));")

#INSERT INTO gastos (salario, fgts, indenizacao, id_setor)
#VALUES (100, 90, 30, (select setor.id_setor from setor where setor.setor='1.Total' and setor.ano=2007));
fgts = gastos.fgts
ind = gastos.indenizacao
salario = gastos.salario
def PreencherGastos():
    for n in range(len(anos)):
        for i in range(50):
            con.QueryTol("INSERT INTO gastos (salario, fgts, indenizacao, id_setor) VALUES ("+str(salario[i][str(anos[n])])+","+str(fgts[i][str(anos[n])])+","+str(ind[i][str(anos[n])])+","+
            "(select setor.id_setor from setor where setor.setor='"+str(setor[i].strip("[']"))+"' and setor.ano="+str(anos[n])+"));")

#INSERT INTO estoque (total, produtos, materiaprima, materiaembalagem, id_setor)
#VALUES (100, 90, 30,40, (select setor.id_setor from setor where setor.setor='1.Total' and setor.ano=2007));
totalE = estoque.total
prod = estoque.produtos
prima = estoque.materiaPrima
emb = estoque.materiaEmbalagem
def PreencherEstoque():
    for n in range(len(anos)):
        for i in range(50):
            if totalE[i][str(anos[n])] == "-": totalE[i][str(anos[n])] = "NULL"
            if prod[i][str(anos[n])] == "-": prod[i][str(anos[n])] = "NULL"
            if prima[i][str(anos[n])] == "-": prima[i][str(anos[n])] = "NULL"
            if emb[i][str(anos[n])] == "-": emb[i][str(anos[n])] = "NULL"
            con.QueryTol("INSERT INTO estoque (total, produtos, materiaprima, materiaembalagem, id_setor) VALUES ("+str(totalE[i][str(anos[n])])+","+str(prod[i][str(anos[n])])+","+str(prima[i][str(anos[n])])+","+str(emb[i][str(anos[n])])+","+
            "(select setor.id_setor from setor where setor.setor='"+str(setor[i].strip("[']"))+"' and setor.ano="+str(anos[n])+"));")
    
#INSERT INTO despesa (aluguel, terceiro, comunicacao, aguaenergiaesgoto,imposto,outras, id_setor)
#VALUES (100, 90, 30,40,40,50, (select setor.id_setor from setor where setor.setor='1.Total' and setor.ano=2007));
agua=despesas.aguaEnergiaEsgoto
aluguel=despesas.aluguel
com = despesas.comunicacao
outras = despesas.outras
terc = despesas.terceiro
imp = despesas.imposto
def PreencherDespesas():
    for n in range(len(anos)):
        for i in range(50):
            con.QueryTol("INSERT INTO despesa (aluguel, terceiro, comunicacao, aguaenergiaesgoto,imposto,outras, id_setor) VALUES ("
            +str(aluguel[i][str(anos[n])])+","+str(terc[i][str(anos[n])])+","+str(com[i][str(anos[n])])+","+
            str(agua[i][str(anos[n])])+","+str(imp[i][str(anos[n])])+","+str(outras[i][str(anos[n])])+","+
            "(select setor.id_setor from setor where setor.setor='"+str(setor[i].strip("[']"))+"' and setor.ano="+str(anos[n])+"));")

#INSERT INTO compra (total, revenda, materiaprima, materiaembalagem, id_setor)
#VALUES (100, 90, 30,40, (select setor.id_setor from setor where setor.setor='1.Total' and setor.ano=2007));
totalC = compra.total
rev = compra.revenda
primaC = compra.materiaPrima
embC = compra.materiaEmbalagem
def PreencherCompra():
    for n in range(len(anos)):
        for i in range(50):
            if totalC[i][str(anos[n])] == "-": totalC[i][str(anos[n])] = "NULL"
            if rev[i][str(anos[n])] == "-": rev[i][str(anos[n])] = "NULL"
            if primaC[i][str(anos[n])] == "-": primaC[i][str(anos[n])] = "NULL"
            if embC[i][str(anos[n])] == "-": embC[i][str(anos[n])] = "NULL"
            con.QueryTol("INSERT INTO compra (total, revenda, materiaprima, materiaembalagem, id_setor) VALUES ("+str(totalC[i][str(anos[n])])+","+str(rev[i][str(anos[n])])+","+str(primaC[i][str(anos[n])])+","+str(embC[i][str(anos[n])])+","+
            "(select setor.id_setor from setor where setor.setor='"+str(setor[i].strip("[']"))+"' and setor.ano="+str(anos[n])+"));")
    
#INSERT INTO ativos (aquisicao, baixa, id_setor)
#VALUES (100, 90, (select setor.id_setor from setor where setor.setor='1.Total' and setor.ano=2007));
aq = ativo.aquisicao
baixa = ativo.baixa
def PreencherAtivos():
    for n in range(len(anos)):
        for i in range(50):
            if aq[i][str(anos[n])] == "-": aq[i][str(anos[n])] = "NULL"
            if baixa[i][str(anos[n])] == "-": baixa[i][str(anos[n])] = "NULL"
            con.QueryTol("INSERT INTO ativos (aquisicao, baixa, id_setor) values ("
            +str(aq[i][str(anos[n])])+","+str(baixa[i][str(anos[n])])+","+"(select setor.id_setor from setor where setor.setor='"+str(setor[i].strip("[']"))+"' and setor.ano="+str(anos[n])+"));")

#Fecha conexao
PreencherSetores()
PreencherReceitas()
PreencherPessoal()
PreencherGastos()
PreencherEstoque()
PreencherDespesas()
PreencherCompra()
PreencherAtivos()

con.ClosedConnection()