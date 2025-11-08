import os
os.system('clear')
import math

num1 = int(input("Digite um numero: "))

if(num1>=0):
    raiz=math.sqrt(num1)
    print(raiz)
else:
    quadrado = math.pow(num1,2)
    print(quadrado)
