import signalOperations as so
from lpf import resolve_carrier_signal_LPF
from kalman import resolve_carrier_signal_KALMAN
from rollingAvg import resolve_carrier_signal_ROLL_AVG
from highPassFilter import resolve_carrier_signal_HPF

def computeFilter(noisySignal):
    stage1 = resolve_carrier_signal_LPF(noisySignal, 18)
    #stage1 = resolve_carrier_signal_ROLL_AVG(noisySignal)
    extracted_signal = resolve_carrier_signal_KALMAN(stage1)
    return extracted_signal, stage1