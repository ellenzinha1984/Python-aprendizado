#Trabalhando listas com loop for

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
print(meses)
print('Neste caso imprimimos a lista como um todo. Agora vamos imprimir fazendo a varredura de item por item: ')
for mes in meses:
    print(mes)
print('\n\nAgora vamos mostrar o índice de cada elemento da lista com o loop for: ')
for indice in range(len(meses)): #Aqui usamos o len para ele fazer a verificação do tamanho da lista e ver cada elemento
    print(indice, meses[indice]) #Ele mostra o índice pela contagem do for e depois o item correspondente a esse índice
print('\n\nTambém podemos fazer essa listagem de índice com o comando enumerate: ')
#O comando enumerate é uma ação possíve dentro do loop for, onde ele fará a verificação sem o lenght
for i, mess in enumerate(meses):
    print(i, mess)

#Note que o índice sempre vai começar em 0, e por isso na listagem o mês de janeiro está com índice 0 e dezembro com 12.