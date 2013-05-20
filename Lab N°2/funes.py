
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Nombre    : Lizzie Ramirez
#Fecha     : 9-Mayo-2013
#Actividad : 3 - Funes Lab N°2
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funciones
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

def contar_palabras(texto):

    from operator import itemgetter
    
    dic = {}
    for palabra in texto:
        if not palabra in dic:
            dic[palabra] = 1
        else:
            dic[palabra] = dic[palabra] + 1

    dic_ordenado=sorted(dic.items(), key=itemgetter(1), reverse=True)
    print (dic_ordenado)

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funcion principal
#~~~~~~~~~~~~~~~~~~~~~~~~~~#

def main():
    
    f = open('funes.txt',encoding='utf-8')

#Debido a que en windows muestra 3 caracteres
#al principio del archivo, se comenzara a leer
#desde el 3 caracter en adelante
    f.seek(3)
#---------------------------#
    f=f.read()
    f=f.lower()
    f=f.split()
    
    contar_palabras(f)
    
    return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Identificador del main
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
if __name__ == '__main__':
  main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
