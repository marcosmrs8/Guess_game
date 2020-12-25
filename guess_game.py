import random


def guess():
    count = 0
    guess_pc = random.randint(1, 10)
    print('Tente adivinhar o numero de 1 a 10: ')
    while True:
        resp = int(input('try again: '))

        if count == 4:
            print('Atingiu o máximo de tentativas! ;c')
            return False
        if guess_pc == resp:
            print('Acertou miseravi!')
            return False
        elif guess_pc > resp:
            count += 1
            print('Errou! é um numero maior. Você tem mais {} tentativas'.format(5 - count))
        elif guess_pc < resp:
            count += 1
            print('Errou! é um número menor. Você tem mais {} tentativas'.format(5 - count))
        else:
            print('Isso não é um número amigão! :D')




guess()