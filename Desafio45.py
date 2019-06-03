import random
resposta = int(input('-1- Pedra, -2- Papel , -3- Tesoura'))
compresp = [1 , 3]
escolhacomp= random.choice(compresp)
pedra = resposta == 1
papel = resposta == 2
tesoura = resposta == 3

if resposta == escolhacomp:
    print('O jogo empatou, você escolheu {}, e o computador escolheu, {}'.format(escolhacomp,compresp))
elif resposta == pedra and escolhacomp == tesoura:
    print('Voce ganhou você escolheu {}, e o computador, {}'.format(resposta, escolhacomp))
elif resposta == tesoura and escolhacomp == papel:
    print('Voce ganhou, voce escolheu {} , e o computador, {}'.format(resposta, escolhacomp))
elif resposta == papel and escolhacomp == pedra:
    print('Você ganhou, você escolheu {}, e o computador, {}'.format(resposta, compresp))
else:
    print('Você perdeu , você escolheu {}, e o computador, {}'.format(resposta,escolhacomp))
