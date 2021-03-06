﻿from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier, RandomForestClassifier
from carregardados import carrega_dados_panda
from collections import Counter

def fit_and_predict(nome,modelo,dados_treino,marcacoes_treino,dados_teste,marcacoes_testes,dados_validacao,marcacoes_validacao):
    modelo.fit(dados_treino,marcacoes_treino)
    resultado = modelo.predict(dados_teste)
    acertos = (resultado == marcacoes_testes)
    total_de_acertos = sum(acertos)
    total_de_elementos = len(marcacoes_testes)
    treino = 100.0 * total_de_acertos/total_de_elementos
    msg = u"Porcentagem de acerto {0} é de {1}% ".format(nome,treino)
    print msg
    return treino
try:
    print "Inicio"
    X, Y, tamanho = carrega_dados_panda()
    tamanho_treino = tamanho * 0.8
    tamanho_teste = tamanho * 0.1
    tamanho_validacao = tamanho - (tamanho * 0.1)
    dados_treino = X[:int(tamanho_treino)]
    marcacoes_treino = Y[:int(tamanho_treino)]

    dados_teste =X[int(tamanho_treino):int(tamanho_validacao)]
    marcacoes_testes = Y[int(tamanho_treino):int(tamanho_validacao)]

    dados_validacao =X[int(tamanho_validacao):]
    marcacoes_validacao = Y[int(tamanho_validacao):]

    modelo = MultinomialNB()
    treinoMultinomial = fit_and_predict('Multinomial',modelo,dados_treino,marcacoes_treino,dados_teste,marcacoes_testes,dados_validacao,marcacoes_validacao)

    modelo = AdaBoostClassifier()
    treinoAdaboost  = fit_and_predict('AdaBoostClassifier',modelo,dados_treino,marcacoes_treino,dados_teste,marcacoes_testes,dados_validacao,marcacoes_validacao)

    if treinoAdaboost > treinoMultinomial:
        modelo = AdaBoostClassifier()
        print "AdaBoost"
    else:
        modelo = MultinomialNB()
        print "Multinomial"

    modelo.fit(dados_treino,marcacoes_treino)
    resultado2 = modelo.predict(dados_validacao)
    validado = (resultado2 == marcacoes_validacao)
    total_de_validacoes = sum(validado)
    total_de_elementos_validacao = len(marcacoes_validacao)
    validacao = 100.0 * total_de_validacoes / total_de_elementos_validacao
    msg = u"Validado de acerto é de {0}% ".format(validacao)
    print msg
    acertos_base = max(Counter(marcacoes_testes).itervalues())
    taxa_acertos_base = 100 * acertos_base / len(marcacoes_testes)
    print "Taxa Base de Acertos:{0}".format(taxa_acertos_base)
except Exception as e:
    print str(e)
