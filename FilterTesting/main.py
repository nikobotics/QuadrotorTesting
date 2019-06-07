import numpy as mpy
import matplotlib.pyplot as pyplot
from noise import pnoise1
from enum import Enum
from lpf import resolve_carrier_signal_LPF
from kalman import resolve_carrier_signal_KALMAN
from noiseType import NoiseType
import signalOperations as so
from parameters import SIZE
from computeFilter import computeFilter

def do_work():
    # Generate useful carrier signal
    carrierSig = so.get_carrier_signal(SIZE, NoiseType.PULSE)

    if (carrierSig != None):
        # Generate noise
        randSig = so.get_random_signal(SIZE, NoiseType.STD_NORMAL)
        if (randSig != None):
            # Generate full noisy signal
            full_signal = so.generate_dirty_signal(carrierSig, randSig)

            # Filter out noise from original noisy signal
            computation = computeFilter(full_signal)

            # Analyze effect of filter
            lpf_sig = computation[1]
            extracted_signal = computation[0]
            
            deviation = so.find_signal_deviation(carrierSig, extracted_signal)
            effect = so.find_carrier_signal_effectiveness(deviation)
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
    pyplot.axis([0, SIZE, -1.0, 1.0])
    pyplot.title("Effective Signal Filtering")
    pyplot.ylabel("Full Signal and Low Pass Adjustment")

    pyplot.subplot(3, 1, 2)
    pyplot.plot(extracted_signal)
    pyplot.plot(carrierSig)
    pyplot.axis([0, SIZE, -1.0, 1.0])
    pyplot.ylabel("Resolved Signal and Carrier Signal")

    pyplot.subplot(3, 1, 3)
    pyplot.axis([0, SIZE, 0.0, 1.0])
    pyplot.plot(deviation)
    pyplot.ylabel("Abs. Signal error |e(t)|")

    print("Effect Index: " + str(effect * 100) + "\n")
    pyplot.show()

do_work()