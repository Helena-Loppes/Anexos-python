notas = []
n = int(input("entre o número de notas: "))
for i in range(n):
    dado = float(input("Entre com a nota" + str(i) + ": "))
    notas.append(dado)
print(notas)