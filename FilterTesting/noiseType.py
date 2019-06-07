from enum import Enum

class NoiseType(Enum):
    STD_NORMAL = 1
    PERLIN = 2
    STEP = 3
    NONE = 4
    PSEUDO_RAND = 5
    PULSE = 6
    UNIT_PULSE = 7

VALID_CARRIERS = [ NoiseType.PERLIN, NoiseType.PULSE, NoiseType.UNIT_PULSE, NoiseType.STEP ]
VALID_NOISE = [ NoiseType.STD_NORMAL, NoiseType.PSEUDO_RAND, NoiseType.NONE ]