

decrescente = True
anterior = int(input("Digite o primeiro numero da sequencia"))

valor = 1

while valor !=0 and decrescente:
	valor = int(input("Digte proximos numeros da sequencia: "))
	if valor > anterior:
		decrescente = False
	anterior = valor
if decrescente:
	print("A sequencia está em ordem descrecente")
else:
	print("A sequencia não está em descrecente")			