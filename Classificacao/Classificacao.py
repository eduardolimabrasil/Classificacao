from sklearn.naive_bayes import MultinomialNB

try:
    print "Inicio"
    cancer = [[1,0,1],
              [1,0,0],
              [1,1,0],
              [0,0,1],
              [1,0,1],
              [1,1,1]]
    
    marcacoes = [1,1,1,-1,-1,-1]
    amostra =[[0,0,0],[1,1,1],[1,0,0],[0,1,0]]

    modelo = MultinomialNB()
    
    modelo.fit(cancer,marcacoes)
    resultado = modelo.predict(amostra)
    marcacoes_testes = [-1,-1,1,-1]
    diferencas = resultado - marcacoes_testes
    print str(diferencas)
    acertos = [d for d in diferencas if d==0]
    print str(len(acertos))
    len(amostra)
except Exception as e:
    print str(e)
