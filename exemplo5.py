#entrada de dados

md_exerc = float(input("Digite a média dos exercicios: "))
nt_port = float(input("Digite a nota do porfólio: "))
nt_prova = float(input("Digite a nota do porfólio: "))

#processamento
media = (md_exerc * 2 + nt_port * 3 + nt_prova * 5)/10


# saida de dados
#estrutura de condição if/else

print("A média do Aluno é: ", media)
if (media >=6):
    print("Situação do Aluno: Aprovado")
else:
    if (media < 2):
        print("Situação do Aluno: Dependência")
    else:
        print("Situação do Aluno: Recuperação")
