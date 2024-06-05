from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000'
        esperado = 24   #Given-Contexto

        funcionario_test = Funcionario('Teste', entrada, 1300)
        resultado = funcionario_test.idade() #When-Ação

        assert resultado == esperado #Then-Desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho ' # Given
        esperado = 'Carvalho'

        funcionario_teste = Funcionario(entrada, '11/11/2000', 1111)
        resultado = funcionario_teste.sobrenome() # When

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '15/08/1987', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado
    
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('teste', '15/08/1987', entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000

            funcionario_teste = Funcionario('Ana', '15/05/2010', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado

    '''def test_retorno_str(self):
        nome, data_nascimento, salario = 'Teste', '15/06/1987', 1300
        esperado = 'Funcionario(Teste, 15/06/1987, 1300)'

        funcionario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funcionario_teste.__str__()

        assert resultado == esperado'''