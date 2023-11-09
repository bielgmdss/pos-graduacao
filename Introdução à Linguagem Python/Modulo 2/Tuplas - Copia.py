# TUPLAS é uma coleção de elementos igual a lista, mas sua principal diferença é que a tupla é imutavel.

# - Não pode ser alterada 


# Criando uma TUPLA

tuplas_vazia = ()
tuplas_vazia2 = tuple()

print(tuplas_vazia)
print(tuplas_vazia2)

# Criando TUPLA com elementos

tupla1 = (3, 19, 4, 21, 3, 5, 13)
tupla2 = (3, 19, 4, 21, 3, 5, 13, "tupla",(1, 2, 3))
tupla3 = (3, 19, 4, 21, 3, 5, 13, "tupla",[1, 2, 3])

print(tupla1)
print(tupla2)
print(tupla3)


# Imutavel

## - tupla1[0] =5
## - print(tupla1)


# Acessando o indice 0 da tupla 1

indice1 = tupla1[0]
print(indice1)

indice2 = tupla2[5]
print(indice2)

indice3 = tupla3[8]
print(indice3)


# Conseguimos mudar uma lista que esta em uma TUPLA

tupla3[8][1] = 5
print(tupla3)

tupla3[8].extend([4, 5, 6])
print(tupla3)

# Verificando quantas vezes o numero 3 aparece em tupla

vezes_aparece3 = tupla1.count(3)
print(vezes_aparece3)

# Verificando em que posiçao esta armazenada o elemento

onde_esta = tupla1.index(21)
print(onde_esta)


print(len(tupla1))
print(max(tupla1))
print(min(tupla1))
print(sum(tupla1))


# Convertendo uma tupla em lista e alterando os valores

lista = list(tupla1)

print(lista)

lista[6] = -1 

print(lista)

