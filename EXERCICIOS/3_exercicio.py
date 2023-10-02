

n = int(input("Quantos casos você vai digitar: "))
    
ctd = 0
    
while ctd < n:
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    valor3 = float(input("Digite o terceiro valor: "))
        
    peso1 = 2
    peso2 = 3
    peso3 = 5

    somaPeso = peso1 + peso2 + peso3

    media = (valor1 * peso1 + valor2 * peso2 + valor3 * peso3) / (somaPeso)
        
    print(f"A média é: {media:.2f}")
        
    ctd += 1
