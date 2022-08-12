#Aumento de salário utilizando funções

salariobase = 2000
salarioanalista = 2500
salarioestagio = 1000
salariolider = 5000
valreajuste = 0.04

#função para o reajuste
def reajusteSal(salario, base, reajuste):
    if salario > base:
        salario += salario * reajuste
        print(f'Novo salário reajustado: {salario}')
        return salario
    else:
        print('Seu salário não foi reajustado')


print('Analista: ')
salarioanalista = reajusteSal(salarioanalista, salariobase, valreajuste)
print('Estagiário: ')
salarioestagio = reajusteSal(salarioestagio, salariobase, valreajuste)
print('Líder: ')
salariolider = reajusteSal(salariolider, salariobase, valreajuste)
