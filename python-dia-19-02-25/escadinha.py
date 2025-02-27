numero = int(input("Digite um número: ")) # Lê o valor de "numero"

for i in range(1, numero + 1): # Imprime "numero" linhas e adiciona mais um conforme a escadinha 
    linha = " " .join(str(x) for x in range(1, i + 1))# Cria uma linha com os números de 1 até i:que é o total do numero, no caso "numero"
    print(linha) #imprime oque é pedido no código
