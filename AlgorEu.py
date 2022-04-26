"""
Programa para calcular un máximo común divisor
Autor : Montserrat Gil
Fecha: 22 de abril 2022
"""

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

fin = False

while not fin:
    division = int(num1/num2)
    resto = num1%num2
    
    ##print(strin)
    if resto==0:
        print(num2)
        fin = True
    else:
        temp1 = num1
        num1=num2
        num2=temp1-(division*num2)
