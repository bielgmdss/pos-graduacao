
# Comando IF é o comando de decisão, ele faz a decisao baseada em uma condição e essa condição so retorna
# 2 valores possiveis TRUE OU FALSE

## - if (condição):
      #  bloco_comandos1 - A identação deve ter 4 espaços ou 1 tabulação
         # Se for verdadeiro ele executa mas se for falso ele não executa


## - if (condição): - Se minha condição for verdadeiro o bloco_comandos1 é executado 
      #  bloco_comandos1
  #  Else: - Se minha condição for falsa o bloco_comandos2 é executado 
      #  bloco_comandos2

## - if (condição): - Se a condição 1 for dado como verdadeiro o bloco_comandos1 é executado
       #  bloco_comandos1
   # elif(condição2): - Se a condição 2 for dado como verdadeiro o bloco_comandos2 é executado
       #  bloco_comandos1
   # elif(condiçãon): - Se a condição n for dado como verdadeiro o bloco_comandosn é executado
       #  bloco_comandosn


## - if (condição): - Se a condição 1 for dado como verdadeiro o bloco_comandos1 é executado
       #  bloco_comandos1
   # elif(condição2): - Se a condição 2 for dado como verdadeiro o bloco_comandos2 é executado
       #  bloco_comandos1
   # elif(condiçãon): - Se a condição n for dado como verdadeiro o bloco_comandosn é executado
       #  bloco_comandosn
   #  else: - Se nenhuma condição anterior for veridadeira ao o bloco_comandoselse é executado 
       #  bloco_comandoselse


peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso/altura **2

if imc <20:
    print("Seu peso está abaixo do ideal. Seu IMC = {}.".format(imc))
else:
    if imc >= 20 and imc<= 25:
        print("Seu peso está dentro da faixa ideal. Seu IMC = {}.".format(imc))
    else: 
        print("Seu peso está acima do ideal. Seu IMC = {}.".format(imc))




