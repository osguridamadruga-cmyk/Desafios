# Na mesma linha dos exercicios anteriores crie uma função chamada pode_ver_filme que recebe a idade e a classificação indicativa do filme
# classificacao: 'L' (Livre), 'Maior de 12', 'Maior de 14', 'Maior 16', 'Maior 18'

#Exemplo:
# idade = 10
# classificacao = 'Maior de 12'
# resposta = "Não pode assitir o filme"

def pode_ver_filme(idade, classificacao):
    if classificacao == "L":
        resposta = "Pode assistir ao filme"

    elif classificacao == "Maior de 12":
        if idade >= 12:
            resposta = "Pode assistir ao filme"
        else:
            resposta = "Não pode assistir ao filme"

    elif classificacao == "Maior de 14":
        if idade >= 14:
            resposta = "Pode assistir ao filme"
        else:
            resposta = "Não pode assistir ao filme"

    elif classificacao == "Maior de 16":
        if idade >= 16:
            resposta = "Pode assistir ao filme"
        else:
            resposta = "Não pode assistir ao filme"

    else:
        if idade >= 18:
            resposta = "Pode assistir ao filme"
        else:
            resposta = "Não pode assistir ao filme"

    return resposta


idade = 10
classificacao = "Maior de 12"

print(pode_ver_filme(idade, classificacao))