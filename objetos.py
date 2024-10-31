from clases import *
matrices = {
    'adn_ejemplo' : [
        ['A', 'G', 'A', 'T', 'C', 'A'],
        ['G', 'A', 'T', 'T', 'C', 'A'],
        ['C', 'A', 'A', 'C', 'A', 'T'],
        ['G', 'A', 'G', 'C', 'T', 'A'],
        ['A', 'T', 'T', 'G', 'C', 'G'],
        ['C', 'T', 'G', 'T', 'T', 'C']
    ]
}

objetos_detector = {
    'adn_ejemplo' : Detector(matrices['adn_ejemplo']),
}

objetos_sanador = {
    'adn_ejemplo' : Sanador(matrices['adn_ejemplo']),
}
