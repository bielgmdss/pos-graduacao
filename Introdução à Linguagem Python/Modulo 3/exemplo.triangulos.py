
lado1 = float(input("Digite o primeiro lado do triangulo: "))
lado2 = float(input("Digite o segundo lado do triangulo: "))
lado3 = float(input("Digite o terceiro lado do triangulo: "))

if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado3 + lado1 > lado2):
    print("Os lados {}, {} e {} formam um triangulo" .format(lado1, lado2, lado3))
else: 
    print("Os lados {}, {} e {} Não formam um triangulo" .format(lado1, lado2, lado3))

############################################################################################

if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado3 + lado1 > lado2):   
    if (lado1 == lado2) and (lado2 == lado3):     
        print("Os lados {}, {} e {} formam um triangulo esquilatero" .format(lado1, lado2, lado3))
    else:
        if (lado1 == lado2) or (lado2 == lado3) or (lado3== lado1):
            print("Os lados {}, {} e {} formam um isoceles" .format(lado1, lado2, lado3))
        else:
            print("Os lados {}, {} e {} formam um escaleno" .format(lado1, lado2, lado3))
else: 
    print("Os lados {}, {} e {} Não formam um triangulo" .format(lado1, lado2, lado3))            

############################################################################################


if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado3 + lado1 > lado2):   
    if (lado1 == lado2) and (lado2 == lado3):     
        print("Os lados {}, {} e {} formam um triangulo esquilatero" .format(lado1, lado2, lado3))
    elif (lado1 == lado2) or (lado2 == lado3) or (lado3== lado1):
        print("Os lados {}, {} e {} formam um isoceles" .format(lado1, lado2, lado3))
    else:
        print("Os lados {}, {} e {} formam um escaleno" .format(lado1, lado2, lado3))
else: 
    print("Os lados {}, {} e {} Não formam um triangulo" .format(lado1, lado2, lado3))  



