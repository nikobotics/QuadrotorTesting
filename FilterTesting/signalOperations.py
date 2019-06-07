from parameters import SIZE
from noiseType import NoiseType
from noise import pnoise1
import random
import numpy as mpy

def get_carrier_signal(len = SIZE, carrier = NoiseType.STD_NORMAL):
    """
    Gets a carrier signal with the desired distribution (perlin-esque noise)
    Of Length len
    """
    if (carrier == NoiseType.STD_NORMAL):
        return __get_carrier_signal_STD_NORMAL(len)
    elif (carrier == NoiseType.PERLIN):
        return __get_carrier_signal_PERLIN(len)
    elif (carrier == NoiseType.STEP):
        return __get_carrier_signal_STEP(len)
    elif (carrier == NoiseType.PULSE):
        return __get_carrier_signal_PULSE(len)
    elif (carrier == NoiseType.UNIT_PULSE):
        return __get_carrier_signal_UNIT_PULSE(len)
    else:
        return None

def generate_dirty_signal(signalA, signalB):
    return clip_list_at(add_signals(signalA, signalB))

def is_constrained(testVal, lowerBound = -1, upperBound = 1):
    return (testVal >= lowerBound) and (testVal <= upperBound)

def clip_list_at(l, lowerBound = -1, upperBound = 1):
    new_l = []
    for n in range(len(l)):
        tVal = l[n]
        if not is_constrained(tVal, lowerBound, upperBound):
            if tVal < lowerBound:
                new_l.append(lowerBound)
            elif tVal > upperBound:
                new_l.append(upperBound)
        else:
            new_l.append(tVal)
    return new_l

def add_signals(sigA, sigB):
    """
    Adds two signals together
    """
    count = min(len(sigA), len(sigB))
    new_sig = []
    for n in range(count):
        new_sig.append(sigA[n] + sigB[n])
    return new_sig

def find_carrier_signal_effectiveness(deviation):
    """
    Returns average deviations from signal
    """
    l = len(deviation)
    if l == 0:
        return 0
    sum = 0
    for n in range(l):
        sum += deviation[n]
    return 1 - (sum / l)

def find_signal_deviation(carrier_signal, filtered_signal):
    """
    Returns list of deviations
    """
    count = min(len(carrier_signal), len(filtered_signal))
    deviation = []
    for n in range(count):
        deviation.append(abs(filtered_signal[n] - carrier_signal[n]))
    return deviation


def __get_carrier_signal_STD_NORMAL(len = SIZE):
    """
    Gets a carrier signal with STD NORMAL perlin-esque noise
    Of Length len
    """
    return __get_random_signal_STD_NORMAL(len)

def __get_carrier_signal_PERLIN(len = SIZE):
    """
    Gets a carrier signal with typical perlin-esque noise
    Of Length len
    """
    noise = []
    rand_base = mpy.random.randint(0, 256)
    for n in range(len):
        val = (5 * n) / SIZE - 2.5
        noise.append(pnoise1(val + rand_base))
    return noise

def __get_carrier_signal_STEP(len = SIZE, wait = 100):
    noise = []
    for n in range(len):
        if (n < wait):
            noise.append(0)
        else:
            noise.append(1)
    return noise

def __get_carrier_signal_UNIT_PULSE(len = SIZE, wait = 100):
    noise = []
    for n in range(len):
        if n == wait:
            noise.append(1)
        else:
            noise.append(0)
    return noise

def __get_carrier_signal_PULSE(len = SIZE, wait = 100, width = 100):
    noise = []
    for n in range(len):
        if n < wait or n > (wait + width):
            noise.append(0)
        else:
            noise.append(1)
    return noise

def get_random_signal(len = SIZE, t = NoiseType.STD_NORMAL):
    """
    Gets a random signal with the desired random signal distribution
    Of Length len
    """
    if (t == NoiseType.STD_NORMAL):
        return __get_random_signal_STD_NORMAL(len)
    elif (t == NoiseType.NONE):
        return __get_random_signal_NONE(len)
    elif (t == NoiseType.PSEUDO_RAND):
        return __get_random_signal_PSEUDO(len)
    else:
        return None

def __get_random_signal_STD_NORMAL(len = SIZE):
    """
    Gets a random signal with STD NORMAL distribution of length len
    """
    sig = []
    for n in range(len):
        val = mpy.random.normal(0, 1, None)
        while not is_constrained(val):
            val = mpy.random.normal(0, 1, None)
        sig.append(val)
    return sig

def __get_random_signal_NONE(len = SIZE):
    return [0] * len

def __get_random_signal_PSEUDO(len = SIZE):
    sig = []
    for n in range(len):
        sig.append((random.randint(0, 200) - 100) / 100)
    return sig