lista1 = []
lista2 = []

print("Digite os números:")
for i in range(5):
    n = int(input(f"Elemento {i+1} da lista 1: "))
    lista1.append(n)

print("Digite os números da segunda lista:")
for i in range(5):
    n = int(input(f"Elemento {i+1} da lista 2: "))
    lista2.append(n)

comum = [elem for elem in lista2 if elem in lista1]

if comum:
    print(f"{comum}")
else:
    print("Não tem")
