import os
from pathlib import Path
import sys

def lectura_de_archivos_base_de_datos(ruta_b):
    """_Método que hace la lectura de la base de datos y regresa los datos en lista_

    Args:
        ruta_b (_pathlib.PosixPath_): _Dirección de los archivo que se van a leer_

    Returns:
        _list_: _Datos del databases sobre los STR y las personas_
    """
    f=open(ruta_b) #Para abrir la base de datos
    base_de_datos=[]
    for linea in f:
        linea=linea[0:-1]
        linea.split(",")
        base_de_datos.append(linea)
    
    lista_resultante = []

    for linea in base_de_datos:
        elementos = linea.split(",")  # Dividir la lista de base de datos en elementos separados por comas
        lista_linea = []  # Crear una lista para cada línea de datos
        for elemento in elementos:
                lista_linea.append(elemento)  # Agregar cada elemento a la lista de la línea
        lista_resultante.append(lista_linea)
  
    for i in range(1,len(lista_resultante)):
        for j in range(1,len(lista_resultante[0])):
            lista_resultante[i][j]=int(lista_resultante[i][j])

    return lista_resultante

def lectura_de_secuencias(ruta_s):
    """_Método que hace la lectura de las secuencias_

    Args:
        ruta_s (_pathlib.PosixPath_): _Dirección de los archivos de secuencias que se van a leer_

    Returns:
        _list_: _Secuencias de DNA que se van a comparar_
    """
    f1=open(ruta_s)
    secuencia= []
    for linea1 in f1:
        linea1=linea1[0:-1]
        secuencia.append(linea1)

    return secuencia

def compara_str(base_datos,buscarstr):
    """_Método que compara la cantidad de STR con las personas y si no hay nadie igual False_

    Args:
        base_datos (_list_): _Datos del databases sobre los STR y las personas_
        buscarstr (_list_): _Cantidad de veces que se repite cada STR_

    Returns:
        _string_: _El nombre de la persona con la que coincide el STR y secuencia_
    """
    for k in range(len(base_datos)): 
        nombre= base_datos[k][0]
        numeros= base_datos[k][1:]
        if numeros == buscarstr:
            return (nombre)
            
    return (False)


def buscar_str(secuencias,strprueba):
    """_Método que cuenta la cantidad de veces que se repite cada STR en la cadena_

    Args:
        secuencias (_list_): _Secuencias de DNA que se van a comparar_
        strprueba (_list_): _STR que se va a buscar en la secuencia_

    Returns:
        _int_: _Cantidad de veces seguidas que se repite el STR en la secuencia_
    """
    
    contar_secuencia = secuencias[0] #AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAA
    lista_secuencia = list(contar_secuencia) #['A', 'A', 'G', 'G', 'T', 'A',.........]
    
    contar_str = strprueba[0] #TTTTTTCT
    listastr = list(contar_str) #['T', 'T', 'T', 'T', 'T', 'T', 'C', 'T']
    
    contador = 0
    i = 0
    repeticiones = 0
    
    while i <= len(lista_secuencia):
        substring = lista_secuencia[i:i+len(listastr)] #['A', 'A', 'G', 'G', 'T', 'A', 'A', 'G'],['A', 'G', 'G', 'T', 'A', 'A', 'G', 'T']
            
        if listastr == substring:
            contador = contador + 1
            i = i + len(listastr) - 1

        else:
            if contador >= repeticiones:
                repeticiones = contador
                contador = 0
        i = i + 1
    
    return repeticiones

def buscar_str2(base_datos):
    """_Método que busca los STR que están en la base de datos y que van a ser usados para comparar_

    Args:
        base_datos (_list_): _Datos sobre todos los STR y repeticiones de cada persona_

    Returns:
        _list_: _STR que se va a buscar en la secuencia_
    """
    strprueba = []
    for i in range (1,len(base_datos[0] )): #[0][1]
        elemento= base_datos[0][i]
        strprueba.append(elemento)
        
    return strprueba
    #print (strprueba)

def main():
    pass

    directorio = os.getcwd()
    subdirectorio_base_datos = Path("dna/databases")
    archivo_b = sys.argv[1]
    ruta_b = directorio / subdirectorio_base_datos / archivo_b
 
    base_datos = lectura_de_archivos_base_de_datos(ruta_b)
    #print(base_datos)

    subdirectorio_secuencias = Path("dna/sequences")
    archivo_s = sys.argv[2]
    ruta_s = directorio / subdirectorio_secuencias / archivo_s

    secuencias = lectura_de_secuencias(ruta_s)
    #print(secuencias)

    strprueba_1 = buscar_str2(base_datos) #['AGATC', 'TTTTTTCT', 'AATG', 'TCTAG', 'GATA', 'TATC', 'GAAA', 'TCTG']
    
    buscarstr=[]
    for j in range(0,len(strprueba_1)):
        strprueba = [strprueba_1[j]]
        buscarstr_1 = buscar_str(secuencias,strprueba)

        buscarstr.append(buscarstr_1)
    #print(buscarstr)

    r = compara_str(base_datos, buscarstr)
    if r== False:
        print("No match")
    else:
        print(r)

if __name__ == '__main__':
    main()
