
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Nombre    : Lizzie Ramirez
#Fecha     : 9-Mayo-2013
#Actividad : 3 - Cachipun Lab N°2
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funciones
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

def ganador_cachipun(jugadores):
    error=False
    jugadas=['R','T','P']

    #valida num de jugadores
    if len(jugadores)!= 2:
        error=True
        raise Exception("Numero incorrecto de jugadores")

    #valida que la jugada exista
    if not(jugadores[0][1] in jugadas and jugadores[1][1] in jugadas):
        error=True
        raise Exception("Jugada no valida")

    #si no existe error, se ve que jugador gana
    if error==False:

        #ve si es empate
        if jugadores[0][1]==jugadores[1][1]:
            print (jugadores[0],"gana ya que es EMPATE")
            
        if (jugadores[0][1] == 'R' and jugadores[1][1] == 'T') or (jugadores[0][1] == 'P' and jugadores[1][1] == 'R') or (jugadores[0][1] == 'T' and jugadores[1][1] == 'P'):
            print(jugadores[0][0]," gana ya que ", jugadores[0][1],">",jugadores[1][1])
            
        if(jugadores[1][1] == 'R' and jugadores[0][1] == 'T' or jugadores[1][1] == 'P' and jugadores[0][1] == 'R' or jugadores[1][1] == 'T' and jugadores[0][1] == 'P'):
            print(jugadores[1][0]," gana ya que ", jugadores[1][1],">",jugadores[0][1])

    #si existe error, se devuelve al main#
    else:
        main()

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funcion principal
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

def main():
    print("Juego del cachipun")
    print("Jugadas :")
    print("         Piedra = R")
    print("         Papel  = P")
    print("         Tijera = T")

    jugadores=[]
    
    jugador_1=input("Ingrese Jugador 1: Nombre Jugada -> ")
    jugador_2=input("Ingrese Jugador 2: Nombre Jugada -> ")

    jugador_1=jugador_1.split()
    jugador_2=jugador_2.split()
    
    jugadores=[jugador_1,jugador_2]

    jugadores[0][1]=jugadores[0][1].upper()
    jugadores[1][1]=jugadores[1][1].upper()

    ganador_cachipun(jugadores)
    
    return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Identificador del main
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
if __name__ == '__main__':
  main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
