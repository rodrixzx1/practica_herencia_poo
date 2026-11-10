import sys
import os

# Agrega la ruta raíz al sistema para que pueda encontrar la carpeta 'ejercicios'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ejercicios.ejercicio1_cine import boletos as ejecutar_ej1
from ejercicios.ejercicio2_estacionamiento import estancias as ejecutar_ej2

def mostrar_menu():
    while True:
        print("\n========================================")
        print("   MENÚ PRÁCTICA: HERENCIA EN POO")
        print("========================================")
        print("1. Ejecutar Ejercicio 1 (Boletos de Cine)")
        print("2. Ejecutar Ejercicio 2 (Estacionamiento)")
        print("3. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            print("\n--- SALIDA EJERCICIO 1 (BOLETOS) ---")
            for boleto in ejecutar_ej1:
                print(boleto.ticket())
        elif opcion == "2":
            print("\n--- SALIDA EJERCICIO 2 (ESTACIONAMIENTO) ---")
            for estancia in ejecutar_ej2:
                print(estancia.ticket())
        elif opcion == "3":
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona una opción correcta.")

if __name__ == "__main__":
    mostrar_menu()