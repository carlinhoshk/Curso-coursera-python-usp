meuCartão = int(input("Digte o numero do cartão"))

cartãoLido = 1
encontreiMeuCartãoNaLista = False

while cartãoLido !=0:
	cartãoLido = int(input("Digite proximos numeros de outro cartão"))
	if cartãoLido == meuCartão:
		encontreiMeuCartãoNaLista = True
if encontreiMeuCartãoNaLista:
	print("encontrei meu cartão")
else:
	print("ainda sem encontrar")			