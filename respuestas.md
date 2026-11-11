# Respuestas a preguntas de analisis

## Preguntas etapa 1
 * ¿Qué es la inteligencia artificial? Explícalo brevemente.
Es una rama de la informatica que requiere de tomar inteligencia humana decisiones, aprender, reconocer patrones y entender lenguajes   

## Preguntas etapa 2
 * ¿Qué función tiene el mensaje de sistema?
 Asignarle un rol al modelo de IA o indicar algo en especifico en el como debe responder

 * ¿Qué cambia entre enviar una pregunta directamente y definir instrucciones de comportamiento?
 En como responde el modelo, puede que responda de una forma muy general o algo que no no pueda ayudar, meintras que si le decimos un comportamiento el modelo le sera de ayuda en como nos debe de responder, por ejemplo si le decimos que sea tecnico y detallado sera una respuesta mucho mas especial

## Preguntas de etapa 3
 * ¿Por qué guardar mensajes del usuario? 
 Para que el modelo pueda tener contexto de la conversacion que se esta llevando
 * ¿Por qué guardar también las respuestas?
 Para que el modelo tenga en cuenta que ah proporcionado y mejorar las siguientes
 * ¿Qué sucede si solo se envía la pregunta actual?
 El modelo no sabra que ha pasado, probablemente alucine si o responda que no sabe

 ## Preguntas de etapa 4
 * ¿En qué difieren memoria y persistencia?
En la memoria solo es temporal, se guarda en la ram, al cerrar el programa se perdera la informacion mientras que en persistencia, esta puede ser utilizada las veces que sea necesaria
 * ¿Por qué convertir mensajes para almacenarlos en JSON? 
 Para tener un mejor control de la conversacion, y en como almacenarlo, para despues usarlos de nuevo
 * ¿Qué sucede si historial.json no existe?
El modelo no podra tener el contexto de las conversaciones pasadas, seria como si se usara por primera vez

## Preguntas de etapa 5
* ¿Qué componente se conecta con el modelo?
Se conecta con un historial json de las conversaciones anteriores que tuvo

* ¿Dónde se definen las instrucciones?
En el ```SystemMessage``` se le dice que rol tendra y como debera responder

* ¿Dónde reside la memoria durante la ejecución?
En la memoria ram

* ¿Cómo se guarda y recupera JSON?
Se guardan los objetos que se han generado con una estructura como 
```json
{
    "type": "human",
    "data": {
        "content": "Hola, me llamo Luciano. Tú cómo te llamas?",
        "additional_kwargs": {},
        "response_metadata": {},
        "type": "human",
        "name": null,
        "id": null
    }
}
```
con un metodo ```messages_to_dict()``` para depues sobreescribir el json y tambien recuperarlo se usa un metodo ```messages_from_dict()```

* ¿Qué diferencia existe entre modelo local y API Key?
El modelo local se ejecuta en la maquina de la persona que lo usuara, con limitaciones de su propio hardware mientras que usando uno con un API key sera con los datos y limitaciones que le de el proveedor

## Pregunta de comprension
1) primero utilice varios if para que segun sea el case decirle al modelo que rol debe tomar, si, el de un especialista en ia, o base datos etc.., en el constructor le meti ese rol, para que al hacerle un ´´´SystemMessage´´´ sepa que rol tamar segun sea el rol
2) si el usuario solo escribe "nuevo" en el prompt se toma como un prompt especial que se condiciona con un if, para solo pasar el ´´´SystemMessage´´´ de nuevo y limpiar el json
3) Al igual que el anterior "historial" se lo tomara como un prompt especial del programa para poder ver si el usuario ha ingresado datos o si solo se le ha dado el rol y se imprimen, con un for, si es mensaje de humano se pone con "usuario: " y si es de el bot seria con "Tutor: " para diferenciar