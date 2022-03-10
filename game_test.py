
#Bibliotecas ultilizadas
import time
import random

# contadores de placar
p1scorec=0
p1vida=0
p1passos=0
p2scorec=0
p2vida=0
p2passos=0

placarP2=[]
placarP1=[]

# variavel numero de jogadores

njogs=0

# atribuindo dados a uma lista

dados =['CPCTPC','CPCTPC','CPCTPC','CPCTPC','CPCTPC','CPCTPC','TPCTPC','TPCTPC','TPCTPC','TPCTPC','TPTCPT','TPTCPT','TPTCPT']

# Funcoes para otimizacao de prints

def jogadorMorreu():
    print('-='*30)
    print('--------------Suas vidas para esta rodada ja acabaram------------------')
    print('-='*30)
    print('``````````````FIM DO SEU TURNO```````````````')


def rodadap1():
    print('--'*40)
    print('{} sua rodada: \n {} Cerebros \n {} vitimas fugiram \n {} Vidas perdidas '.format(p1, p1scorec, p1passos,
                                                                                             p1vida))
    print('--'*40)


def rodadap2():
    print('--' * 40)
    print('{} sua rodada: \n {} Cerebros \n {} vitimas fugiram \n {} Vidas perdidas '.format(p2, p2scorec, p2passos,
                                                                                             p2vida))
    print('--' * 40)


def sorteiodadocerebro():
    print('--------------------------')
    print('  C = Voce comeu um cérebro')
    print('--------------------------')


def sorteiodadopasso():
    print('--------------------------')
    print('  P = Opsss, vitima fugiu')
    print('--------------------------')


def sorteiodadovida():
    print('--------------------------')
    print('  T = Voce levou um tiro')
    print('--------------------------')


def jogadap1():
    c = 0
    p = 0
    v = 0
    jogadap1 = str(input('{} é a sua vez , pressione enter para jogar os dados: '.format(p1)))
    turno = True  # enquanto turno Verdadeiro, jogador continua a jogar
    while turno == True:  # enquanto for sim vai repetir a jogada do jogador 1
        for i in range(0, 3):
            dado_jog = random.choice(dados)
            letra_dado = random.choice(dado_jog)
            if letra_dado == 'C':
                sorteiodadocerebro()
                c += 1

            elif letra_dado == 'P':
                sorteiodadopasso()
                p += 1
            else:
                sorteiodadovida()
                v += 1
            if v > 2:
                jogadorMorreu()
                break
        continua1 = str(input('Deseja continuar?    s / n : '))
        if continua1 == 's':
            turno = True
        else:
            turno = False

        return (c,p,v)

    print(c,p,v)

# INICIO DO GAME

print('-----------VOCE ESTA NO ZOMBIE DICE----------------')
#print('regras do jogo.....') implementar

while njogs < 2: #Bloqueio para menos de 2 jogadores
    njogs=int(input('quantos jogadores vão jogar: '))
    if njogs < 2:
        print('precisamos de no minimo 2 jogadores para iniciar o nosso game')
p1=str(input('digite seu zombie name player 1 : '))
print('---------------------------------------------------')
p2=str(input('digite seu zombie name player 2 : '))

#incio da rodada 1

jogadap1()

time.sleep(1)          #placar da rodada informado
rodadap1()

#inicio jogada player 2

jogadap2 = str(input('{} agora e a sua vez pressione enter para jogar os dados : '.format(p2)))
turno=True
while turno == True: # enquanto for sim vai repetir a jogada do jogador 2
    for i in range(0, 3):
        dado_jog = random.choice(dados)
        letra_dado = random.choice(dado_jog)
        if letra_dado == 'C':
            sorteiodadocerebro()
            p2scorec += 1
        elif letra_dado == 'P':
            sorteiodadopasso()
            p2passos += 1
        else:
            sorteiodadovida()
            p2vida += 1
            if p2vida > 2:
                jogadorMorreu()
                break
    continua1 = str(input('Deseja continuar?    s / n : '))
    if continua1 == 's':
        turno=True
    else:
        turno=False
time.sleep(1)
rodadap2() #mostra rodada p2








time.sleep(2)

#Resultado final, quem comer 13 cerebros vence

if p1scorec > 12 :
    print('{}, VOCE VENCEU , foi o zombie mais destemido e conseguiu comer {} cerebros '.format(p1, p1scorec))
elif p2scorec > 12:
    print('{} , VOCE VENCEU , foi o zombie mais destemido e conseguiu comer {} cerebros'.format(p2, p2scorec))


#Resultado final, quem comeu mais cerebros vence

if p1scorec > p2scorec:
    time.sleep(1)
    print('{}, VOCE VENCEU , foi o zombie mais destemido e conseguiu comer {} cerebros '.format(p1,p1scorec))
else:
    time.sleep(1)
    print('{} , VOCE VENCEU , foi o zombie mais destemido e conseguiu comer {} cerebros'.format(p2,p2scorec))