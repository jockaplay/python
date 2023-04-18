import os, random

def clear():
    os.system("cls")

def acertou(sequencia, nova_string):
    corrento = ''
    # trasformar lista em string
    for i in sequencia:
        corrento += str(i)
    # o que digitou é igual à sequencia?
    if nova_string == corrento:
        return True
    else:
        return False

def iniciar_jogo():
    pontos = 0
    sequencia = []
    clear()
    while True:
        sequencia.append(random.randint(0,4))
        clear()
        print(f'\n--O último número é: {sequencia[-1]} --\n')
        if acertou(sequencia, input()):
            pontos += 1
        else:
            clear()
            print(f"\nVocê errou!\n")
            break

if __name__ == "__main__":
    iniciar_jogo()