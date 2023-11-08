
# LISTAS é uma coleçao de elementos

# - Cada elemento possui uma posicao dentro de uma lista. Essa possiçao é chamada indice
# - Começa a contar do 0 na ordem crescente e -1 na ordem decrescente 

# Criando uma lista vazia

lista_vazia = []
lista_vazia2 = list()

# Criando listas com elementos

lista = [23, 56, 2, -3, 10, 2, 18, 0, 5]
lista_reais = [1.5, -2.13, 5.14]
lista_string = ["Gabriel", "Python", "PUC Minas", "Ciencia de Dados e Big Data"]
lista_booleanos = [True, True, False, True]
lista_misturada = [1, 2, 3.14159, "teste"]
lista_misturada2 = [1, 2, 3.14159, "teste", [1, "A", 1.0]]
listas_alinhadas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Vendo as listas

print(lista)
print(lista_reais)
print(lista_string)
print(lista_booleanos)
print(lista_misturada)
print(lista_misturada2)
print(listas_alinhadas)

# Como acessar elementos de uma lista

lista_0 = lista[0]
print(lista_0)

lista_string3 = lista_string[3]
print(lista_string3)

lista_misturada3 = lista_misturada[3]
print(lista_misturada3)

lista_misturada2_3 = lista_misturada2[4][1]
print(lista_misturada2_3)


# Como modificar elementos de uma lista

lista[1] = 18
print(lista)

# Modificando o elemento do indice 2. Ele recebe a soma dos dois elementos anteriores

lista[2] = lista[0] + lista[1]

print(lista)

# Adicionando o 17 no final da lista = append()

lista.append(17)
print(lista)

# Removendo todos os elementos da lista_reais - clear()

lista_reais.clear()
print(lista_reais)

# Copiando uma lista para outra - copy()

copia = lista.copy()
print(copia)

copia[0] = 5
print(copia)

# Verificando quantos vezes o numero aparece - count()

repetido = copia.count(5)
print(repetido)

# Maneira correta de adicionar novos elementos de uma lista, a partir de outra lista - extend()

numeros = [1, 2, 3]
numeros.extend([4,5])
print(numeros)

# Redefinindo os elementos da lista

lista = [1, 3, 7, 2, 3, 8, 4]
lista.index(7)
print(lista)

posicao8 = lista.index(8) ## - Ele vai pegar o primeiro indice que aparece
print(posicao8)

# O metodo insert () permite adicionar um elemento em qualquer posiçao da lista

lista.insert(2, "ABC")
print(lista)

lista.insert(100, "XYZ")
print(lista)

# O metodo pop() quando desejamos apagar uma posiçao da lista 

valor = lista.pop(2)
print(valor)
print(lista)

# Utilizamos o remove() quando desejamos apagar um elemento especifico da lista 

print(lista_string)

lista_string.remove("Gabriel")

print(lista_string)

# Redefinindo os elementos da lista - reverse()
lista = [1, 2, 3, 4, 5, 6]
lista.reverse()
print(lista)

# Redefinindo os elementos da lista na sorte - sort()
lista = [1, 2, 3, 4, 5, 6, 25]
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

print(sum(lista))
print(max(lista))
print(len(lista))
print(min(lista))
