def resolve_carrier_signal_HPF(signal, HPFk = 0.7):
    s = len(signal)
    newSig = [0] * s

    for a in range(s):
        if a == 0:
            newSig[a] = signal[a]
        else:
            newSig[a] = HPFk * newSig[a - 1] + (HPFk * (signal[a] - signal[a-1]))
    return newSig