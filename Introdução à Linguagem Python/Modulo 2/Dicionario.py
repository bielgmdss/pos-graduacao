
#  Em um dicionario, nos armazenamos uma informação (valor) que queremos localizar e recuperar posteriomente atraves de uma chave

# - O principal proposito de um dicionario é associar um valor (value) a uma chave (key)

dic_vazio1 = {}
dic_vazio2 = dict()

print(type(dic_vazio1))
print(isinstance(dic_vazio2, dict))

# Criando um Dicionario

dic_estados = { "MG":"Minas Gerais", "PR": "Paraná", "BA": "Bahia", "RN": "Rio Grande do Norte", "AM": "Amzonas"}
print(dic_estados)

dic_produtos = {1215:"Lápis", 3221:"Caneta", 2329:"Borracha", 1092:"Caderno", 7633:"Cola"}
print(dic_produtos)

dic_notas_alunos = {"João":[30, 12, 21], "Maria": [20, 30, 29], "José": [20, 23, 19]}
print(dic_notas_alunos)

dic_notas_alunos2 = {"João": {"nota1": 30, "nota2": 12, "nota3": 21}, 
                     "Maria": {"nota1": 20, "nota2": 30, "nota3": 29}, 
                     "José": {"nota1": 20, "nota2": 23, "nota3": 19}, 
                    }
print(dic_notas_alunos2)

# Modificando os elementos 

dic_estados["PR"]

print("Eu nasci em "+dic_estados["MG"]+".")

dic_produtos[2329]

nome_aluno = "Maria"

print("As notas de "+nome_aluno+" foram: "+str(dic_notas_alunos[nome_aluno])+".")

print(nome_aluno+" tirou "+str(dic_notas_alunos[nome_aluno][0])+" pontos na 1a prova.")

print(dic_notas_alunos2["João"]["nota1"])

print(dic_estados)

# Modificando valores no dicionario

dic_estados["AM"] = "Amazonas"
print(dic_estados)

dic_notas_alunos["João"][1] = 22
print(dic_notas_alunos)

# Criando um nove dicionario a parti da seleçao dsa chaves que deseja

dic_num_pares = dict.fromkeys([2, 4, 6, 8, 10])
print(dic_num_pares)

# - Se deseja atribuir um valor default, basta informa aposta a lista com a chaves

dic_num_pares = dict.fromkeys([2, 4, 6, 8, 10], "par")
print(dic_num_pares)

# O metodo GET() retorna o valor associado a uma chave

dic_exemplo = {1: "um", 2: "dois", 3: "tres",4 : "quatro" }

dic = dic_exemplo.get(2)
print(dic)

dic2 = dic_exemplo.items()
print(dic2)

dic3 = dic_exemplo.keys()
print(dic3)

dic4 = dic_exemplo.pop(1)
print(dic4)


# POPITEM()

removido = dic_num_pares.popitem
print(removido)

# SETDEFAULT()

mg=dic_estados.setdefault("MG")
print(mg)

dic_estados.setdefault("SC", "Santa Catarina")
print(dic_estados)


#UPDATE()
