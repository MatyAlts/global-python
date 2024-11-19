from clases import *
from objetos import *
from funciones import *
     
def main() -> None:
    while(True):
        print('''
            1. Ingresar ADN
            2. Detectar mutantes
            3. Crear mutante
            4. Sanar mutantes
            5. Imprimir ADN
            6. Salir
            ''')
        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            ingresar_ADN()
        elif opcion == '2':
            funcion_detectar(input('Ingrese el nombre del ADN: '))
        elif opcion == '3':
            funcion_mutacion(input('Ingrese el nombre del ADN: '))
        elif opcion == '4':
            funcion_sanador(input('Ingrese el nombre del ADN: '))
        elif opcion == '5':
            funcion_imprimir_ADN(input('Ingrese el nombre del ADN: '))
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opcion incorrecta, intente de nuevo")

if __name__ == '__main__':
    main()