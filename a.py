from time import sleep
def cabecalho():
    print('=-' * 20)

def contagem(a, b, c):
    cabecalho()
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if c < 0:
        c *= -1 # Evita erro caso o usuário digite números negativos
    if c == 0:
        c = 1  # Evita erro caso o usuário digite 0
    if a < b:
        for i in range(a, b + 1, c):
            print(i, end=' ')
            sleep(0.5)
    else:
        for i in range(a, b - 1, -c):
            print(i, end=' ')
            sleep(0.5)
    print('FIM!')

# Testes:

contagem(1, 10, 1)
contagem(10, 0, 2)

# Contagem personalizada

cabecalho()
print("Agora é sua vez de personalizar a contagem!")
a = int(input("Início: "))
b = int(input("Fim: "))
c = int(input("Passo: "))
contagem(a, b, c)

