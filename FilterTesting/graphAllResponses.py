import noiseType as n
import signalOperations as so
import computeFilter as f
from parameters import SIZE
import matplotlib.pyplot as pyplot

noise = n.NoiseType.PSEUDO_RAND

def graphAllResponses():
    carrierSigs = n.VALID_CARRIERS
    randomSig = so.get_random_signal(SIZE, noise)
    cnt = len(carrierSigs) / 2

    pyplot.title("Signal Responses")
    
    index = 0
    for carrier in carrierSigs:
        thisCarrier = so.get_carrier_signal(SIZE, carrier)
        thisNoisy = so.generate_dirty_signal(thisCarrier, randomSig)

        filterOut = f.computeFilter(thisNoisy)

        resolved = filterOut[0]

        pyplot.subplot(cnt, 2, index + 1)
        pyplot.plot(thisNoisy)
        pyplot.plot(resolved)
        if noise != n.NoiseType.NONE:
            pyplot.plot(thisCarrier)
        pyplot.axis([0, SIZE, -1.1, 1.1])

        deviation = so.find_signal_deviation(thisCarrier, resolved)
        effect = so.find_carrier_signal_effectiveness(deviation)
        pyplot.ylabel("Effect: " + str(round(effect * 100)))

        index += 1
    pyplot.show()


        


graphAllResponses()