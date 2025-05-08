import random
import json

def mostrarPregunta(resultadoDeLaRuleta):
    """
    La funcion mostraPregunta(resultadoDeLaRuleta) recibe un archivo json con las preguntas y respuestas del juego y segun el resultado de la ruleta, devuelve una pregunta de esa categoria con sus opciones.
    """
    with open("preguntas.json", "r", encoding="utf-8") as archivo:
        preguntas = json.load(archivo)
    
    for pregunta in preguntas:
        if pregunta["categoria"].lower() == resultadoDeLaRuleta.lower():
            print(f"📚 Pregunta de {pregunta['categoria']}:")
            print(pregunta["pregunta"])
            print("Opciones:")
            for opcion in pregunta["opciones"]:
                print(f"- {opcion}")
            break
    return pregunta

def girarRuleta():
    """
    La funcion girarRuleta() elige aleatoreamente mediante un random.choice de la lista "categorias" una categoria para jugar.
    """
    categorias = ["Arte", "Ciencia", "Deportes", "Entretenimiento", "Geografia", "Historia", "Corona"]
    resultadoDeLaRuleta = random.choice(categorias)
    return resultadoDeLaRuleta

def gestionarTurnos(jugadorQueComienza, usuario):
    """
    La funcion gestionarTurnos(jugadorQueComienza, usuario) gestiona los turnos de los jugadores para ver quien comienza la partida.
    """
    if jugadorQueComienza == usuario:
        print(f"Comienza jugando: {jugadorQueComienza}")
    else:
        print(f"Comienza jugando: Computadora")

def determinarQuienComienza(usuario):
    """
    La funcion jugadorQueComienza(usuario) elige aleatoreamente desde una lista de jugadores, quien empieza a jugar.
    """
    jugadores = [usuario, "Computadora"]
    jugadorQueComienza = random.choice(jugadores)
    return jugadorQueComienza

def iniciarJuego():
    """
    La funcion iniciarJuego() le da la bienvenida al usuario, pide el ingreso de un nombre y valida que la entrada sea valida.
    """
    usuario = str(input("Ingrese su nombre para iniciar la partida: ")).capitalize()
    while usuario == " ":
        print("Por favor ingrese un nombre valido.")
        usuario = str(input("Ingrese su nombre para iniciar la partida: ")).capitalize()
    return usuario

def main():
    """
    La funcion main() llama a todas las funciones del programa, para chequear su funcionamiento.
    """
    
    print(f"Bienvenido al juego de Preguntados!\n")
    usuario = iniciarJuego()
    print(f"\nHola {usuario}!")
    
    jugadorQueComienza = determinarQuienComienza(usuario)
    print(f"\nTurno de comenzar: {jugadorQueComienza}")
    
    resultadoDeLaRuleta = girarRuleta()
    print(f"🎡 Resultado de la ruleta: {resultadoDeLaRuleta}\n")

    pregunta = mostrarPregunta(resultadoDeLaRuleta)
main()