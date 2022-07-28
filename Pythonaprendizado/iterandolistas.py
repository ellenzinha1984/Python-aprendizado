print('Iteração de duas listas, percorrendo-as simultaneamente')
#É possível fazer a varredura de duas ou mais listas ao mesmo tempo, respeitando o tamanho da menor lista.

linha = ['Centro', 'Jardins', 'Tatuapé', 'Butantã', 'Ipiranga', 'Tucuruvi']
numero = ['30', '200', '26', '90']
print('\nVamos imprimir as linhas e horários. Temos menos horários que linhas nas listas. Como se comporta?')
for l, n in zip(linha, numero): #zip faz o desempacotamento das listas ao mesmo tempo
    print(l, n)

