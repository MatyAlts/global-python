import random

class Detector:
    """
    Encargada de detectar mutantes en el ADN
    """

    def __init__(self, adn: list) -> None:
        self.adn = adn
        self.__cantidad_mutantes_horizontales = 0
        self.__cantidad_mutantes_verticales = 0
        self.__cantidad_mutantes_diagonales = 0
    
    __cantidad_mutantes_horizontales = 0
    __cantidad_mutantes_verticales = 0
    __cantidad_mutantes_diagonales = 0
    
    def mutante_horizontal(self) -> bool:
    # Detectar mutante horizontal
        for i in range(len(self.adn)):
            for j in range(len(self.adn[i])-3):
                if self.adn[i][j] == self.adn[i][j+1] == self.adn[i][j+2] == self.adn[i][j+3]:
                    self.__cantidad_mutantes_horizontales += 1
                    return True
        return False

    def mutante_vertical(self) -> bool:
        # Detectar mutante vertical
        for i in range(len(self.adn)-3):
            for j in range(len(self.adn[i])):
                if self.adn[i][j] == self.adn[i+1][j] == self.adn[i+2][j] == self.adn[i+3][j]:
                    self.__cantidad_mutantes_verticales += 1
                    return True
        return False

    def mutante_diagonal(self) -> bool:
        # Detectar mutante diagonal
        for i in range(len(self.adn)-3):
            for j in range(len(self.adn[i])-3):
                if self.adn[i][j] == self.adn[i+1][j+1] == self.adn[i+2][j+2] == self.adn[i+3][j+3]:
                    self.__cantidad_mutantes_diagonales += 1
                    return True
        return False

    
    def detectar_mutantes(self) -> bool:
        return self.mutante_horizontal() or self.mutante_vertical() or self.mutante_diagonal()
        
    def devolver_adn(self) -> list:
        # Devuelve el ADN
        return self.adn
    
class Mutador:
    """
    Encargada de crear mutantes en el ADN
    """
    def __init__(self, adn: list) -> None:
        self.adn = adn
        
    #base_nitrogenada = ['A', 'T', 'C', 'G']
    atributo_2 = 0
    atributo_3 = 0
    
    def crear_mutante(self, base_nitrogenada: list, posicion_inicial: int, orientacion_de_la_mutacion: str) -> list:
        pass
    
class Radiacion(Mutador):
    """
    Heredada de la clase Mutador
    Encargada de crear mutantes horizontales y verticales
    """
    def __init__(self, adn: list) -> None:
        super().__init__(adn)
        
    def crear_mutante(self, base_nitrogenada: list, posicion_inicial: tuple, orientacion_de_la_mutacion: str) -> list:
        fila, columna = posicion_inicial
        adn_mutada = [list(fila) for fila in self.adn]
        
        if orientacion_de_la_mutacion == 'horizontal':
            if columna + len(base_nitrogenada) > len(self.adn[0]):
                raise ValueError("La posición inicial y la longitud de la mutación exceden los límites de la matriz ADN.")
            for i in range(len(base_nitrogenada)):
                adn_mutada[fila][columna + i] = base_nitrogenada[i]
        elif orientacion_de_la_mutacion == 'vertical':
            if fila + len(base_nitrogenada) > len(self.adn):
                raise ValueError("La posición inicial y la longitud de la mutación exceden los límites de la matriz ADN.")
            for i in range(len(base_nitrogenada)):
                adn_mutada[fila + i][columna] = base_nitrogenada[i]
        
        return adn_mutada

class Virus(Mutador):
    """
    Heredada de la clase Mutador
    Encargada de crear mutantes diagonales
    """
    def __init__(self, adn: list) -> None:
        super().__init__(adn)
        
    def crear_mutante(self, base_nitrogenada: str, posicion_inicial: tuple) -> list:
        fila, columna = posicion_inicial
        adn_mutada = [list(row) for row in self.adn]

        longitud_mutacion = 4

        if fila < 0 or columna < 0 or fila + longitud_mutacion > len(self.adn) or columna + longitud_mutacion > len(self.adn[0]):
            raise ValueError("La posición inicial y la longitud de la mutación exceden los límites de la matriz ADN.")

        for i in range(longitud_mutacion):
            adn_mutada[fila + i][columna + i] = base_nitrogenada

        adn_mutada = [''.join(row) for row in adn_mutada]
        return adn_mutada
class Sanador(Detector):
    """
    Heredada de la clase Detector
    Encargada de sanar mutantes
    """
    def __init__(self, adn: list) -> None:
        super().__init__(adn)
    
    def sanar_mutantes(self) -> list:
        if(self.detectar_mutantes()):
            # Crea una nueva matriz ADN aleatoria
            while(self.detectar_mutantes()):
                for i in range(len(self.adn)):
                    self.adn[i] = [random.choice(['A', 'T', 'C', 'G']) for j in range(len(self.adn[i]))]
            return self.adn
        else:
            # Devuelve la misma matriz ADN
            print("No hay mutantes")
            return self.adn
    
    
    
