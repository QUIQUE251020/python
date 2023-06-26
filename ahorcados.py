import random

def juegoPerdido():
    #añadir intentos como variable ejemplo: def juegoPerdido(intentos) para que por cada intento fallido se muestre una imagen diferente
    ahorcado = [
        r"""
            --------
            |      |
            |      O
            |     \|/
            |      |
            |     / \
            -
        """
    ]
    print(ahorcado[0])


def inicioJuego():
    palabras=["python","padre","madre","perro","hermano"]
    palabraOculta = random.choice(palabras)
    palabra = "*" * len(palabraOculta)
    intentos = 6
    
    print("¡Bienvenido al Juego del Ahorcado!")
    print("La palabra tiene", len(palabraOculta), "letras.")
    print(palabra)
    
    while intentos>0:
        letra = input("Ingresa una letra: ")
        letra=letra.lower()

        if letra in palabraOculta:
            palabraActualizada = ""
            for i in range(len(palabraOculta)):
                if palabraOculta[i] == letra:
                    palabraActualizada += letra
                else:
                    palabraActualizada += palabra[i]
            palabra = palabraActualizada
            print(palabra)
                
        else:
            intentos -= 1
            print("Letra incorrecta. Te quedan", intentos, "intentos.")
            print(palabra)


        if "*" not in palabra:
            print("Felcididades Adivinaste la Palabra:", palabra)
            break

    if intentos == 0:
            print("Has perido, la palabra era: ",palabraOculta)
            juegoPerdido()
            
inicioJuego()
