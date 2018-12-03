import csv

def carregar_acessos():

    x = []
    y = []

    arquivo = open('acesso.csv', 'r')
    #Abrindo o arquivo CSV
    leitor = csv.reader(arquivo)
    #Lendo e botando dentro da variavel leitor

    next(leitor)
    #Ignorando a primeira linha do array

    for home,como_funciona, \
        contato, comprou in leitor:

        x.append([int(home),
            int(como_funciona),
            int(contato)])
        y.append(int(comprou))
    return x, y
    #Percorrendo os acessos, inserindo os dados em  x(Lado esquerdo) e y(Lado direito).
