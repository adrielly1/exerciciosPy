
n = int(input("Digite a quantidade de números: "))
    
ctd = 0
    
while ctd < n:
    num = float(input("Digite um número: "))
        
    if num == 0:
            print("NULO")
    elif num % 2 == 0:
        if num > 0:
            print("PAR POSITIVO")
        else:
            print("PAR NEGATIVO")
    else:
        if num > 0:
            print("IMPAR POSITIVO")
        else:
            print("IMPAR NEGATIVO")
        
    ctd += 1
        

