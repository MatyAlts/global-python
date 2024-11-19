import random

class Detector:
    """
    Encargada de detectar mutantes en el ADN
    """
    __cantidad_mutantes_horizontales = 0
    __cantidad_mutantes_verticales = 0
    __cantidad_mutantes_diagonales = 0
    
    def __init__(self, adn: list) -> None:
        self.adn = adn
        
    def __str__(self) -> str:
        self.mutante_horizontal()
        self.mutante_vertical()
        self.mutante_diagonal()
        return f"""
                Mutantes horizontales: {self.__cantidad_mutantes_horizontales}
                Mutantes verticales: {self.__cantidad_mutantes_verticales}
                Mutantes diagonales: {self.__cantidad_mutantes_diagonales}
                """
    
    def mutante_horizontal(self) -> bool:
    # Detectar mutante horizontal
        mutacion_encontrada = False
        for i in range(len(self.adn)):
            for j in range(len(self.adn[i])-3):
                if self.adn[i][j] == self.adn[i][j+1] == self.adn[i][j+2] == self.adn[i][j+3]:
                    self.__cantidad_mutantes_horizontales += 1
                    mutacion_encontrada = True
        return mutacion_encontrada

    def mutante_vertical(self) -> bool:
        # Detectar mutante vertical
        mutacion_encontrada = False
        for i in range(len(self.adn)-3):
            for j in range(len(self.adn[i])):
                if self.adn[i][j] == self.adn[i+1][j] == self.adn[i+2][j] == self.adn[i+3][j]:
                    self.__cantidad_mutantes_verticales += 1
                    mutacion_encontrada = True
        return mutacion_encontrada

    def mutante_diagonal(self) -> bool:
        # Detectar mutante diagonal
        mutacion_encontrada = False
        for i in range(len(self.adn)-3):
            for j in range(len(self.adn[i])-3):
                if self.adn[i][j] == self.adn[i+1][j+1] == self.adn[i+2][j+2] == self.adn[i+3][j+3]:
                    self.__cantidad_mutantes_diagonales += 1
                    mutacion_encontrada = True
        return mutacion_encontrada

    
    def detectar_mutantes(self) -> bool:
        return self.mutante_horizontal() or self.mutante_vertical() or self.mutante_diagonal()
        
    def devolver_adn(self) -> list:
        # Devuelve el ADN
        return self.adn
    
class Mutador:
    """
    Encargada de crear mutantes en el ADN
    """
    base_nitrogenada = ['A', 'C', 'G', 'T']
    longitud_mutacion = 4
    fila = 0
    columna = 0
    
    def __init__(self, adn: list) -> None:
        self.adn = adn
    
    
    def crear_mutante(self, posicion_inicial: int, orientacion_de_la_mutacion: str) -> list:
        pass
    
class Radiacion(Mutador):
    """
    Heredada de la clase Mutador
    Encargada de crear mutantes horizontales y verticales
    """
    def __init__(self, adn: list) -> None:
        super().__init__(adn)
        
    def crear_mutante(self, base:int, posicion_inicial: tuple, orientacion_de_la_mutacion: str) -> list:
        self.fila, self.columna = posicion_inicial
        adn_mutada = [list(fila) for fila in self.adn]
        if orientacion_de_la_mutacion == 'horizontal':
            if self.columna + self.longitud_mutacion > len(self.adn[0]):
                raise ValueError("La posición inicial y la longitud de la mutación exceden los límites de la matriz ADN.")
            for i in range(self.longitud_mutacion):
                adn_mutada[self.fila][self.columna + i] = self.base_nitrogenada[base]
        elif orientacion_de_la_mutacion == 'vertical':
            if self.fila + self.longitud_mutacion > len(self.adn):
                raise ValueError("La posición inicial y la longitud de la mutación exceden los límites de la matriz ADN.")
            for i in range(self.longitud_mutacion):
                adn_mutada[self.fila + i][self.columna] = self.base_nitrogenada[base]
        
        return adn_mutada

class Virus(Mutador):
    """
    Heredada de la clase Mutador
    Encargada de crear mutantes diagonales
    """
    def __init__(self, adn: list) -> None:
        super().__init__(adn)
        
    def crear_mutante(self, base:int, posicion_inicial: tuple) -> list:
        self.fila, self.columna = posicion_inicial
        adn_mutada = [list(row) for row in self.adn]

        if self.fila < 0 or self.columna < 0 or self.fila + self.longitud_mutacion > len(self.adn) or self.columna + self.longitud_mutacion > len(self.adn[0]):
            raise ValueError("La posición inicial y la longitud de la mutación exceden los límites de la matriz ADN.")

        for i in range(self.longitud_mutacion):
            adn_mutada[self.fila + i][self.columna + i] = self.base_nitrogenada[base]

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
    
    
    
