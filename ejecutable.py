from clases import *

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
        imprimir_ADN(adn)
        return adn

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
        
def mutante_horizontal(adn):
    # Detectar mutante horizontal
    for i in range(len(adn)):
        for j in range(len(adn[i])-3):
            if adn[i][j] == adn[i][j+1] == adn[i][j+2] == adn[i][j+3]:
                return True
    return False

def mutante_vertical(adn):
    # Detectar mutante vertical
    for i in range(len(adn)-3):
        for j in range(len(adn[i])):
            if adn[i][j] == adn[i+1][j] == adn[i+2][j] == adn[i+3][j]:
                return True
    return False

def mutante_diagonal(adn):
    # Detectar mutante diagonal
    for i in range(len(adn)-3):
        for j in range(len(adn[i])-3):
            if adn[i][j] == adn[i+1][j+1] == adn[i+2][j+2] == adn[i+3][j+3]:
                return True
    return False

def main():
    adn = []
    while(True):
        print('''
            1. Ingresar ADN
            2. Detectar mutantes
            3. Crear mutante
            4. Sanar mutantes
            5. Salir
            ''')
        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            adn = ingresar_ADN()
        elif opcion == '2':
            print("Es mutante") if mutante_horizontal(adn) or mutante_vertical(adn) or mutante_diagonal(adn) else print("No es mutante")
        elif opcion == '3':
            Mutador.crear_mutante(adn)
        elif opcion == '4':
            Sanador.sanar_mutantes(adn)
        elif opcion == '5':
            break
        else:
            print("Opcion incorrecta, intente de nuevo")

if __name__ == '__main__':
    main()