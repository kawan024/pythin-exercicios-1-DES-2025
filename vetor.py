import random 

frutas = ["maçã", "bananas", "laranja", "uva", "manga"]
print("lista de frutas:")
for i  in range(len(frutas)):
        print(f"{i + 1} - {frutas[i]}")
posição_sorteada = random.radint(1, 5)
palpite = input("qual fruta voçê acha que esta na posição")
fruta_certa = frutas[posição_sorteada - 1]
if palpite.capitalize() == fruta_certa:
    print(" parabéns! voçê acertou!")
    print(f"A fruta na posição {posição_sorteada} era realmente {fruta_certa}.")
else:
    print(" que pena, voçê errou.")
    print(f"A fruta na posição {posição_sorteada} era {fruta_certa}.")