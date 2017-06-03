from sklearn.naive_bayes import MultinomialNB

cancer = [[1,0,1],
          [1,0,0],
          [1,1,0],
          [0,0,1],
          [1,0,1],
          [1,1,1]]

marcacoes = [1,1,1,0,0,0]
amostra =[0,0,0]
modelo = MultinomialNB()

modelo.fit(cancer,marcacoes)
print modelo.predict(amostra)

