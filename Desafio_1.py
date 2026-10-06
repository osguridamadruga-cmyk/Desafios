# Faça um código que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
# Exemplo de Resultado: O Seu salário atual é de R$1500,00 com o aumento de 15% seu novo salário será de R$1725,00
salario = float(input("Qual é o seu salario ?"))
porcentagem = salario * 0.15
novo_salario = salario + porcentagem
print(f'O seu salario atual {salario} com o aumento de 15% seu novo salario séra de R${novo_salario}')