from numpy import array

class Particle(object):

    def __init__(self, **kwargs):
        self._name = kwargs['name']
        self._mass = kwargs['mass']
        
        self._position = kwargs['position'] if 'position' in kwargs \
                            else array([0, 0])
        self._momentum = kwargs['momentum'] if 'momentum' in kwargs \
                            else array([0, 0])

    @property
    def name(self):
        return self._name
    
    @property
    def mass(self):
        return self._mass
    
    @property
    def position(self):
        return self._position
        
    @position.setter
    def position(self, value):
        self._position = value
        
    @property
    def momentum(self):
        return self._momentum

    @momentum.setter
    def momentum(self, value):
        self._momentum = value
