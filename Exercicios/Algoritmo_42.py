import os
os.system('clear')
import math

angulo = float(input("Digite um angulo: "))

graus = math.radians(angulo)

seno = math.sin(graus)
coseno = math.cos(graus)
tangente = math.tan(graus)
secante = 1/seno
cosecante = 1/coseno
cotangente = 1/tangente

print(f"Seno {seno}\nCosseno {coseno}\nTangente {tangente}\nSecante {secante}\nCo-secante{cosecante}\nCo-tangente {cotangente}")