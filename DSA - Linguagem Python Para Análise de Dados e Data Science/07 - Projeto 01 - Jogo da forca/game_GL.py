import random

# Função que desenha a forca na tela
def display_hangman(chances):
    stages = [
        r"""
           ╔══════════════╗
           ║              ║
           ║              😵
           ║             \|/
           ║              |
           ║             / \
         ══╩═══       FORCA FINAL
        """,
        r"""
           ╔══════════════╗
           ║              ║
           ║              😧
           ║             \|/
           ║              |
           ║             / 
         ══╩═══       FORCA 5
        """,
        r"""
           ╔══════════════╗
           ║              ║
           ║              😨
           ║             \|/
           ║              |
           ║              
         ══╩═══       FORCA 4
        """,
        r"""
           ╔══════════════╗
           ║              ║
           ║              😟
           ║             \|
           ║              |
           ║              
         ══╩═══       FORCA 3
        """,
        r"""
           ╔══════════════╗
           ║              ║
           ║              😐
           ║              |
           ║              |
           ║              
         ══╩═══       FORCA 2
        """,
        r"""
           ╔══════════════╗
           ║              ║
           ║              🙂
           ║              
           ║              
           ║              
         ══╩═══       FORCA 1
        """,
        r"""
           ╔══════════════╗
           ║              ║
           ║              
           ║              
           ║              
           ║              
         ══╩═══       FORCA INICIAL
        """
    ]
    return stages[chances]

# 1. Lista de palavras possíveis
palavras = ['python', 'engenheiro', 'dados', 'forca', 'script', 'cloud', 'pipeline']

# 2. Escolher uma palavra aleatória
palavra_secreta = random.choice(palavras)

# 3. Letras já adivinhadas
letras_adivinhadas = []

# 4. Tentativas
tentativas_max = 6
tentativas_restantes = tentativas_max

print("🔤 Bem-vindo ao Jogo da Forca!")
print("Dica: a palavra tem", len(palavra_secreta), "letras.")

# 5. Loop principal
while tentativas_restantes > 0:
    # a. Mostrar estado atual da palavra
    exibicao = ''
    for letra in palavra_secreta:
        exibicao += letra + ' ' if letra in letras_adivinhadas else '_ '

    print("\nPalavra:", exibicao.strip())

    # f. Verificar vitória
    if all(letra in letras_adivinhadas for letra in palavra_secreta):
        print("\n🎉 Você venceu! A palavra era:", palavra_secreta)
        break

    # b. Input do jogador
    chute = input("Digite uma letra: ").lower()

    # Validações
    if len(chute) != 1 or not chute.isalpha():
        print("⚠️ Digite apenas UMA letra.")
        continue
    if chute in letras_adivinhadas:
        print("🔁 Você já tentou essa letra.")
        continue

    # c. Letra correta
    if chute in palavra_secreta:
        letras_adivinhadas.append(chute)
        print("✅ Letra correta!")
    else:
        # e. Letra errada
        tentativas_restantes -= 1
        print(f"❌ Letra incorreta. Tentativas restantes: {tentativas_restantes}")
        print(display_hangman(tentativas_restantes))
        
# h. Derrota
if tentativas_restantes == 0:
    print(display_hangman(6))
    print("\n💀 Você perdeu. A palavra era:", palavra_secreta)
