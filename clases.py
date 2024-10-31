import random

class Detector:

    def __init__(self, adn):
        self.adn = adn
        self.__cantidad_mutantes_horizontales = 0
        self.__cantidad_mutantes_verticales = 0
        self.__cantidad_mutantes_diagonales = 0
    
    __cantidad_mutantes_horizontales = 0
    __cantidad_mutantes_verticales = 0
    __cantidad_mutantes_diagonales = 0
    
    def mutante_horizontal(self):
    # Detectar mutante horizontal
        for i in range(len(self.adn)):
            for j in range(len(self.adn[i])-3):
                if self.adn[i][j] == self.adn[i][j+1] == self.adn[i][j+2] == self.adn[i][j+3]:
                    self.__cantidad_mutantes_horizontales += 1
                    return True
        return False

    def mutante_vertical(self):
        # Detectar mutante vertical
        for i in range(len(self.adn)-3):
            for j in range(len(self.adn[i])):
                if self.adn[i][j] == self.adn[i+1][j] == self.adn[i+2][j] == self.adn[i+3][j]:
                    self.__cantidad_mutantes_verticales += 1
                    return True
        return False

    def mutante_diagonal(self):
        # Detectar mutante diagonal
        for i in range(len(self.adn)-3):
            for j in range(len(self.adn[i])-3):
                if self.adn[i][j] == self.adn[i+1][j+1] == self.adn[i+2][j+2] == self.adn[i+3][j+3]:
                    self.__cantidad_mutantes_diagonales += 1
                    return True
        return False

    
    def detectar_mutantes(self):
        return self.mutante_horizontal() or self.mutante_vertical() or self.mutante_diagonal()
    
    def imprimir_cantidad_mutantes(self):
        # Imprime la cantidad de mutantes
        print("Cantidad de mutantes horizontales: ", self.__cantidad_mutantes_horizontales)
        print("Cantidad de mutantes verticales: ", self.__cantidad_mutantes_verticales)
        print("Cantidad de mutantes diagonales: ", self.__cantidad_mutantes_diagonales)
        
    def devolver_adn(self):
        # Devuelve el ADN
        return self.adn
    
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
    
class Sanador(Detector):
    def __init__(self, adn):
        super().__init__(adn)
    
    def verificar_mutantes(self):
        return self.detectar_mutantes()
    
    def sanar_mutantes(self):
        if(self.verificar_mutantes()):
            # Crea una nueva matriz ADN aleatoria
            while(self.verificar_mutantes()):
                for i in range(len(self.adn)):
                    self.adn[i] = [random.choice(['A', 'T', 'C', 'G']) for j in range(len(self.adn[i]))]
            return self.adn
        else:
            # Devuelve la misma matriz ADN
            print("No hay mutantes")
            return self.adn
    
    
    
