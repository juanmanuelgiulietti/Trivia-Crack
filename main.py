def iniciarJuego():
    """
    La funcion iniciarJuego() le da la bienvenida al usuario, pide el ingreso de un nombre y valida que la entrada sea valida.
    """
    usuario = str(input("Ingrese su nombre para iniciar la partida: "))
    while usuario == " ":
        print("Por favor ingrese un nombre valido.")
        usuario = str(input("Ingrese su nombre para iniciar la partida: "))
    return usuario

def main():
    """
    La funcion main() llama a todas las funciones del programa, para chequear su funcionamiento.
    """
    
    print(f"Bienvenido al juego de Preguntados!\n")
    usuario = iniciarJuego()
    print(f"\nHola {usuario}!")
main()