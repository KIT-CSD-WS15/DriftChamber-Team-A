from driftchamber.core.configuration.configuration_option import ConfigurationOption
from driftchamber.core.configuration.configuration_option_validation import ConfigurationOptionValidation


configuration_specification = {
'Particle': [
    ConfigurationOption('mass',
                        'The mass of the particle in GeV.',
                        float,
                        [ConfigurationOptionValidation(
                            lambda value: value > 0,
                            'The mass of the particle must be positive.'
                        )],
                        p_isCompulsory=True),
    ConfigurationOption('name',
                        'The name of a particle.',
                        lambda value: str(value),
                        p_isCompulsory=True),
    ConfigurationOption('probability',
                        'The probability for noise per cell and event',
                        float,
                        [ConfigurationOptionValidation(
                            lambda value: value >= 0 and value <= 1,
                            'The probability must be a number between 0 and 1.'
                        )],
                        p_isCompulsory=True)
    ]
}