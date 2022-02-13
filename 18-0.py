def imprime_retangulo_vazado(l,a):
    pl = 0
    pa = 0
    while pa < a:
        while pl < l:
            if pa == 0 or pa == (a-1):
                print("#",end="")
            else:
                if pl == 0 or pl == (l-1):
                    print("#",end="")
                else:
                    print(" ",end="")
            pl+=1
        print()
        pl = 0
        pa+=1
            
def main():
    enterMsg1 = "digite a largura: "
    enterMsg2 = "digite a altura: "
    while True:
         try:
            l = int(input(enterMsg1))
            a = int(input(enterMsg2))
            if l > 0 and a > 0:
                break
            else:
                print("\nAtenção: 'n' e 'm' devem ser inteiros maiores que 0")
                continue
         except:
            print("\nPor favor, insira somente números inteiros maiores que 0!")
    
    imprime_retangulo_vazado(l,a)

main()
