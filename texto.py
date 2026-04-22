nome_completo = "Matheus Henrique Gama OSório"
idade = 23
altura = 1.86
peso = 110
imc = peso / (altura ** 2)

#Essas são formas de imprimir variáveis em Python, usando formatação de string
#%s para string, %d para inteiro, %.2f para float com 2 casas decimais
#essa versão é útil para evitar tipos incompatíveis, pois o Python converte automaticamente o tipo da variável para o formato especificado
print("Nome: %s" %nome_completo, " / Idade: %d" %idade, " / Altura: %.2f" %altura, " / Peso: %.2f" %peso)
print("Nome: ", nome_completo, " / Idade: ", idade, " / Altura: ", altura, " / Peso: ", peso)

#esse é o método f-string, que é mais moderno e recomendado pra formatar strings 
#apesar disso o método com %s é o mais seguro na questão de tratamento de dados
print(f"Nome: {nome_completo} / Idade: {idade} / Altura: {altura:.2f} / Peso: {peso:.2f}")

#método mais antigo, mas ainda válido, para formatar strings
print("Nome: {} {}".format(nome_completo, idade))