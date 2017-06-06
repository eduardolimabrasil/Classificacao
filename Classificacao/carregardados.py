import csv

def carrega_dados():
    dados = []
    marcacoes = []
    arquivo = open('acesso.csv','rb')
    leitor = csv.reader(arquivo)
    leitor.next()
    for home, como_funciona,contato, comprou in leitor:
        dados.append([int(home),int(como_funciona),int(contato)])
        marcacoes.append([int(comprou)])
    return dados , marcacoes