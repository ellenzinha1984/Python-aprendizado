#Trabalhando loops com for

'''
Aqui será utilizado o comando for ...in range.
Nele é possível fazer iterações como o if, porém percorrendo com comandos já definidos, facilitando o trabalho
e otimizando o código. Comando:
for i in range (1, 21, 1): - neste caso ele fará a contagem de 1 a 20, de 1 em 1. O número de limite (do meio) sempre
considerará um número a menos, ele não é incluído na iteração.
for i in range (1, 21, 2): - aqui ele fará a contagem de 1 a 20 mas dessa vez de dois em dois.
'''
print('Vamos ver a contagem utilizando o for i in range na prática. Começando com a contagem de 1 a 20 de 1 em 1:')
for i in range(1, 21, 1):
    print(i)
print('\n\nAgora faremos a mesma contagem de 2 em 2: ')
for y in range(1, 21, 2):
    print(y)