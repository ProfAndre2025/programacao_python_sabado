import os
os.system('clear')

idade = int(input("digite um numero: "))

if(idade<=11):
    print("Infantil")
elif (idade >=12 and idade <= 17):
    print("Adolecente")
elif(idade >=18 and idade < 24):
    print("Jovem")
else:
    print("Adulto") 