
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Nombre    : Lizzie Ramirez
#Fecha     : 9-Mayo-2013
#Actividad : 2 - Palindroma Lab N°2
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funciones
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

def es_par(num):
    if num%2==0:
        return True
    else:
        return False

def es_palindroma(lista):
    largo = len(lista)
    if es_par(largo):
        for i in range(largo):
            if lista[i] != lista[largo-1-i]:
                return False
    else:
        for i in range(largo):
            if lista[i]!=lista[largo-1-i]:
                return False
    return True

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funcion principal
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

def main():
    print("Verificador de palabras palindromas")
    palabra=input("Ingrese su palabra  : ")

    lista=list(palabra)

    if (es_palindroma(lista)):
        print("La palabra",palabra,"es PALINDROMA")
    else:
        print("La palabra",palabra,"NO es PALINDROMA")

    return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Identificador del main
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
if __name__ == '__main__':
  main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
