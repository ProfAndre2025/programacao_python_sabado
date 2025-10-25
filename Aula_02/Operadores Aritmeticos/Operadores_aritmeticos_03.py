import os
os.system('clear')

quantidade = 5
valor = 2800.00
desconto = 0.15

#primeira forma
total = quantidade*valor
desc = total*desconto
valorFinal = total-desc

print(f"total: {valorFinal}")
print(f"Total se desconto: {total}")

#segunda forma
total02 = quantidade*(valor-((valor/100)*15))
print(total02)