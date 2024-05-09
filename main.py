import PyPDF2 
import pandas

#Abrindo um arquivop em moto leitura 'r' e lendo o binário 'rb'
pdf_file = open(r"C:\Users\abe4ca\Desktop\joao.pdf", "rb") #Tem que ficar assim pra dar certo
#pdf_file = open("C:\\Users\\abe4ca\\Desktop\\joao.pdf", "rb") #Ou assim

#Após pegar o binário, pegamos os dados do pdf do binário
dados_do_pdf = PyPDF2.PdfReader(pdf_file)
#Printando o número de páginas do pdf que acabamos de ler
print("Números de páginas: {}".format(str(len(dados_do_pdf.pages))))

#Setando a variável pagina1
pagina1 = dados_do_pdf.pages[0] #Pegando a página 1

#Pegando o texto extrado da página 1
texto_pagina_1 = pagina1.extract_text()

#Passando para dicionario para passar no excel... ou fazer em lista
data = {'dados' : [texto_pagina_1]}

#Só para ver como ficou
print(data)

#Preparando os dados para o excel
teste = pandas.DataFrame(data)
#Passando para o excel
teste.to_excel('C:/Users/abe4ca/Desktop/teste.xlsx')
