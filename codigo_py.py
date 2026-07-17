# --- gerenciador_notas.py ---

# 1. Estrutura de dados
estudantes = [
    {
        'nome': 'Ana Beatriz',
        'idade': 15,
        'turma': 'B',
        'notas': [6.0, 8.0, 7.5], 
    },
    {   
        'nome': 'Janaina',
        'idade': 8,
        'turma': 'A',
        'notas': [8.0, 8.5, 8.5],
    }
]

# 2. Funções de cálculo e regras de negócio com docstrings (PEP 8)
def calcular_media(notas):
    """
    Calcula a média aritmética a partir de uma lista de notas.

    Args:
        notas (list): Uma lista de valores numéricos (float) representando 
                      as notas individuais obtidas pelo estudante.

    Returns:
        float: O valor final da média calculada.
    """
    soma_total = sum(notas)
    quantidade_notas = len(notas)
    media_calculada = soma_total / quantidade_notas
    
    return media_calculada


def verificar_aprovacao(media, media_minima=7.0):
    """
    Avalia a situação acadêmica do estudante com base na média obtida.

    Args:
        media (float): O valor da média final do estudante.
        media_minima (float, optional): A nota de corte estabelecida pela instituição 
                                        para aprovação. O valor padrão é 7.0.

    Returns:
        str: Retorna 'Aprovado' se a média for maior ou igual 
             à média mínima exigida. Caso contrário, retorna 'Reprovado'.
    """
    if media >= media_minima:
        return 'Aprovado'
    else:
        return 'Reprovado'

# 3. Função de Relatório
def gerar_relatorio(alunos):
    print("--- RELATÓRIO DE DESEMPENHO ACADÊMICO ---")

    for aluno in alunos:
        nome = aluno['nome']
        notas = aluno['notas']

        media_calculada = calcular_media(notas)
        status = verificar_aprovacao(media_calculada)
        print(f"Aluno: {nome} | Média: {media_calculada:.1f} | Status: {status}")

    print("_" * 40) 

# Execução do sistema
gerar_relatorio(estudantes)


# --- test_notas.py ---

import unittest
from gerenciador_notas import calcular_media, verificar_aprovacao

class TestSistemaAcademico(unittest.TestCase):

    def test_condicoes_normais(self):
        # Testa o comportamento comum de aprovação e reprovação (corte padrão 7.0)
        self.assertEqual(verificar_aprovacao(8.5), 'Aprovado')
        self.assertEqual(verificar_aprovacao(7.0), 'Aprovado')
        self.assertEqual(verificar_aprovacao(5.0), 'Reprovado')

    def test_lista_vazia(self):
        # Testa o edge case limitador (lista vazia). 
        # Como não há notas, a divisão por zero (len(notas) == 0) deve gerar uma exceção.
        with self.assertRaises(ZeroDivisionError):
            calcular_media([])

    def test_media_minima_zero(self):
        # Testa o comportamento da função ao forçar a nota de corte para zero absoluto
        self.assertEqual(verificar_aprovacao(2.5, media_minima=0), 'Aprovado')
        self.assertEqual(verificar_aprovacao(0.0, media_minima=0), 'Aprovado')

if __name__ == '__main__':
    unittest.main()


# --- README.md ---

# Sistema de Gerenciamento Acadêmico

## Sobre o Projeto
Este projeto é um sistema em Python feito para gerenciar o desempenho acadêmico de estudantes. Ele recebe uma base de dados com as notas, calcula as médias, verifica a aprovação (com nota de corte 7.0) e exibe um relatório consolidado no terminal.

## Pré-requisitos
* Python 3.x instalado na máquina.
* Um terminal ou interpretador de linha de comando.
* Não é necessário instalar bibliotecas externas.

## Como Executar
1. Salve o arquivo principal do projeto (`gerenciador_notas.py`) no seu computador.
2. Abra o terminal do seu sistema operacional.
3. Acesse a pasta onde o arquivo está salvo usando o comando `cd`.
4. Execute o script digitando `python gerenciador_notas.py` e aperte Enter.
5. O relatório de desempenho será gerado e exibido na tela.

## Como Testar
Para garantir que as funções de cálculo e verificação estão corretas, você pode rodar os testes unitários:
1. Salve o arquivo de testes (`test_notas.py`) na mesma pasta do arquivo principal.
2. Abra o terminal nessa pasta.
3. Digite o comando `python test_notas.py` para executar as checagens e validar as regras institucionais.
