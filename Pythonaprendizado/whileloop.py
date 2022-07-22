#Exemplos de loop com o comando while - enquanto a condição for verdadeira ele executa o bloco

x = 0
while x <= 20:
    print('Vou executar até que o x seja 20. Estou em: ', x)
    x += 1

#Novo loop agora infinito e com break
print('\n\n\n')
print('Agora o loop será infinito até que se atenda o requisito')

while True:
    resposta = int(input('Quanto é 2 + 2? '))
    if resposta == 4:
        print('Correto! Encerrando o programa...')
        break #O break faz a interrupção do loop
    else:
        print('Digite a resposta correta! Quanto é 2 + 2? ')