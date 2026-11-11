from src.modelo.modelo import Prompt

import os
from rich.console import Console
from rich.markdown import Markdown

class menuPrincipal():
    def __init__(self):
        self.console = Console()
        self.opcion = ""

    @staticmethod
    def limpiar_pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def pausar():
        input("\nPresione ENTER para volver al menú...")

    def mostrar_menu(self):
        print("=== Menú Principal ===\n")
        print("1. Modelo IA")
        print("2. Modelo Tutor programación")
        print("3. Modelo tutor IA")
        print("4. Modelo tutor base de datos")
        print("0. Salir\0")

    def ejecutar_opcion(self):
        while True:
            self.limpiar_pantalla()
            self.mostrar_menu()
            self.opcion = input("\n> Seleccione una opción: ")

            if self.opcion == "0":
                print("\nSaliendo del programa...")
                break

            elif self.opcion == "1":
                prompt = Prompt()
                respuesta = Markdown(prompt.generar_respuesta())

            elif self.opcion == "2":
                prompt = Prompt(tutor="programacion")
                respuesta = Markdown(prompt.generar_respuesta())

            elif self.opcion == "3":
                prompt = Prompt(tutor="ia")
                respuesta = Markdown(prompt.generar_respuesta())


            elif self.opcion == "4":
                prompt = Prompt(tutor="base_datos")
                respuesta = Markdown(prompt.generar_respuesta())

            else:
                print("Opción inválida. Por favor seleccione una opción válida.")
                self.pausar()