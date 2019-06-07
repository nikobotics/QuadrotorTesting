from parameters import SIZE
from noiseType import NoiseType
import signalOperations

def crappy_test_filter(signal):
    size = len(signal)
    filtered_signal = []
    rand_sig = signalOperations.get_random_signal(size, NoiseType.STD_NORMAL)
    for n in range(size):
        filtered_signal.append(signal[n] - rand_sig[n])
    return signalOperations.clip_list_at(filtered_signal)