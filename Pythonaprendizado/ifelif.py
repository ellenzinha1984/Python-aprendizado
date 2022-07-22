#Uso de if e elif para mais de uma condição a ver verificada

print('Uso de if e elif para verificar as condições estabelecidas')
idade = int(input('Digite a idade a ser verificada: '))

if idade <=12:
    print('Você é uma criança')
elif idade > 12 and idade < 18:
    print('Você é adolescente')
elif idade >= 18 and idade < 65:
    print('Você é adulto')
elif idade >= 65:
    print('Você é idoso')

print('------------')
print('Faremos uma verificação diferente com if')

var = 'Criança / adolescente' if idade < 18 else 'Adulto'
print(var)