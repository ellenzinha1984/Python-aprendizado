#Cálculos de área em figuras geométrticas

#Círculo
raio = 4
pi = 3.14
areacirc = (pi*(raio**2))
print('A área do círculo é ', areacirc)

#Retângulo
base = 2
largura = 3
areatri = base * largura
print('A área do retângulo é ', areatri)

#Para escolhas do usuário
opcao = int(input('Cálculo de área: Digite 1 para círculo e 2 para triângulo: '))
if opcao == 1:
    raiou = float(input('Digite o raio do círculo em cm: '))
    areacircu = (pi*(raiou**2))
    print('O área do círculo é: ', areacircu, ' cm')
elif opcao == 2:
    baseu = float(input('Digite a medida da base em cm: '))
    largurau = float(input('Digite a medida da largura em cm: '))
    areatriu = baseu * largurau
    print('A área do triângulo é ', areatriu, ' cm')
else:
    print('Digite uma opção válida!')
