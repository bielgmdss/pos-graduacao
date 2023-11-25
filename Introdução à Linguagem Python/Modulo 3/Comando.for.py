

lista = [3, 5, 7, 9, 13, 17, 23]
for num in lista:
    print(num)
print(num)

# Verificando se é par ou impar

for num in lista:
    if num % 2 == 0: # % resto da divisao
        print("{} é par.".format(num))
    else:
        print(num, "é impar")


# Verificando quantos numeros são par e quantos são impar

cont_impar = 0
cont_par = 0
for num in lista:
    if num % 2 ==0:
        cont_par += 1
    else:
        cont_impar += 1
print("A lista contem {} numeros pares e {} numeros impares.".format(cont_par, cont_impar))

# Somatorio

soma = 0
for n in lista:
    soma += n
print("A soma dos elementos da lista = ", soma)

# Forma mais facil de calcular o Somatorio de todos os elementos

print("A soma dos elementos da lista = ", sum(lista))

# Para calcular elementos escolhidos é preciso usar outros codigos

soma_impar = 0
for n in lista:
    if n % 2 == 1:
        soma_impar = soma_impar + n
print("A soma dos elementos impares da lista = ", soma_impar)

# Interando sobre um string

maiorpalavrar = " GABRIELMARCOSDASILVASANTOS"
for letra in maiorpalavrar:
    print(letra)

# Interando sobre uma Tupla

tupla = (1, 19, 5, 12, 6)
for ele in tupla:
    print(ele)

lista_tupla = [(1, 2, 3),(4, 5, 6), (7, 8, 9)]
(t1, t2, t3) = lista_tupla[1] # desmembrando a tupla
print(type(lista_tupla))
print(type(lista_tupla[1]))
print(type(t1))
print(lista_tupla)
print(lista_tupla[1])
print(t1)

lista_tupla_notas = [(18, 20, 15, 22), (10, 15, 25, 19), (16, 24, 21, 20), (10, 13, 18, 13)]
for (ele1, ele2, ele3, ele4) in lista_tupla_notas:
    print("A 3a nota = {}.".format(ele3))


# Interagindo com um conjunto

conj1 = {1, 5, 2, 6, 3, 4}
for ele5 in conj1:
    print(ele5)

conj2 = {1, 17, 12, 4, 2, 20}  
for ele5 in conj1:
    if ele5 in conj2:
        print(" O elemento {} esta contigo em conj2.". format(ele5))
    else:
        print(" O elemento {} não esta contigo em conj2.". format(ele5))


# Iterando em um dicionario

dic_estados = { "MG":"MINAS GERAIS", "PR":"PARANA", "BA":"BAHIA", "AM":"AMAZONAS", }
for a in dic_estados:
    print(a)

for b in dic_estados.values():
    print(b)

for (sig, est) in dic_estados.items():
    print("A sigla para {} é {}". format(est, sig))
    
        


