import random
import requests
import html

def mostrar_pregunta(pregunta):
    print("\n📢 Pregunta:")
    print(pregunta["question"])

    opciones = pregunta["incorrect_answers"] + [pregunta["correct_answer"]]
    random.shuffle(opciones)

    print("\nOpciones:")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

    return opciones

def obtener_pregunta_por_id(id_categoria):
    dificultad = random.choice(["medium", "hard"])
    
    url = f"https://opentdb.com/api.php?amount=1&category={id_categoria}&difficulty={dificultad}&type=multiple"

    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        data = respuesta.json()
        if data["results"]:
            pregunta_bruta = data["results"][0]

            # Decodificar todos los textos HTML
            pregunta_decodificada = {
                "category": html.unescape(pregunta_bruta["category"]),
                "question": html.unescape(pregunta_bruta["question"]),
                "correct_answer": html.unescape(pregunta_bruta["correct_answer"]),
                "incorrect_answers": [html.unescape(op) for op in pregunta_bruta["incorrect_answers"]]
            }

            return pregunta_decodificada

    print("❌ No se pudo obtener una pregunta.")
    return None


def obtener_id_categoria(resultadoDeLaRuleta):
    mapa_categorias = {
        "Arte": 25,
        "Ciencia": 17,
        "Deportes": 21,
        "Entretenimiento": 10,
        "Geografia": 22,
        "Historia": 23,
        "Corona": 9
    }
    return mapa_categorias.get(resultadoDeLaRuleta, 9)

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
    
    id_categoria = obtener_id_categoria(resultadoDeLaRuleta)
    pregunta = obtener_pregunta_por_id(id_categoria)
    
    opciones = mostrar_pregunta(pregunta)
    print(opciones)
main()