
import math
import msvcrt

#Se crea una funcion para calcular los años de las muestras
def Calcular_Años(K, Ar):
    t = (1.248 * (pow(10,9)))
    fFija = 0.109
    fAños =  ( (t) / math.log(2)) * ( math.log( ( ( (K*fFija) + (1*Ar) )/(1*fFija) ) / (K) ))
    return fAños

bEsNum = False #Se inicializa una variable booleana que nos servira para manter el ciclo

while bEsNum == False:
    sCantidadMuestras = input ( "Digite la catidad de muestras que desea realizar: ")

    #Verificamos si el valor digitado corresponde a un entero, en caso de serlo lo enmascaramos
    try:
        int(sCantidadMuestras)
        bEsNum = True
    except:
        bBabEsNumndera = False

    #Creamos una lista del tamaño de las muestras digitadas por el usuario
    if bEsNum == True:
        iCantidadMuestras = int(sCantidadMuestras)
        Cantidad_Muestras_Lista = [0] * iCantidadMuestras

        #Con un ciclo asignamos un valor unico a cada elemento de la lista
        i=0
        while i < iCantidadMuestras:
            Cantidad_Muestras_Lista[i] = i+1
            i = i+1
    else:
        print ("Ingrese un número")

# Se inicializan las variables que usaremos en las operaciones
Dic_Años = {0:0}
Dic_Masas = {0:0}
Dic_Eras = {0:0}

TMPrePaleozoica = 0
TMPaleozoica = 0
TMMesozoica = 0
TMCenozoica = 0

MPrePaleozoica = 0
MPaleozoica = 0
MMesozoica = 0
MCenozoica = 0

IdPrePaleozoica = "-"
IdPaleozoica = "-"
IdMesozoica = "-"
IdCenozoica = "-"

cenozoica = 65500000
mesozoica = 251000000
paleozoica = 542000000

for numero in  Cantidad_Muestras_Lista:
    print("")
    print("")
    print("-------------------------------------------------------------------------------------")
    print("")
    print("")
    Masa = int(input ( "Ingrese la masa del la muestra n°"+str(numero)+" :" ))
    K = int(input ( "Ingrese el valor de POTASIO del isótopo n°"+str(numero)+" :" ))
    Ar = int(input ( "Ingrese el valor del ARGÓN del isótopo n°"+str(numero)+" :" ))

    fAños =  Calcular_Años(K, Ar)

    Dic_Masas[numero] = Masa
    Dic_Años[numero] = fAños

    print("")
    print("")
    print("Información de la muestra")
    print("")
    print("")
    print ("El ID de la muestra es el ("+str(numero)+") y su edad aproximada en años es de: "+ str(Dic_Años[numero]))
    print("")
    print("")

    if fAños >= paleozoica:
        print("Basados en la edad apróximada la muestra pertenece a la era Pre-Paleozoica")
        Dic_Eras[numero] = "Pre-Paleozoica"
        TMPrePaleozoica = TMPrePaleozoica + int(Dic_Masas[numero])
        if int(Dic_Masas[numero]) > MPrePaleozoica:
            MPrePaleozoica = int(Dic_Masas[numero])
            IdPrePaleozoica = numero

    else:
        if fAños > mesozoica:
            print("Basados en la edad apróximada la muestra pertenece a la era Paleozoica")
            Dic_Eras[numero] = "Paleozoica"
            TMPaleozoica = TMPaleozoica + int(Dic_Masas[numero])
            if int(Dic_Masas[numero]) > MPaleozoica:
                MPaleozoica = int(Dic_Masas[numero])
                IdPaleozoica = numero

        else:
            if fAños > cenozoica:
                print("Basados en la edad apróximada la muestra pertenece a la era Mesozoica")
                Dic_Eras[numero] = "Mesozoica"
                TMMesozoica = TMMesozoica + int(Dic_Masas[numero])
                if int(Dic_Masas[numero]) > MMesozoica:
                    MMesozoica = int(Dic_Masas[numero])
                    IdMesozoica = numero

            else:
                print("Basados en la edad apróximada la muestra pertenece a la era Cenozoica")
                Dic_Eras[numero] = "Cenozoica"
                TMCenozoica = TMCenozoica + int(Dic_Masas[numero])
                if int(Dic_Masas[numero]) > MCenozoica:
                    MCenozoica = int(Dic_Masas[numero])
                    IdCenozoica = numero



print("")
print("")
print("Presione '0' para ver el resumen...")
key = None
while key != '0':
    key = msvcrt.getwch()

print("")
print("")
print("-------------------------------------------------------------------------------------")
print("")
print("Total de masa para la era Pre-Paleozoica: "+str(TMPrePaleozoica))
print("La muestra con mayor masa tiene el ID ("+str(IdPrePaleozoica)+") con un total de :"+str(MPrePaleozoica))
print("")
print("Total de masa para la era Paleozoica: "+str(TMPaleozoica))
print("La muestra con mayor masa tiene el ID ("+str(IdPaleozoica)+") con un total de :"+str(MPaleozoica))
print("")
print("Total de masa para la era Mesozoica: "+str(TMMesozoica))
print("La muestra con mayor masa tiene el ID ("+str(IdMesozoica)+") con un total de :"+str(MMesozoica))
print("")
print("Total de masa para la era Cenozoica: "+str(TMCenozoica))
print("La muestra con mayor masa tiene el ID ("+str(IdCenozoica)+") con un total de :"+str(MCenozoica))
print("")

print("")
print("")
print("Presione '0' para ver todas las muestras (ID-AÑOS-MASA-ERA)")
key = None
while key != '0':
    key = msvcrt.getwch()

print("")
print("")
print("")
for numero in Cantidad_Muestras_Lista:
    print ("ID ("+str(numero)+") años -> ("+str(Dic_Años[numero])+") Masa -> ("+str(Dic_Masas[numero])+") Era -> ("+str(Dic_Eras[numero])+"). ")
    print("")



