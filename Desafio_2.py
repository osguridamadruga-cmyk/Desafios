# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor:
# Exemplo:
# Você digitou o número : 10
# O sucessor dele é o número : 11
# O antecessor dele é o número : 9
num = float(input('Digite um número: '))
antecessor = num-1
sucessor = num+1
print(f' qual é o antecessor do numero {num}? é o {antecessor}') 
print(f'print qual é o sucessor do numero  {num}? é o {sucessor}')
