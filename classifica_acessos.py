from dados import carregar_acessos

x, y = carregar_acessos()

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()

modelo.fit(x, y)

print (modelo.predict([[1,0,1], [0,1,0], [1,0,0], [1,1,0], [1,1,1]]))

