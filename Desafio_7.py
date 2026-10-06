# Crie uma função que calcule o valor da gorjeta de um garçom, baseada na qualidade do serviço
# qualidade_servico: 'ruim', 'medio', 'bom', 'excelente'

# A função deve pedir o valor da conta e a qualidade do serviço
# Se a qualidade for ruim a gorjeta é 0
# Se a qualidade for media a gorjeta é %2.5 do valor da conta
#Se a qualidade for bom a gorjeta é %4 do valor da conta
#Se a qualidade for excelente a gorjeta é %5 do valor da conta

#Exemplo:
# valor_conta = 100
# qualidade_servico = 'excelente'
# o valor da gorjeta é de R$ 5,00


def calcular_gorjeta(qualidade_do_serviço, total_da_conta):
    if qualidade_do_serviço == "ruim":
        gorjeta = 0
    elif qualidade_do_serviço == 'media':
        gorjeta = total_da_conta * 0.025

    elif qualidade_do_serviço == 'boa':
        gorjeta = total_da_conta * 0.04

    else  :
        gorjeta = total_da_conta * 0.05
    return gorjeta

valor_conta = 100
qualidade_servico = "excelente"

gorjeta = calcular_gorjeta(qualidade_servico, valor_conta)

print(f"Valor da conta: R$ {valor_conta:.2f}")
print(f"Qualidade do serviço: {qualidade_servico}")
print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
print(f"Total a pagar: R$ {valor_conta + gorjeta:.2f}")
    
