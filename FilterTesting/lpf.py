from signalOperations import clip_list_at
from parameters import SIZE
from noiseType import NoiseType

def resolve_carrier_signal_LPF(signal, tau = 18):
    size = len(signal)
    filtered_signal = []
    for n in range(size):
        if n == 0:
            filtered_signal.append(signal[0])
        else:
            val = ((1 - (1 / tau)) * filtered_signal[n - 1]) + ((1 / tau) * signal[n])
            filtered_signal.append(val)
    return clip_list_at(filtered_signal)
