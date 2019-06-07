import numpy as mpy
import matplotlib.pyplot as pyplot
from noise import pnoise1
from enum import Enum
from lpf import resolve_carrier_signal_LPF
from kalman import resolve_carrier_signal_KALMAN
from noiseType import NoiseType
import signalOperations

SIZE = 1000

def do_work():
    # Do math
    carrierSig = signalOperations.get_carrier_signal(SIZE, NoiseType.STEP)
    if (carrierSig != None):
        randSig = signalOperations.get_random_signal(SIZE, NoiseType.NONE)
        if (randSig != None):
            full_signal = signalOperations.add_signals(carrierSig, randSig)
            full_signal = signalOperations.clip_list_at(full_signal)
            lpf_sig = resolve_carrier_signal_LPF(full_signal)
            extracted_signal = resolve_carrier_signal_KALMAN(lpf_sig)
            deviation = signalOperations.find_signal_deviation(carrierSig, extracted_signal)
            effect = signalOperations.find_carrier_signal_effectiveness(deviation)
        else:
            print("UNRESOLVED RANDOM SIGNAL TYPE\n")
            return
    else:
        print("UNRESOLVED CARRIER SIGNAL TYPE\n")
        return

    # Plot signals
    pyplot.subplot(3, 1, 1)
    pyplot.plot(full_signal)
    pyplot.plot(lpf_sig)
    pyplot.title("Effective Signal Filtering")
    pyplot.ylabel("Full Signal and Low Pass Adjustment")

    pyplot.subplot(3, 1, 2)
    pyplot.plot(extracted_signal)
    pyplot.plot(carrierSig)
    pyplot.ylabel("Resolved Signal and Carrier Signal")

    pyplot.subplot(3, 1, 3)
    pyplot.plot(deviation)
    pyplot.ylabel("Abs. Signal error |e(t)|")


    print("Effect Index: " + str(effect * 100) + "\n")
    pyplot.show()

do_work()