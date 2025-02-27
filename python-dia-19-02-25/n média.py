n = int(input("Quantas notas você deseja inserir? "))
notas = []

for i in range(n):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

print("Notas inseridas:", notas)

media = sum(notas) / len(notas)

print(f"A média das notas é: {media:.2f}")
