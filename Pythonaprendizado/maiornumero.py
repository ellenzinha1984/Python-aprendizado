#Mostrando o maior número de uma lista
numeros = [1, 5, 8, 9, 7, 10, 4, 6, 30, 100, 50, 12, 22]
maiornum = numeros[0] #Preciso estabelecer um valor inicial para comparativo
for num in numeros: #Varredura da lista para comparar
    if num > maiornum: #Compara cada valor com o valor armazenado em maiornumn. Se for maior, ele faz a substituição
        maiornum = num
print('Números: ',numeros)
print('O maior número da lista é: ', maiornum)

#Também é possível usar a opção max(numeros) para isso
print('\nUsando a opção max(numeros):')
print(max(numeros))