from analizador.core import AnalizadorTexto

def main():
    print("Bienvenido al Analizador de Texto con Regex.")
    
    # Simulación de carga de archivo de texto
    archivo = input("Ingresa el nombre del archivo de texto (ejemplo: 'documento.txt'): ")
    try:
        with open(archivo, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no se encontró.")
        return

    analizador = AnalizadorTexto(text)
    
    while True:
        print("\n¿Qué patrón te gustaría buscar?")
        print("1. Correo electrónico")
        print("2. Número de teléfono")
        print("3. Fecha")
        print("4. URL")
        print("5. Dirección IP")
        print("6. Mostrar todos los resultados")
        print("7. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            analizador.analizar("email")
        elif opcion == "2":
            analizador.analizar("phone")
        elif opcion == "3":
            analizador.analizar("date")
        elif opcion == "4":
            analizador.analizar("url")
        elif opcion == "5":
            analizador.analizar("ip")
        elif opcion == "6":
            analizador.mostrar_resultados()
        elif opcion == "7":
            print("¡Gracias por usar el Analizador de Texto!")
            break
        else:
            print("Opción no válida.")

    # Opción para guardar los resultados en un archivo
    guardar = input("\n¿Te gustaría guardar los resultados en un archivo? (s/n): ")
    if guardar.lower() == 's':
        analizador.guardar_resultados()

if __name__ == "__main__":
    main()