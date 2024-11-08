from objetos import *
def ingresar_ADN() -> None:
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

def verificar_ADN(adn) -> bool:
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

def imprimir_ADN(adn) -> None:
    # Imprimir el ADN
    print("Su ADN: ")
    for i in range(len(adn)):
        print('\t[', end = " ")
        for j in range(len(adn[i])):
            print('\t', adn[i][j], end = " ")
        print('\t]')

def funcion_detectar(nombre) -> None:
    # Detectar mutantes
    try:
        objetos_detector[nombre] = Detector(matrices[nombre])
        print(objetos_detector[nombre].detectar_mutantes())
    except:
        print("ADN no encontrado")

def funcion_mutacion(nombre) -> None:
    # Crear mutantes
    if nombre not in matrices:
        print("ADN no encontrado")
        return
    base_nitrogenada = input("""
                             Ingrese la base nitrogenada a mutar
                             (A) Adenina (C) Citosina (G) Guanina (T) Timina
                             """).upper()
    
    while(base_nitrogenada != 'A' and base_nitrogenada != 'C' and base_nitrogenada != 'G' and base_nitrogenada != 'T'):
        print("Base nitrogenada invalida")
        base_nitrogenada = input("""
                             Ingrese la base nitrogenada a mutar
                             (A) Adenina (C) Citosina (G) Guanina (T) Timina
                             """).upper()
        
    orientacion_de_la_mutacion = input("""Ingrese la orientacion de la mutacion
                                       Horizontal, Vertical, Diagonal
                                       """).lower()
    
    while(orientacion_de_la_mutacion != 'horizontal' and orientacion_de_la_mutacion != 'vertical' and orientacion_de_la_mutacion != 'diagonal'):
        print("Orientacion invalida")
        orientacion_de_la_mutacion = input("""Ingrese la orientacion de la mutacion
                                       Horizontal, Vertical, Diagonal
                                       """).lower()
    fila = int(input("Ingrese la fila de la mutacion"))-1
    while(fila < 0 or fila > 5):
        print("Fila invalida")
        fila = input("Ingrese la fila de la mutacion")-1
    columna = int(input("Ingrese la columna de la mutacion"))-1
    while(columna < 0 or columna > 5):
        print("Columna invalida")
        columna = input("Ingrese la columna de la mutacion")-1
    posicion_inicial = (fila, columna)
    try:
        if orientacion_de_la_mutacion == 'horizontal' or orientacion_de_la_mutacion == 'vertical':
            objetos_radiacion[nombre] = Radiacion(matrices[nombre])
            matrices[nombre] = objetos_radiacion[nombre].crear_mutante(base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion)
        else:
            objetos_virus[nombre] = Virus(matrices[nombre])
            matrices[nombre] = objetos_virus[nombre].crear_mutante(base_nitrogenada, posicion_inicial)
    except ValueError:
        print("La posición inicial y la longitud de la mutación exceden los límites de la matriz ADN.")
    except Exception as e:
        print("Error: ",e)
    else:
        print("Mutante creado")
        imprimir_ADN(matrices[nombre])

def funcion_sanador(nombre) -> None:
    # Sanar mutantes
    try:
        objetos_sanador[nombre] = Sanador(matrices[nombre])
    except:
        print("ADN no encontrado")
    else:
        objetos_detector[nombre] = objetos_sanador[nombre].sanar_mutantes()
        print("Mutante sanado")
        imprimir_ADN(objetos_detector[nombre])
        