import os
os.system('clear')

idade= int(input("digite a idade: "))
altura = float(input("Digite a altura da modelo: "))

idade_certa = idade == 16
altura_certa = altura == 1.7

if(idade_certa and altura_certa):
    print("Aprovada")
else:
    print("Reprovada")














    