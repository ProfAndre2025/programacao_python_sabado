import os
os.system('clear')

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))

total = num1+num2

if(total>20):
    total=total+8
    print(total)
else:
    total = total-5
    print(total)
