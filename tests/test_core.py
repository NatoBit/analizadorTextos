import unittest
from analizador.core import AnalizadorTexto

class TestAnalizadorTexto(unittest.TestCase):
    
    def setUp(self):
        self.text = "Mi correo es ejemplo@correo.com y mi número es +123 456 7890."
        self.analizador = AnalizadorTexto(self.text)
    
    def test_buscar_email(self):
        resultado = self.analizador.analizar("email")
        self.assertIn("ejemplo@correo.com", resultado)
    
    def test_buscar_telefono(self):
        resultado = self.analizador.analizar("phone")
        self.assertIn("+123 456 7890", resultado)

if __name__ == '__main__':
    unittest.main()