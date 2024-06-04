import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "desenvolvimento", "software", "hardware"]

# Função para escolher uma palavra aleatória
def escolher_palavra():
    return random.choice(palavras)

# Função principal do jogo
def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ["_"] * len(palavra)
    tentativas = 6
    letras_erradas = []

    print("Bem-vindo ao jogo da forca!")
    print("Adivinhe a palavra:")
    print(" ".join(palavra_oculta))

    while tentativas > 0 and "_" in palavra_oculta:
        print(f"Tentativas restantes: {tentativas}")
        print("Letras erradas:", " ".join(letras_erradas))
        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        if letra in letras_erradas or letra in palavra_oculta:
            print("Você já tentou essa letra.")
            continue

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
            print(" ".join(palavra_oculta))
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print("Letra incorreta.")

    if "_" not in palavra_oculta:
        print("Parabéns, você ganhou!")
    else:
        print(f"Você perdeu. A palavra era '{palavra}'.")

# Executa o jogo
if __name__ == "__main__":
    jogar()
