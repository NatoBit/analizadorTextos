import re
from .patterns import PATTERNS

class AnalizadorTexto:
    def __init__(self, text):
        """Inicializa el analizador con un bloque de texto."""
        self.text = text
        self.resultados = {}

    def analizar(self, pattern_name):
        """Aplica el patrón seleccionado al texto y guarda los resultados."""
        if pattern_name not in PATTERNS:
            raise ValueError(f"El patrón '{pattern_name}' no está definido.")
        
        pattern = PATTERNS[pattern_name]
        matches = re.findall(pattern, self.text)
        self.resultados[pattern_name] = matches
        return matches

    def mostrar_resultados(self):
        """Muestra los resultados de todas las búsquedas."""
        if not self.resultados:
            print("No se han encontrado coincidencias.")
        else:
            for pattern, matches in self.resultados.items():
                print(f"\nPatrón '{pattern}':")
                for match in matches:
                    print(f"  - {match}")

    def guardar_resultados(self, filename="resultados.txt"):
        """Guarda los resultados en un archivo de texto."""
        with open(filename, "w") as f:
            for pattern, matches in self.resultados.items():
                f.write(f"\nPatrón '{pattern}':\n")
                for match in matches:
                    f.write(f"  - {match}\n")
