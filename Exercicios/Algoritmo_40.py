import os
os.system('clear')

dividendo = float(input("Digite um numero: "))
divisor = float(input("Digite um numero: "))

quociente = dividendo/divisor
resto = dividendo%divisor

print(f"Dividendo: {dividendo}\nDivisor: {divisor}\nQuociente: {quociente}\nResto: {resto}")