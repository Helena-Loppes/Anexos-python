string = input("Digite um texto: ")

texto_limpo = string.replace(" ", "")  # Remover espaços em branco

if texto_limpo == texto_limpo[::-1]:  # Comparar com a versão invertida
    print("Palíndromo")
else:
    print("Não é palíndromo")
