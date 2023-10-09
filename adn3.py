def buscar_str(secuencia_prueba,strprueba):
    contador = 0
    i = 0
    maximo = 0
    
    contar_secuencia = secuencia_prueba[0]
    lista_secuencia = list(contar_secuencia)

    contar_str = strprueba[0] #Pasar de lista a string
    listastr = list(contar_str) #Poner cada letra divida en comas en una lista
    
    while i < len(lista_secuencia):
                
        substring = contar_secuencia[i:i+len(listastr)]

        if contar_str == substring:
            contador = contador + 1
            print(contador)
            substring = secuencia_prueba[i+len(listastr):i+len(listastr)]
        else:
            if maximo > contador:
                repeticiones = maximo
                print(repeticiones)
            
    #repeticiones = max(repeticiones,contador)
    #return repeticiones

def main():
    pass

    strprueba = ["AGATC"]
    secuencia_prueba = ["AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGGGATAGAAGG"]
    
    buscarstr = buscar_str(secuencia_prueba,strprueba)
    #print (buscarstr)

if __name__ == '__main__':
    main()