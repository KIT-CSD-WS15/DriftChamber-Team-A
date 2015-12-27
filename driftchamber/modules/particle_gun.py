from random import random, randint
from numpy import array
from driftchamber.core.module import Module
from driftchamber.data.particle import Particle

class ParticleGun(Module):

    def __init__(self, **kwargs):
        self._name = kwargs['name']
        self._mass = kwargs['mass']
        self._max_position_x = kwargs['max_position_x']
        self._max_position_y = kwargs['max_position_y']
        self._max_momentum = kwargs['max_momentum']

    def begin(self, datastore):
        mom_x = (random() - 0.5) * 2 * self._max_momentum
        mom_y = random() * self._max_momentum
        
        pos_x = randint(0, self._max_position_x)
        pos_y = randint(0, self._max_position_y)
        
        particle = Particle(name=self._name, mass=self._mass)
        particle.momentum = array([mom_x, mom_y])
        particle.position = array([pos_x, pos_y])
        
        datastore.put('particle', particle)
