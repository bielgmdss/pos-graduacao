
# Enquanto for verdadeiro a repetiçao continua



#lista_idades = []
#lista_pessoas = []

#nome = (str(input("Digite um nome: ")))
#while (nome.lower() != 'fim'):
    #idade = (int(input("Digite uma idade: ")))
    #lista_idades.append(idade)
    #lista_pessoas.append(nome)
    #nome = (str(input("Digite um nome: ")))

#print("\n\nNomes digitados\n============") 
#print(lista_pessoas)
#print("\nIdades\n============")    
#print(lista_idades)

##############################################################################################

#lista_idades = []
#lista_pessoas = []
#cont = 0

#while (cont <5):
    #nome = (str(input("Digite um nome: ")))
    #idade = (int(input("Digite uma idade: ")))
    #lista_idades.append(idade)
    #lista_pessoas.append(nome)
    #cont = cont + 1

#print("\n\nNomes digitados\n============") 
#print(lista_pessoas)
#print("\nIdades\n============")    
#print(lista_idades)


##############################################################################################

soma = 0
qtde = 0
den = 0
termo = 1
while (termo>0.0001):
    qtde += 1
    den = qtde ** 2
    termo = 1/den
    soma += termo
    print("{} o termo {}/{} = {}".format(qtde, 1, den, termo))
print(soma)






