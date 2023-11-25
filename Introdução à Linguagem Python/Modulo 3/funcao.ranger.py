
# Interando sobre uma faixa de valores gerada com a função range()

for i in range(5):
    print(i)

# Somatorio dos multiplos de 3 entre 1 e 100

soma_multi_3 = 0
for x in range ( 3, 100, 3):
    soma_multi_3 += x 
print(soma_multi_3)

# Imprimindo a taboada de um numero qualquer

num = (int(input("Digite o numero que deseja imprimir a taboada: ")))
for mult in range (1, 11):
    print("{} x {} = {}". format(num, mult, num*mult))

# Imprimindo a taboada de 1 a 9

for num in range (1, 11):
    for mult in range( 1, 11):
        print("{} x {} = {}". format(num, mult, num*mult))
    

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


