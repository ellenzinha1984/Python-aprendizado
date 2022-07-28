print('Fizz Buzz - números divisíveis por 3 são substituídos por Fizz, números divisíveis por 5 são substituídos por'
      'Buzz e números divididos por ambos são substituídos por Fizz Buzz')
#Ele receberá um número, fará as verificações e contagem de número a número até atingir o número digitado
def FizzBuzz(num):
    for i in range(1, num + 1):  #Inicia em 1 e faz a contagem até o número informado
        if(i % 15 == 0):
            print('FizzBuzz ', end='')  # O end='' evita que o código pule uma linha a cada número
            continue  # O continue faz com que o código volte para o início do loop para nova verificação
        elif(i % 3 == 0):
            print('Fizz ', end='')
            continue
        elif(i % 5 == 0):
            print('Buzz ', end='')
            continue

        print(i, '', end='')

FizzBuzz(int(input('Digite um número: ')))