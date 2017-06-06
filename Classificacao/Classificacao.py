from sklearn.naive_bayes import MultinomialNB
from carregardados import carrega_dados
try:
    print "Inicio"
    X, Y = carrega_dados()    
    dados_treino = X[:90]
    marcacoes_treino = Y[:90]

    dados_teste =X[-9:]
    marcacoes_teste = Y[-9:]

    modelo = MultinomialNB()
    
    modelo.fit(dados_treino,marcacoes_treino)
    resultado = modelo.predict(dados_teste)

    diferencas = resultado - marcacoes_testes
    acertos = [d for d in diferencas if d==0]
    print len(acertos)
    print str(100 *(float(len(acertos))/float(len(marcacoes_testes))))+"%"
except Exception as e:
    print str(e)
