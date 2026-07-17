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
    soma_total = sum(notas)
    quantidade_notas = len(notas)
    media_calculada = soma_total / quantidade_notas
    return media_calculada

def verificar_aprovacao(media, media_minima=7.0):
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
