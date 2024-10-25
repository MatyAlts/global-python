class Detector:

    def __init__(self, adn):
        self.adn = adn

    def detectar_mutantes(self, adn):
        pass
    
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
        self.adn = adn

    def sanar_mutantes(self, adn):
        return self.adn
    
    
    
