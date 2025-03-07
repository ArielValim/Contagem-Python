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


O MESMO TEXTO MAS COM 2885 CARACTERES

Estou há alguns meses estudando Python para me adiantar, pois estou no segundo semestre da faculdade e sabia que teria muito Python pela frente. Hoje fiquei satisfeito com minha progressão nos estudos ao assistir uma aula em que o professor resolveu um exercício sobre funções utilizando o while, enquanto preferi usar o for e cheguei ao mesmo resultado. Abaixo, apresento minha resolução e a do professor.
O exercício propõe a criação do comando contagem(), que deve exibir dois exemplos: uma contagem de 1 até 10, pulando de 1 em 1, e outra de 10 até 0, pulando de 2 em 2. Além disso, o programa deve permitir que o usuário defina o início, o fim e o passo da contagem.
Iniciamos com o comando def contagem(), que define a função necessária para o programa, já que o Python não possui um comando específico para isso. Nessa função, definimos ‘a’ como o início da contagem, ‘b’ como o final e ‘c’ como o passo. Para uma melhor organização, criamos uma função separada para exibir um cabeçalho:
def cabecalho(): print('=-' * 20)
Dentro da função contagem(), inserimos um print para exibir as informações da contagem:
def contagem(a, b, c): cabecalho() print(f'Contagem de {a} até {b} de {c} em {c}')
Se executarmos esse código chamando contagem(1, 10, 1), veremos a seguinte saída:
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Contagem de 1 até 10 de 1 em 1
Agora, precisamos implementar a lógica da contagem. Se ‘a’ for menor que ‘b’, utilizamos:
if a < b: for c in range(a, b+1, c): print(c, end=' ') print('FIM!')
Para tornar o programa mais interessante, utilizamos o comando sleep() da biblioteca time. Assim, o código fica:
from time import sleep
def cabecalho(): print('=-' * 20)
def contagem(a, b, c): cabecalho() print(f'Contagem de {a} até {b} de {c} em {c}')

if a < b:
    for c in range(a, b+1, c):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')
contagem(1, 10, 1)
Agora, se ‘a’ for maior que ‘b’, utilizamos o else:
else: for c in range(a, b-1, -c): print(c, end=' ') sleep(0.5) print('FIM!')
Como a contagem está em ordem decrescente, subtraímos ‘b’ por -1 para evitar que pare antes do esperado. Além disso, ‘c’ deve ser negativo para garantir que o laço funcione corretamente.
Agora, o programa deve permitir que o usuário personalize a contagem:
cabecalho() print('Agora é sua vez de personalizar a contagem!') a = int(input('Início: ')) b = int(input('Fim: ')) c = int(input('Passo: ')) contagem(a, b, c) cabecalho()
Caso o usuário informe um passo igual a zero, o programa apresentará erro. Para evitar isso, adicionamos:
if c == 0: c = 1
Se o usuário informar um número negativo, o programa também pode falhar. Então, adicionamos:
if c < 0: c *= -1
Essas verificações devem estar dentro da função contagem():
def contagem(a, b, c): if c == 0: c = 1 if c < 0: c *= -1 print('=-'*20) print(f'Contagem de {a} até {b} de {c} em {c}')
Nosso programa está finalizado. Essa jornada de aprendizado tem sido desafiadora, mas aprender com o Guanabara do Curso em Vídeo torna a experiência mais leve e interessante. Agora pretendo compartilhar mais sobre meu aprendizado.

O MESMO TEXTO MAS EM 3000 CARACTERES

Estou há alguns meses estudando Python para me adiantar, pois estou no segundo semestre da faculdade e sabia que teria muito Python pela frente. Hoje fiquei satisfeito com minha progressão nos estudos ao assistir uma aula em que o professor resolveu um exercício sobre funções utilizando o while, enquanto preferi usar o for e cheguei ao mesmo resultado. Abaixo, apresento minha resolução e a do professor.
O exercício propõe a criação do comando contagem(), que deve exibir dois exemplos: uma contagem de 1 até 10, pulando de 1 em 1, e outra de 10 até 0, pulando de 2 em 2. Além disso, o programa deve permitir que o usuário defina o início, o fim e o passo da contagem.
Iniciamos com o comando def contagem(), que define a função necessária para o programa, já que o Python não possui um comando específico para isso. Nessa função, definimos ‘a’ como o início da contagem, ‘b’ como o final e ‘c’ como o passo. Para uma melhor organização, criamos uma função separada para exibir um cabeçalho:
def cabecalho(): print('=-' * 20)
Dentro da função contagem(), inserimos um print para exibir as informações da contagem:
def contagem(a, b, c): cabecalho() print(f'Contagem de {a} até {b} de {c} em {c}')
Se executarmos esse código chamando contagem(1, 10, 1), veremos a seguinte saída:
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Contagem de 1 até 10 de 1 em 1
Agora, precisamos implementar a lógica da contagem. Se ‘a’ for menor que ‘b’, utilizamos:
if a < b: for c in range(a, b+1, c): print(c, end=' ') print('FIM!')
Para tornar o programa mais interessante, utilizamos o comando sleep() da biblioteca time. Assim, o código fica:
from time import sleep
def cabecalho(): print('=-' * 20)
def contagem(a, b, c): cabecalho() print(f'Contagem de {a} até {b} de {c} em {c}')
if a < b:
    for c in range(a, b+1, c):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')
contagem(1, 10, 1)
Agora, se ‘a’ for maior que ‘b’, utilizamos o else:
else: for c in range(a, b-1, -c): print(c, end=' ') sleep(0.5) print('FIM!')
Como a contagem está em ordem decrescente, subtraímos ‘b’ por -1 para evitar que pare antes do esperado. Além disso, ‘c’ deve ser negativo para garantir que o laço funcione corretamente.
Agora, o programa deve permitir que o usuário personalize a contagem:
cabecalho() print('Agora é sua vez de personalizar a contagem!') a = int(input('Início: ')) b = int(input('Fim: ')) c = int(input('Passo: ')) contagem(a, b, c) cabecalho()
Caso o usuário informe um passo igual a zero, o programa apresentará erro. Para evitar isso, adicionamos:
if c == 0: c = 1
Se o usuário informar um número negativo, o programa também pode falhar. Então, adicionamos:
if c < 0: c *= -1
Essas verificações devem estar dentro da função contagem():
def contagem(a, b, c): if c == 0: c = 1 if c < 0: c *= -1 print('=-'*20) print(f'Contagem de {a} até {b} de {c} em {c}')
Nosso programa está finalizado. Essa jornada de aprendizado tem sido desafiadora, mas aprender com o Guanabara do Curso em Vídeo torna a experiência mais leve e interessante. A cada novo exercício, percebo minha evolução e fico ainda mais motivado a continuar. Programação exige paciência e prática, e compartilhar meu aprendizado tem sido uma excelente maneira de fixar o conhecimento. Agora pretendo postar mais sobre meu progresso e minhas descobertas ao longo do caminho.

