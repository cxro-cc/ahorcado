##################################
#       Palabras escondidas      #
##################################
import random

palabras = ["rinoceronte", "chimpance", "guacamaya", "avestruz", "caballo", "camaleon", "venado", "jaguar", "conejo", "gorila", "china", "paraguay", "argentina", "jamaica", "sudan", "chad", "australia", "venezuela", "indonesia"]

# Elección de la palabra al azar

def palabra():
    azar = random.randint(0, len(palabras)-1)
    return(palabras[azar])