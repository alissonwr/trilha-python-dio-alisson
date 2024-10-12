frutas = ["Maçã", "Uva"]
# pessoas = []
# pessoas.list("Maçã", "Uva")

for indece, fruta in enumerate(frutas):
    print(f"{indece}: {fruta}")

numeros = [2, 3, 4, 8, 11, 15, 16, 18]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)