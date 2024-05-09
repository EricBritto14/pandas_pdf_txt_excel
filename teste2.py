import pandas

teste = open("C:/Users/abe4ca/Desktop/joao.txt", "r", encoding="utf-8")
valor = teste.readlines()
print(valor)

data = {'dados' : [valor]}

#Preparando os dados para o excel
teste = pandas.DataFrame(valor)
#Passando para o excel
teste.to_excel('C:/Users/abe4ca/Desktop/teste2.xlsx')