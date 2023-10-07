def lectura_de_archivos(nombre):
    f=open(nombre) #Para abrir la base de datos pequeña
    base_de_datos_s=[]
    for linea1 in f:
        linea1=linea1[0:-1]
        base_de_datos_s.append(linea1)
    return base_de_datos_s

def main():
    pass
    x=lectura_de_archivos("/workspaces/Proyecto-ADN/dna/databases/large.csv")
    print(x)

if __name__ == '__main__':
    main()
