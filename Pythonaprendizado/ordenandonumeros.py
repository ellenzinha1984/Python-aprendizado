#Ordenando números de uma lista
numeros = [1, 5, 8, 9, 7, 10, 4, 6, 30, 100, 50, 12, 22]
desordena = True
print('Números: ', numeros)
while desordena: #Enquanto ele não terminar de ordenar, vamos colocar o desordena como false
    desordena = False
    for num in range(len(numeros)-1): #Como não teoricamente não sabemos o número de elementos, usamos o len(numeros)-1
        if numeros[num] > numeros[num+1]:
            numeros[num], numeros[num+1] = numeros [num+1], numeros[num]
            desordena = True
    print('Números ordenados - crescente: ',numeros)
'''Para entender o processo, deixei o print aqui para ir repetindo até acabar, pois nesse contexto o algoritmo entende
que existem dois elementos adjacentes fora da ordem quando uma sequência está desordenada. Ele vai fazendo a varredura
da lista e troca a posição dos itens fora de ordem, fazendo as comparações até que todos estejam dentro da ordem
crescente. É Possível fazer o contrário também, apenas mudando os sinais e ordem dos itens a serem trocados'''
print('\nNúmeros em ordem decrescente: ')
desordenado = True
while desordenado:
    desordenado = False
    for num1 in range(len(numeros)-1):
        if numeros[num1] < numeros[num1+1]:
            numeros[num1+1], numeros[num1] = numeros[num1], numeros[num1+1]
            #Aqui é o contrário do crescente, pois se num1+1 for maior, ele deve vir primeiro
            desordenado = True
    print('Números ordenados - descrescente: ', numeros)

#Como eu usei o mesmo código e lista para fazer crescente e decrescente, ele fará mais vezes a repetição no decrescente
