import random

class Detector:

    def __init__(self, adn):
        self.__adn = adn
        self.__cantidad_mutantes_horizontales = 0
        self.__cantidad_mutantes_verticales = 0
        self.__cantidad_mutantes_diagonales = 0
    
    __cantidad_mutantes_horizontales = 0
    __cantidad_mutantes_verticales = 0
    __cantidad_mutantes_diagonales = 0
    
    def mutante_horizontal(self):
    # Detectar mutante horizontal
        for i in range(len(self.__adn)):
            for j in range(len(self.__adn[i])-3):
                if self.__adn[i][j] == self.__adn[i][j+1] == self.__adn[i][j+2] == self.__adn[i][j+3]:
                    self.__cantidad_mutantes_horizontales += 1
                    return True
        return False

    def mutante_vertical(self):
        # Detectar mutante vertical
        for i in range(len(self.__adn)-3):
            for j in range(len(self.__adn[i])):
                if self.__adn[i][j] == self.__adn[i+1][j] == self.__adn[i+2][j] == self.__adn[i+3][j]:
                    self.__cantidad_mutantes_verticales += 1
                    return True
        return False

    def mutante_diagonal(self):
        # Detectar mutante diagonal
        for i in range(len(self.__adn)-3):
            for j in range(len(self.__adn[i])-3):
                if self.__adn[i][j] == self.__adn[i+1][j+1] == self.__adn[i+2][j+2] == self.__adn[i+3][j+3]:
                    self.__cantidad_mutantes_diagonales += 1
                    return True
        return False

    
    def detectar_mutantes(self):
        return self.mutante_horizontal() or self.mutante_vertical() or self.mutante_diagonal()
    
    def imprimir_cantidad_mutantes(self):
        print("Cantidad de mutantes horizontales: ", self.__cantidad_mutantes_horizontales)
        print("Cantidad de mutantes verticales: ", self.__cantidad_mutantes_verticales)
        print("Cantidad de mutantes diagonales: ", self.__cantidad_mutantes_diagonales)
        
    def devolver_adn(self):
        return self.__adn
    
class Mutador:
    def __init__(self, adn):
        self.adn = adn
        
    base_nitrogenada = []
    atributo_2 = 0
    atributo_3 = 0
    
    def crear_mutante(self, adn):
        pass
    
class Radiacion(Mutador):
    def __init__(self, adn):
        super().__init__(adn)
        
    def crear_mutante(self, base_nitrogenada, posicion_inicial, orientacion_de_la_mutacion):
        adn_mutada = []
        return adn_mutada
    
class Virus(Mutador):
    def __init__(self, adn):
        super().__init__(adn)
        
    def crear_mutante(self, base_nitrogenada, posicion_inicial):
        adn_mutada = []
        return adn_mutada
    
class Sanador:
    def __init__(self, adn):
        self.__adn = adn
    
    def sanar_mutantes(self):
        if(Detector(self.__adn).mutante_horizontal() or Detector(self.__adn).mutante_vertical() or Detector(self.__adn).mutante_diagonal()):
            while(Detector(self.__adn).mutante_horizontal() or Detector(self.__adn).mutante_vertical() or Detector(self.__adn).mutante_diagonal()):
                for i in range(len(self.__adn)):
                    self.__adn[i] = [random.choice(['A', 'T', 'C', 'G']) for j in range(len(self.__adn[i]))]
            return self.__adn
        else:
            print("No hay mutantes")
            return self.__adn
    
    
    
