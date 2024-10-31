from objetos import *
def ingresar_ADN():
    # Ingresar el ADN
    adn = []
    print('''
          Ingrese un ADN de 6x6, separando cada fila por "," ejemplo:
          AGATCA, GATTCA, CAACAT, GAGCTA, ATTGCG, CTGTTC
          ''')
    try:
        while(True):
            adn_en_formato = input('Ingrese el ADN: ').replace(' ', '').upper()
            if(verificar_ADN(adn_en_formato.split(','))):
                adn = adn_en_formato.split(',')
                break
            else:
                print("ADN incorrecto, intente de nuevo\n")
    except:
        print("Error al ingresar el ADN")
    else:
        nombre = input("Ingrese el nombre para su ADN: ")
        matrices[nombre] = adn
        
        imprimir_ADN(adn)

def verificar_ADN(adn):
    # Verificar si el ADN es correcto
    for i in range (len(adn)):
            if len(adn[i]) != 6:
                print("Error al ingresar el ADN")
                return False
            else:
                for i in range(len(adn)):
                    for j in range(len(adn[i])):
                        if adn[i][j] != 'A' and adn[i][j] != 'C' and adn[i][j] != 'G' and adn[i][j] != 'T':
                            return False
    return True

def imprimir_ADN(adn):
    # Imprimir el ADN
    print("Su ADN: ")
    for i in range(len(adn)):
        print('\t[', end = " ")
        for j in range(len(adn[i])):
            print('\t', adn[i][j], end = " ")
        print('\t]')

def funcion_detectar(nombre):
    # Detectar mutantes
    objetos_detector[nombre] = Detector(matrices[nombre])
    try:
        if objetos_detector[nombre].detectar_mutantes():
            objetos_detector[nombre].imprimir_cantidad_mutantes()
        else:
            print("No es un mutante")
    except:
        print("ADN no encontrado")

def funcion_sanador(nombre):
    # Sanar mutantes
    try:
        objetos_sanador[nombre] = Sanador(matrices[nombre])
    except Exception as e:
        print("error: ", e)
    else:
        objetos_detector[nombre] = objetos_sanador[nombre].sanar_mutantes()
        print("Mutante sanado")
        imprimir_ADN(objetos_detector[nombre])
        