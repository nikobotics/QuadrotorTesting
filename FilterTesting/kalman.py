import numpy as mpy
import matplotlib as pyplot
from enum import Enum

SIZE = 80

class NoiseType(Enum):
    STD_NORMAL = 1
    PERLIN = 2

def resolve_carrier_signal(signal):
    """
    Uses filtering to resolve the carrier signal
    """
    return [0]

def get_carrier_signal(len = SIZE, carrier = NoiseType.STD_NORMAL):
    """
    Gets a carrier signal with the desired distribution (perlin-esque noise)
    Of Length len
    """
    if (carrier == NoiseType.STD_NORMAL):
        return __get_carrier_signal_STD_NORMAL(len)
    elif (carrier == NoiseType.PERLIN):
        return __get_carrier_signal_PERLIN(len)
    else:
        return None

def __get_carrier_signal_STD_NORMAL(len = SIZE):
    """
    Gets a carrier signal with STD NORMAL perlin-esque noise
    Of Length len
    """
    return [0]

def __get_carrier_signal_PERLIN(len = SIZE):
    """
    Gets a carrier signal with typical perlin-esque noise
    Of Length len
    """
    return [0]

def get_random_signal(len = SIZE, t = NoiseType.STD_NORMAL):
    """
    Gets a random signal with the desired random signal distribution
    Of Length len
    """
    if (t == NoiseType.STD_NORMAL):
        return __get_random_signal_STD_NORMAL(len)
    else:
        return None

def __get_random_signal_STD_NORMAL(len = SIZE):
    """
    Gets a random signal with STD NORMAL distribution of length len
    """
    return [0]

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
    return sum / l

def find_signal_deviation(carrier_signal, filtered_signal):
    """
    Returns list of deviations
    """
    count = min(len(carrier_signal), len(filtered_signal))
    deviation = []
    for n in range(count):
        deviation.append(abs(filtered_signal[n] - carrier_signal[n]))
    return deviation

def do_work():
    # Do math
    sigA = get_carrier_signal(SIZE, NoiseType.STD_NORMAL)
    if (sigA != None):
        sigB = get_random_signal(SIZE)
        if (sigB != None):
            full_signal = add_signals(sigA, sigB)
            extracted_signal = resolve_carrier_signal(full_signal)
            deviation = find_signal_deviation(sigA, extracted_signal)
            effect = find_carrier_signal_effectiveness(deviation)
        else:
            print("UNRESOLVED RANDOM SIGNAL TYPE\n")
            return
    else:
        print("UNRESOLVED CARRIER SIGNAL TYPE\n")
        return

    # Plot signals

    

do_work()
