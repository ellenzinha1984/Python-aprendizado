#Aprendendo listas com o Python
print('Iniciando o uso de listas, onde se armazena uma coleção de dados')
'''Para as listas, utilizamos colchetes [] para inserir os dados, sendo os dados adicionados
separados por vírgulas.
Os dados adicionados na lista recebem um índice automático, iniciando com 0, e depois é possível
fazer a varredura da lista através do dado ou do índice para acessar a informação armazenada '''

print('Foram definidos os dados a serem armazenados - meses do ano')
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
print('Imprimindo agora os dados armazenados: ', meses)
print('Acessando o mês de índice 2: ', meses[2])
print('Acessando o mês de índice 6: ', meses[6])
print('Acessando o mês de índice 10: ', meses[10])

''' Também é possível substituir valores que já estão armazenados por outros, bastando apenas informar o índice a ser
substituído, conforma feito abaixo, onde vamos substituir o mês de índice 0 (janeiro) por january.
'''
print('Novamente imprimindo os dados armazenados antes de fazer troca: ')
print(meses)
meses[0] = 'January'
print('Imprimindo após a troca de Janeiro por January: ')
print(meses)