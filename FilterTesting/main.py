import numpy as mpy
import matplotlib.pyplot as pyplot
from noise import pnoise1
from enum import Enum
from lpf import resolve_carrier_signal_LPF
from kalman import resolve_carrier_signal_KALMAN
from noiseType import NoiseType
import signalOperations as so
from parameters import SIZE, NUM_SENSORS, DETERMINE_EFFECTIVENESS_TRIALS
from computeFilter import computeFilter

carrier_noise = NoiseType.PERLIN
noise_type = NoiseType.PSEUDO_RAND

def do_work():
    effectiveness = 0
    for n in range(DETERMINE_EFFECTIVENESS_TRIALS):
        # Generate useful carrier signal
        if NUM_SENSORS == 1:
            carrierSig = so.get_carrier_signal(SIZE, carrier_noise)
        else:
            carrierSigs = so.get_signal_from_n_sensors(SIZE, carrier_noise, noise_type, NUM_SENSORS)
            carrierSig = carrierSigs[1]

        if (carrierSig != None):
            # Generate noise
            randSig = so.get_random_signal(SIZE, noise_type)
            if (randSig != None):
                # Generate full noisy signal
                if (NUM_SENSORS > 1):
                    full_signal = carrierSigs[0]
                else:
                    full_signal = so.generate_dirty_signal(carrierSig, randSig)

                # Filter out noise from original noisy signal
                computation = computeFilter(full_signal)

                # Analyze effect of filter
                lpf_sig = computation[1]
                extracted_signal = computation[0]
                
                rel_deviation = so.find_rel_signal_deviation(carrierSig, extracted_signal)
                deviation = so.find_signal_deviation(carrierSig, extracted_signal)
                effect = so.find_carrier_signal_effectiveness(deviation)
            else:
                print("UNRESOLVED RANDOM SIGNAL TYPE\n")
                return
        else:
            print("UNRESOLVED CARRIER SIGNAL TYPE\n")
            return

        effectiveness += effect
        print("\nDeviation Integral (Trial #" + str(n+1) + "): " + str(round(so.find_signal_integral(rel_deviation))))
        print("Effect (Trial #" + str(n+1) + "): " + str(round(effect * 100)))

    if (DETERMINE_EFFECTIVENESS_TRIALS == 1):
        # Plot signals
        pyplot.subplot(3, 1, 1)
        pyplot.plot(full_signal)
        pyplot.plot(lpf_sig)
        pyplot.axis([0, SIZE, -1.1, 1.1])
        pyplot.title("Effective Signal Filtering")
        pyplot.ylabel("Full Signal and Low Pass Adjustment")

        pyplot.subplot(3, 1, 2)
        pyplot.plot(extracted_signal)
        pyplot.plot(carrierSig)
        pyplot.axis([0, SIZE, -1.1, 1.1])
        pyplot.ylabel("Resolved Signal and Carrier Signal")

        pyplot.subplot(3, 1, 3)
        pyplot.axis([0, SIZE, 0.0, 2.0])
        pyplot.plot(deviation)
        pyplot.ylabel("Abs. Signal error |e(t)|")

        pyplot.show()
    else:
        print("\nTotal Effect Index: " + str(round(effectiveness * 100 / DETERMINE_EFFECTIVENESS_TRIALS)) + ", " + str(NUM_SENSORS) + " sensors.\n")

do_work()