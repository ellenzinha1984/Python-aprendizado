#Código para embaralhar as letras de uma palavra

def alphabetsoup(word):
    return "".join(sorted(word))

print(alphabetsoup(input('Digite a palavra a ser embaralhada: ')))