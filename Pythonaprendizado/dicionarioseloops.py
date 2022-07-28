#Dicionários com loop
print('Loops com dicionário')
dicionario = {'nome':'Bela', 'espécie':'canina', 'idade':10, 'cor':'caramelo', 'raça':'SRD'}
print(dicionario)
print('Percorrendo as chaves:')
for i in dicionario:
    print(i)
print('\nPodemos imprimir as chaves e valores juntos:')
for j, k in dicionario.items():
    print(j, k)
