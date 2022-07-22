#Loop com while e continue

print('Demonstrando loop infinito com while, continue e break')
print('Por exemplo, verificação de usuário e senha')

'''
Loop só será encerrado quando a condição estabelecida for alcançada.
Vai ser pedido o username, que tem que ser 'admin' para ele prosseguir com as verificações.
Se o username for diferente de 'admin' ele solicitará novamente o dado (verificado pelo if).
O continue leva ao início do loop novamente, sem passar pelo resto, até o username estar correto.
Se o for digitado admin como username, ele continua a verificação da senha, que seguirá o mesmo padrão que o username.
Posso colocar um while dentro de outro, para garantir que serão feitas as duas verificações até que seja atendido
o esperado.
'''

while True:
    username = input('Digite o username: ')
    if username != 'admin':
        print('Usuário incorreto! Digite novamente!')
        continue
    elif username == 'admin':
        while True:
            password = input('Digite a senha: ')
            if password != 'admin':
                print('Senha incorreta! Digite novamente!')
                continue
            elif password == 'admin':
                print('Seja bem-vindo, {}'. format(username))
                break
    break
