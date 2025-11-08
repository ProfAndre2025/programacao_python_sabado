import os
os.system('clear')

cont = 0
acm = 0

numero = int(input("digite um numero ou 0 para encerrar: "))

while (True):
    if(numero == 0):
        break
    
    acm = acm+numero
    numero = int(input("digite um numero ou 0 para encerrar: "))

print(f"Programa encerrado e a soma total foi {acm}")