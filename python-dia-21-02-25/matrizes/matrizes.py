def leMatriz(dimensao):
    mat = [[] for i in range(dimensao)]# Inicializa a matriz como uma lista de listas vazias, com 'dimensao' linhas
    for i in range(dimensao):# Loop para percorrer todas as linhas da matriz
        for j in range(dimensao):# Loop para percorrer todas as colunas da matriz
            # Solicita ao usuário que insira um número para a posição (i+1, j+1) da matriz
            num = int(input("(" + str(i+1) + "," + str(j+1) + "): ")) # A fórmula "(+-str(i+1)+","+str(j+1)+")" é usada para formatar o texto de forma legível
            mat[i].append(num)# Adiciona o número inserido pelo usuário na linha 'i' da matriz

    return mat# Retorna a matriz preenchida
print(leMatriz(3))
