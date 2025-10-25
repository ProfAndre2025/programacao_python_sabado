import os
os.system('clear')
salarioMinimo = float(input("Digite o salario minimo: "))
qtdeKw = int(input("Digite a quantidade de quilowatts usado: "))

umKW = (salarioMinimo/7)/100
kwGasta = qtdeKw * umKW
kwGastoDesc = kwGasta - (kwGasta*0.10)
print(f"Total a pagar R${kwGastoDesc}")
