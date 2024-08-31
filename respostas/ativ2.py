palavra = input("Digite uma palavra: ")

cont = 0

for i in range(len(palavra)):
    if (palavra[i] == "a" or palavra[i] == "A"):
        cont += 1

print("A palavra tem", cont, "letras 'a' ou 'A'")