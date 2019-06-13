import numpy as mpy
import noiseType
import signalOperations

zk = 0 # Observation at t = k
Z_k = [] # Set of Observations up to and including k

xk = [] # System state vector at t = k
xeki = [] # System state estimation at t = k based on some t = i
xekk = [] # System estimation error
Pk = [] # Covariance matrix
Fk = [] # State transition matrix
Hk = [] # Output transition matrix
wk = [0, 0] # process (or system or plant) noise vector
vk = [] # measurement noise vector
Qk = [] # process (or system or plant) noise covariance matrix
Rk = [] # measurement noise covariance matrix
Kk = [] # Kalman gain matrix
vk = [] # Innovation at time t = k
sk = [] # Innovation covariance matrix at time t = k

Gk = [] # Input control (transition) matrix
uk = [] # Input control vector

"""
TWO Options:
    - Define the input matrix as signal [Ax, Ay, Az] (Acceleration axes), or
    - Given signal a(t), use signal [a, da/dt] as input vector
Trying option 2 for now, because it's easiest to implement and less dependent on other noise.
"""

def resolve_carrier_signal_KALMAN(signal):
    """
    Uses filtering to resolve the carrier signal
    """

    return signal





