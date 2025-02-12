texto = input("Digite um texto: ")
pontuacao = [".", ",", ":", ";", "!", "?"]

#remove os sinais de pontuação
for p in pontuacao:
    texto = texto.replace(p," ")

#split devolve lista com palavras coo itens
numero_palavra = len(texto)
print("Número de palavras;", numero_palavra) 