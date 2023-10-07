def lectura_de_archivos_base_de_datos(nombre_base_de_datos):
    f=open(nombre_base_de_datos) #Para abrir la base de datos 
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

def lectura_de_secuencias(secuencias):
    f1=open(secuencias)
    secuencia= []
    for linea1 in f1:
        linea1=linea1[0:-1]
        secuencia.append(linea1)
    return secuencia

def compara_str(basededatos, secuenciaPrueba):
    for k in range(len(basededatos)): 
        nombre= basededatos[k][0]
        numeros= basededatos[k][1:]
        if numeros== secuenciaPrueba:
            break
    return nombre


def main():
    pass
    basededatos=lectura_de_archivos_base_de_datos("/workspaces/Proyecto-ADN/dna/databases/large.csv")
    print(basededatos)
    secuencias = lectura_de_secuencias("/workspaces/Proyecto-ADN/dna/sequences/1.txt")
    secuenciaPrueba = [9,13,8,26,15,25,41,39]
    
    r = compara_str(basededatos,secuenciaPrueba)
    print(r)

if __name__ == '__main__':
    main()

