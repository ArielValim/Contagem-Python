Estou a uns meses estudando python pensando em me adiantar pois estou no segundo semestre da faculdade e sabia que viria muito python pela frente.
Hoje fiquei feliz com minha progressão nos estudos vendo uma aula onde o professor fez um exercício sobre funções usando o While e eu preferi usar o For chegando exatamente no mesmo resultado proposto. Segue abaixo minha resolução e do lado a do professor:

Agora vou explicar o exercício (ajuda muito no aprendizado de programação!):

A proposta do exercício é fazer um comando ‘Contagem( )’ onde ele mostre dois exemplos do programa fazendo a contagem de 1 até 10 pulando de 1 em 1 e também a contagem de 10 até 0 de 2 em 2. Depois ele pede ao usuário que digite o começo de uma contagem, o fim, e a razão(passo) e mostre automaticamente essa contagem descrita.

Começamos com o comando ‘def contagem( )’ que define o comando que vamos usar no programa pois no python não existe o tal. Nele definimos ‘a’ como o início da contagem, ‘b’ como o final da contagem, e ‘c’ a razão da contagem.
Na definição do comando ‘contagem( )’ primeiro fazemos um print que veremos na execução do programa, para a estética e organização do mesmo:
Seria:
def cabecalho():
    print('=-' * 20)
para o cabeçalho. 
O outro print, com a formatação das variáveis ‘a’, ‘b’ e ‘c’ ficaria: 
def contagem(a, b, c):
    cabecalho()
    print(f'Contagem de {a} até {b} de {c} em {c}')
se executarmos esses dois comandos já escritos, pedindo que o programa mostre 
contagem{1, 10, 1), veríamos o resultado abaixo:

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Contagem de 1 até 10 de 1 em 1

Process finished with exit code 0

Agora precisamos escrever os comandos que o programa vai fazer quando solicitado alguma contagem específica, que no início é de 1 a 10 pulando de 1 em 1. Primeiro destacamos que se ‘a’ é maior que ‘b’ iremos usar o comando abaixo:
if a<b:
    for c in range(a, b+1, c):
        print(c , end=' ')
    print('FIM!')

Para deixar o programa mais interessando também usamos o comando sleep( ) da biblioteca time. Com esse comando o código ficaria assim:

from time import sleep
def cabecalho():
    print('=-' * 20)

def contagem(a, b, c):
    cabecalho()
    print(f'Contagem de {a} até {b} de {c} em {c}')

    if a<b:
        for c in range(a, b+1, c):
            print(c , end=' ')
            sleep(0.5)
        print('FIM!')

contagem(1, 10, 1)

Prestando atenção no código acima vemos que a variável ‘b’ precisa estar somada a +1 pois por regra do uso de ‘for’, o último número do laço nunca é adicionado pois o início do laço sempre começa no zero.
E agora se executarmos esse código vamos ver o resultado abaixo:
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Contagem de 1 até 10 de 1 em 1
1 2 3 4 5 6 7 8 9 10 FIM!

Process finished with exit code 0

Agora adicionamos o ‘else’ que seria se a variável ‘a’ fosse menor que ‘b’:
else:
    for c in range(a, b-1, -c):
        print(c , end=' ')
        sleep(0.5)
    print('FIM!')

Neste caso, já que estamos fazendo a contagem de trás pra frente, no exercício pede de 10 até 0 pulando de 2 em 2, a variável ‘b’ terá que ser subtraída por -1 pois a contagem pode parar antes do esperado. E a variável ‘c’ tem que ser negativa pois na regra do ‘for’ só assim o laço vai ser decrescente.
Agora temos que fazer com que o programa peça para o usuário fazer sua contagem personalizada:
cabecalho()
print('Agora é sua vez de personalizar a contagem!')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
contagem(a, b, c)
cabecalho()

Se o usuário digitar que o passo é igual a zero, o programa vai dar erro então definimos um ‘if’ para que isso não aconteça:
if c == 0:
    c = 1

Se o usuário digitar um numero negativo, o programa novamente vai dar erro então definimos um ‘if’ para que isso não aconteça:
if c < 0:
    c *= -1

Esses dois últimos ‘if’ que fizemos devem estar dentro do ‘def contagem( )’ para que funcione:
def contagem(a, b, c):
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    print('=-'*20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
Nosso programa está finalizado!
Essa jornada de aprendizado está sendo bastante desafiadora, mas aprender com o Guanabara do Curso em Video está deixando a experiencia bem mais leve e divertida, o cara é bom mesmo! (hehe)
Agora vou postar mais vezes estas minhas experiencias, espero que gostem!
#Python #PythonProgramming #Coding


