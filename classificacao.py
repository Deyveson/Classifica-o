# e gordinho? tem perninha curta? se faz au au?
porco1 =   [1,1,0]
porco2 =   [1,1,0]
porco3 =   [1,1,0]
cachoro1 = [1,1,1]
cachoro2 = [0,1,1]
cachoro3 = [0,1,1]

dados = [porco1, porco2, porco3,
		cachoro1, cachoro2, cachoro3]

marcacoes = [1,1,1,-1,-1,-1]
#Ensinando o algoritmo através de dados.

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()

modelo.fit(dados, marcacoes)
#Treiando o algoritmo, para aprender baseado nos dados e marcações

misterioso1 = [1,1,1]
misterioso2 = [1,0,0]
misterioso3 = [1,0,1]

testes = [misterioso1,misterioso2,misterioso3]
#Execulta os teste, passando dados pra ele prever, o que são baseado no que ele aprendeu

marcacoes_teste = [-1, 1, 1]

resultado = modelo.predict(testes)

print (resultado)

diferencas = resultado - marcacoes_teste

print (diferencas)

acertos = [d for d in diferencas if d == 0]
#Loop para percorer os acertos, para cada uma das diferencas se for igual a 0 Acertou.

total_de_acertos = len(acertos)
# Total de Acertos

total_de_elementos = len(testes)
# Total de Elementos teste

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos
#Calculando a taxa de acerto

print (taxa_de_acerto)
