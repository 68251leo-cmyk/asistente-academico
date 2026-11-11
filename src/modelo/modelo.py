from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from langchain_core.messages import(
    SystemMessage,
    HumanMessage,
    messages_to_dict,
    messages_from_dict
)
import json
import os


class Prompt:
    def __init__(self, tutor=None):
        load_dotenv()
        self.file = "historial.json"
        self.tutor = tutor
        self.modelo = ChatOllama(model="qwen2.5:3b", temperature=0.2)
        self.historial = self.cargar_historial()


    def cargar_historial(self):
        if (self.tutor == None):
            if os.path.exists(self.file):
                with open(self.file, "r", encoding="utf-8") as f:
                    return messages_from_dict(json.load(f))
            else:
                return [
                    SystemMessage(
                        content="Eres un tutor universitario, que responde en español, usa lenguaje sencillo, explica claramente, incluye ejemplos cuando convenga y reconoce cuando desconoces una respuesta."
                        )]
        elif self.tutor == "programacion":
            return [
                SystemMessage(
                    content="Eres un tutor de programacion, que responde en español, usa lenguaje sencillo, explica claramente, incluyendo ejemplos cuando convenga y reconoce cuando desconoces una respuesta"
                )]

        elif self.tutor == "ia":
            return [
                SystemMessage(content="Eres un tutor de inteligencia artificial, que responde en español, usa lenguaje sencillo, explica claramente, incluyendo ejemplos cuando convenga y reconoce cuando desconoces una respuesta"
            )]        

        elif self.tutor == "base_datos":
            return [
                SystemMessage(content="Eres un tutor de base de datos, que responde en español, usa lenguaje sencillo, explica claramente, incluyendo ejemplos cuando convenga y reconoce cuando desconoces una respuesta"
            )]
        else:
            return self.historial


    def guardar_historial(self):
        with open(self.file, "w", encoding="utf-8") as f:
            historial_dict = messages_to_dict(self.historial)
            json.dump(historial_dict, f, ensure_ascii=False, indent=4)


    def generar_respuesta(self):
        while True:
            print("\n==========================")
            pregunta = input("> Usuario: ")

            if pregunta.lower() == "salir":
                break

            elif pregunta.lower() == "nuevo":
                self.historial = self.cargar_historial()
                self.guardar_historial()
                print("\nHistorial reiniciado. Puedes hacer nuevas preguntas.")
                

            elif pregunta.lower() == "historial":
                print("\nHistorial de conversación:")
                for mensaje in self.historial:
                    if isinstance(mensaje, HumanMessage):
                        print(f"Usuario: {mensaje.content}")
                    else:
                        print(f"Tutor: {mensaje.content}")
                
            else:
                self.historial.append(HumanMessage(content=pregunta))

                respuesta = self.modelo.invoke(self.historial)
                print("\n--------------------------")
                print("Respuesta: ", respuesta.content)

                self.historial.append(respuesta)
                self.guardar_historial()