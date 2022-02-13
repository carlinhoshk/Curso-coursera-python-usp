
print("Digite uma sequencia de valores que termina por zero. ")

soma = 0
valor = 1

while valor != 0:
	valor = int(input("Digte um valor para somar: ")) 
	soma = soma + valor
print("A soma dos valores digitados é: ", soma)