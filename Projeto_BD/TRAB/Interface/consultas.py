

import ConexaoComBD
con = ConexaoComBD
def Consultar(tabelaName , setorIndex):
    setorIndex = setorIndex * 12
    base = setorIndex - 11

    dados = con.GetDate('select * from ' + str(tabelaName) + ' where id_setor >= '+str(base)+'and id_setor <='+str(setorIndex) )
    return dados