#entrada de dados

md_exerc = float(input("Digite a média dos exercicios: "))
nt_port = float(input("Digite a nota do porfólio: "))
nt_prova = float(input("Digite a nota do porfólio: "))

#processamento
media = (md_exerc * 2 + nt_port * 3 + nt_prova * 5)/10


# saida de dados
print("A média do Aluno é: ", media)
