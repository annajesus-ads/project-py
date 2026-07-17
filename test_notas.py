import unittest
from gerenciador_notas import calcular_media, verificar_aprovacao

class TestSistemaAcademico(unittest.TestCase):

    def test_condicoes_normais(self):
        self.assertEqual(verificar_aprovacao(8.5), 'Aprovado')
        self.assertEqual(verificar_aprovacao(7.0), 'Aprovado')
        self.assertEqual(verificar_aprovacao(5.0), 'Reprovado')

    def test_lista_vazia(self):
        with self.assertRaises(ZeroDivisionError):
            calcular_media([])

    def test_media_minima_zero(self):
        self.assertEqual(verificar_aprovacao(2.5, media_minima=0), 'Aprovado')
        self.assertEqual(verificar_aprovacao(0.0, media_minima=0), 'Aprovado')

if __name__ == '__main__':
    unittest.main()
