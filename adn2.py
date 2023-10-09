import os
from pathlib import Path
import sys

def lectura_de_archivos_base_de_datos(ruta_b):
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
    f1=open(ruta_s)
    secuencia= []
    for linea1 in f1:
        linea1=linea1[0:-1]
        secuencia.append(linea1)
    return secuencia

def compara_str(base_datos, secuencia_prueba):
    for k in range(len(base_datos)): 
        nombre= base_datos[k][0]
        numeros= base_datos[k][1:]
        if numeros== secuencia_prueba:
            break
    return nombre

def buscar_str(secuencias,strprueba):
    contar_secuencia = secuencias[0]
    lista_secuencia = list(contar_secuencia)

    contar_str = strprueba[0] #Pasar de lista a string
    listastr = list(contar_str) #Poner cada letra divida en comas en una lista
    
    for listastr in secuencias:
        contador = 0
        i = 0
        repeticiones = 0
    
        while i < len(lista_secuencia):
            substring = contar_secuencia[i:i+len(listastr)]
            
            if contar_str == substring:
                contador = contador + 1
                i = i + len(listastr)
            else:
                if contador > repeticiones:
                    repeticiones = contador
                contador = 0
                i = i + 1

        print(repeticiones)

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

    strprueba = ["TTTTTTCT"]
    
    buscarstr = buscar_str(secuencias,strprueba)
    #print (buscarstr)


    #secuencia_prueba = [9,13,33,26,45,11,36,39]

    #r = compara_str(base_datos, secuencia_prueba)
    #print(r)

if __name__ == '__main__':
    main()