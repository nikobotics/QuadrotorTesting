import numpy as mpy
import matplotlib.pyplot as pyplot
from noise import pnoise1
from enum import Enum

SIZE = 800

class NoiseType(Enum):
    STD_NORMAL = 1
    PERLIN = 2

def resolve_carrier_signal(signal):
    """
    Uses filtering to resolve the carrier signal
    """
    return [0]

def low_pass_filter(signal, tau = 16):
    size = len(signal)
    filtered_signal = []
    for n in range(size):
        if n == 0:
            filtered_signal.append(signal[0])
        else:
            val = ((1 - (1 / tau)) * filtered_signal[n - 1]) + ((1 / tau) * signal[n])
            filtered_signal.append(val)
    return clip_list_at(filtered_signal)

def crappy_test_filter(signal):
    size = len(signal)
    filtered_signal = []
    rand_sig = get_random_signal(size, NoiseType.STD_NORMAL)
    for n in range(size):
        filtered_signal.append(signal[n] - rand_sig[n])
    return clip_list_at(filtered_signal)

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
    noise = []
    rand_base = mpy.random.randint(0, 256)
    for n in range(len):
        val = (5 * n) / SIZE - 2.5
        noise.append(pnoise1(val + rand_base))
    return noise

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
    sig = []
    for n in range(len):
        val = mpy.random.normal(0, 1, None)
        while not is_constrained(val):
            val = mpy.random.normal(0, 1, None)
        sig.append(val)
    return sig

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

def do_work():
    # Do math
    sigA = get_carrier_signal(SIZE, NoiseType.PERLIN)
    if (sigA != None):
        sigB = get_random_signal(SIZE, NoiseType.STD_NORMAL)
        if (sigB != None):
            full_signal = add_signals(sigA, sigB)
            full_signal = clip_list_at(full_signal)
            #extracted_signal = resolve_carrier_signal(full_signal)
            extracted_signal = low_pass_filter(full_signal)
            deviation = find_signal_deviation(sigA, extracted_signal)
            effect = find_carrier_signal_effectiveness(deviation)
        else:
            print("UNRESOLVED RANDOM SIGNAL TYPE\n")
            return
    else:
        print("UNRESOLVED CARRIER SIGNAL TYPE\n")
        return

    # Plot signals
    
    pyplot.plot(full_signal)
    pyplot.plot(extracted_signal)
    pyplot.plot(sigA)

    print("Effect Index: " + str(effect * 100) + "\n")
    pyplot.show()

do_work()
