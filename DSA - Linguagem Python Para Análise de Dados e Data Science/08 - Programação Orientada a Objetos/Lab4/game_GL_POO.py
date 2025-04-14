import random

# Classe base para exibição
class Exibidor:
    def mostrar_palavra(self, palavra_secreta, letras_adivinhadas):
        raise NotImplementedError

    def mostrar_erro(self, tentativas_restantes):
        raise NotImplementedError

    def mostrar_vitoria(self):
        raise NotImplementedError

    def mostrar_derrota(self, palavra_secreta):
        raise NotImplementedError


# Exibição no terminal com arte
class ExibidorTerminal(Exibidor):
    def __init__(self):
        self.stages = [
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

    def mostrar_palavra(self, palavra_secreta, letras_adivinhadas):
        exibicao = " ".join([letra if letra in letras_adivinhadas else "_" for letra in palavra_secreta])
        print(f"\nPalavra: {exibicao}")

    def mostrar_erro(self, tentativas_restantes):
        print(self.stages[tentativas_restantes])

    def mostrar_vitoria(self):
        print("🎉 Parabéns! Você venceu!")

    def mostrar_derrota(self, palavra_secreta):
        print(f"💀 Você perdeu. A palavra era: '{palavra_secreta}'")


# Classe principal do jogo
class JogoDaForca:
    def __init__(self, palavras, exibidor, tentativas_max=6):
        self.palavras = palavras
        self.exibidor = exibidor
        self.tentativas_max = tentativas_max

    def jogar(self):
        palavra = random.choice(self.palavras).upper()
        letras_adivinhadas = set()
        tentativas_restantes = self.tentativas_max

        print("\n🕹️ Bem-vindo ao jogo da Forca!")

        while tentativas_restantes > 0:
            self.exibidor.mostrar_palavra(palavra, letras_adivinhadas)
            self.exibidor.mostrar_erro(tentativas_restantes)

            letra = input("Digite uma letra: ").upper()

            if not letra.isalpha() or len(letra) != 1:
                print("⚠️ Digite apenas uma letra válida.")
                continue

            if letra in letras_adivinhadas:
                print("🔁 Você já tentou essa letra.")
                continue

            letras_adivinhadas.add(letra)

            if letra not in palavra:
                tentativas_restantes -= 1
                print(f"❌ Letra incorreta. Tentativas restantes: {tentativas_restantes}")
            else:
                print("✅ Boa! Letra correta!")

            if all(l in letras_adivinhadas for l in palavra):
                self.exibidor.mostrar_palavra(palavra, letras_adivinhadas)
                self.exibidor.mostrar_vitoria()
                return

        self.exibidor.mostrar_erro(tentativas_restantes)
        self.exibidor.mostrar_derrota(palavra)


# Execução
if __name__ == "__main__":
    palavras = ["banana", "computador", "python", "mercado", "engenheiro"]
    exibidor = ExibidorTerminal()
    jogo = JogoDaForca(palavras, exibidor)
    jogo.jogar()
