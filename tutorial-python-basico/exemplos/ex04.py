continua = True

while continua:
    pergunta = input('Deseja continuar? ')

    if pergunta == 'sim':
        continua = True
        print('Então continua')
    elif pergunta == 'não':
        continua = False
        print('Chega')
    else:
        continua = True
        print('Que?!?')