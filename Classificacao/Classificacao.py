from sklearn.naive_bayes import MultinomialNB
from carregardados import carrega_dados_panda
from collections import Counter

try:
    print "Inicio"
    X, Y, tamanho = carrega_dados_panda()
    tamanho_treino = tamanho * 0.9
    tamanho_teste = tamanho - tamanho_treino
    dados_treino = X[:int(tamanho_treino)]
    marcacoes_treino = Y[:int(tamanho_treino)]

    dados_teste =X[-int(tamanho_teste):]
    marcacoes_testes = Y[-int(tamanho_teste):]

    modelo = MultinomialNB()
    
    modelo.fit(dados_treino,marcacoes_treino)
    resultado = modelo.predict(dados_teste)
    acertos = (resultado == marcacoes_testes)
    acertos_base = max(Counter(marcacoes_testes).itervalues())
    taxa_acertos_base = 100 * acertos_base / len(marcacoes_testes)
    print float(taxa_acertos_base)
    print float(sum(acertos))
    print str(100 *(float(len(acertos))/float(len(marcacoes_testes))))+"%"
except Exception as e:
    print str(e)
