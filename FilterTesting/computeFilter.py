import signalOperations as so
from lpf import resolve_carrier_signal_LPF
from kalman import resolve_carrier_signal_KALMAN

def computeFilter(noisySignal):
    lpf_sig = resolve_carrier_signal_LPF(noisySignal)
    extracted_signal = resolve_carrier_signal_KALMAN(lpf_sig)
    return extracted_signal, lpf_sig