from codigo.bytebank import Funcionario

Joao = Funcionario('Joao Carlos', '21/08/1981', 1350)

print(Joao.idade())

def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

    funcionario_teste1 = Funcionario('Teste', '13/03/1999', 1111)
    print(f'Teste = {funcionario_teste1.idade()}')

    funcionario_teste2 = Funcionario('Teste', '01/12/1999', 1111)
    print(f'Teste = {funcionario_teste2.idade()}')

teste_idade()

ana = Funcionario('ana', '15/10/2020', 100000000)

print(ana.calcular_bonus())

