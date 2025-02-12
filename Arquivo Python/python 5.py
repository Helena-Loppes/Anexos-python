def adjacente(numero):
    """
    Verifica se o número contém dois dígitos adjacentes iguais.
    """
    numero = str(numero)
    for i in range(len(numero) - 1):
        if numero[i] == numero[i + 1]:
            return True
    return False

def main():
    """
    Lê um único número inteiro e verifica
    se possui dígitos adjacentes iguais.
    """
    n = int(input("Digite a quantidade de dígitos do número: "))
    numero = input(f"Digite um número inteiro com {n} dígitos: ")
    
    if len(numero) != n:
        print(f"Erro: O número precisa ter exatamente {n} dígitos.")
        return

    if adjacente(numero):
        print("Sim, o número tem dois dígitos adjacentes iguais.")
    else:
        print("Não, o número não tem dois dígitos adjacentes iguais.")
        
if __name__ == "__main__":
    main()
