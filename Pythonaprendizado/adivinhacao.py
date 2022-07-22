import random
#Essa biblioteca gera número aleatórios

adivinha = random.randint(0,8) #Gera números aleatórios de 0 a 8 (8 respostas possíveis aqui)

input('Me pergunte algo! ')

if adivinha == 0:
    print('Claro!')
elif adivinha == 1:
    print('Acho que sim')
elif adivinha == 2:
    print('Com certeza!')
elif adivinha == 3:
    print('Não tenho como te falar agora...')
elif adivinha == 4:
    print('Não e não!')
elif adivinha == 5:
    print('Acho que não')
elif adivinha == 6:
    print('Melhor não!')
elif adivinha == 7:
    print('Vá em frente!')
elif adivinha == 8:
    print('Não tenho uma opinião formada para isso!')