#######################
#       AHORCADO      #
#######################

import ahorcado_diagramas
import palabras as p

# Palabra elegida al azar
palabra = p.palabra()
# Lista con guiones
lineas = ["_" for n in palabra]

# Inicializar intentos
intentos = 7
adivinada = ""
intentos_letra = []
# Representación con guiones de palabra
print(" ".join(lineas))


# Ahorcado
while intentos > 0 and adivinada != palabra:
    letra = input("letra: ")
    letra = letra.lower()
    # Letra dentro de palabra
    if letra in palabra:
        p = 0
        while p != -1:
            p = palabra.find(letra, p)
            if p != -1:
                lineas[p] = letra
                p = p + 1
    else: 
        intentos_letra.append(letra)
        intentos=intentos-1
    
    # Impresion de dibujos
    print(ahorcado_diagramas.ahorcado(intentos))
    # Impresion de letras usadas
    print("intentos: ", intentos_letra)
    # Impresion de letras
    print(" ".join(lineas))

    adivinada = "".join(lineas)

if intentos == 0:
    print("La palabra era: ", palabra)
else:
    intentos = 8
    print(ahorcado_diagramas.ahorcado(intentos))






