import os
os.system('clear')

idade= int(input("digite a idade: "))
altura = float(input("Digite a altura da modelo: "))
etinia = input("Digite a etinia da candidata: ")

if(idade == 16 and altura == 1.7 and etinia == "indigena"):
    print("Candidata aprovada")
else:
    print("Candidata Reprovada")

    