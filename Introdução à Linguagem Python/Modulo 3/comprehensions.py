
# Uma maneira bastante concisa que o Python fornece para a criação de sequencias (lista, tuplas, dicionarios, string, etc)

# Digitando todos os elementos
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(lista)

# Usando a função ranger()
lista1 = list(range(1,21))
print(lista1)

# Usando a função for
lista3 = []
for i in range (1,21):
    lista3.append(i)
print(lista3)   

# Usando comprehensions
lista4 = [i for i in range(1,21)]
print(lista4)


pares2 = [num for num in range(1,51) if num % 2 == 0]
print(pares2)

divisao3e7 = [num for num in range(1,100) if num % 3 == 0 and num % 7 == 0]
print(divisao3e7)

letras = [l.upper() for l in "palavra"]
print(letras)




