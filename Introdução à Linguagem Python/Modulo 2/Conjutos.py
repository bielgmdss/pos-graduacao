
# São coleções de elementos unicos

# - Não suportam indexação como as listas e tuplas


# Criando conjuntos vazios
conj_vazio1 = set() # Essa é a única forma de se criar um conjunto vazio
conj_vazio2 = {} # As chaves são utilizadas para construir um dicionário vazio.

print(type(conj_vazio1))
print(type(conj_vazio2))

# Criando conjuntos com elementos
conj1 = {1, 2, 3, 4, 5}
conj2 = {"A", "B", "C", "D"}
conj3 = {"ABC", 123, 3.14}

# Conjuntos não podem conter outras estruturas aninhadas
# conj3 = {1, "ABC", [1,2,3]} # Provoca um erro por causa da lista

# Conjuntos não suportam indexação. Então vamos precisar do comando for para acessar os elementos de um conjunto
for elem in conj1:
    print(elem)

# Tentar acessar uma posição em um conjunto provoca um erro
# conj1[0]

# Visualizando os elementos de conj1
print(conj1)

# Adicionando o elemento 6 add()
conj1.add(6)
print(conj1)

# Visualizando os elementos de conj3
print(conj3)

# Apagando clear()

conj3.clear()
print(conj3)


# Copiando conjunto copy()

conj3 = conj1.copy()
print(conj3)

# Atribuindo a diferença entre os conjuntos

s1 = {1,2,3,4,5}
s2 = {4,5,6,7}
s3 = s1.difference(s2)
print(s3)

# Intersection()

s4 = s1.intersection(s2)
print(s4)

# isdisjoint() Verificando se tem em comum
s5=s1.isdisjoint(s2)
s6=s3.isdisjoint(s4)
print(s5)
print(s6)

# Verificando se é um subconjunto

s7 = s1.issubset(s2)
print(s7)

s8 = s3.issubset(s1)
print(s8)

























