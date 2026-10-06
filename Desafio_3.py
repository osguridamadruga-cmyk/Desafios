# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada
# Exemplo:
# Você digitou o número : 10
# --------------- Tabuada do 10 ------------------
# 10 X 0 = 0
# 10 X 1 = 10
# E assim sucessivamente....

num = int(input('Digite um número: '))
for i in range(1,11):
 print(f'{num} x {i} = {num * i}')