import unittest
import os

from testfixtures import LogCapture
from driftchamber.modules.ParticleGunModule.ParticleGunModule import ParticleGun
from driftchamber.core.datastore import DataStore, ObjectLifetime
from driftchamber.core.configuration.configuration import Configuration
from driftchamber.modules.ParticleGunModule.configuration_specification import configuration_specification



class ParticleGunTest(unittest.TestCase):
    """
    Test class for the ParticleGun class
    """
    def setUp(self):
        self.pathToConfgiFiles = os.path.dirname(os.path.abspath(__file__))
        self.pathToDefaultTestConfigFile = self.pathToConfgiFiles + '/particleGun_Electron.cfg'
        configuration = Configuration(self.pathToDefaultTestConfigFile, configuration_specification)
        self.datastore = DataStore()
        self.module = ParticleGun()
        self.datastore.put(self.module, configuration, ObjectLifetime.Application)


    def test_begin(self):
        with LogCapture() as l:
            self.module.begin(self.datastore)

            l.check(
                    ('root', 'INFO', "Begin of module 'ParticleGun'"),
                    ('root', 'WARNING', "ParticleGun hasn't found detector, set cells to default."),
                    ('root', 'INFO', "Particle gun initialized that shoots a 'electron'.")
            )

    def test_event(self):
        self.module.begin(self.datastore) #Execute begin method to set variables needed to execute event method
        self.module.event(self.datastore)
        for particle in self.datastore.get('Particles').get_all_particles():
            self.assertLessEqual(particle.position().pos()[0], self.module.cells)
            self.assertEqual(particle.position().pos()[1], 0)
            self.assertLessEqual(particle.momentum().mom()[0], self.module.particle_max_mom)
            self.assertLessEqual(particle.momentum().mom()[1], self.module.particle_max_mom)


    def test_end(self):
        with LogCapture() as l:
            self.module.end(self.datastore)

            l.check(
                    ('root', 'INFO', "End of module 'ParticleGun'")
            )

