import inline
import matplotlib

from scipy.optimize import curve_fit, fsolve
from scipy.constants import c, G, pi
import numpy as np
import matplotlib.pyplot as plt
import pickle

# A) The simulation

x = np.linspace(0, 2*pi, 101)
k = 2.
phi = pi/6.
# w/o err_floor, the err can be too small and can cause artificially large chi2 due to
# numerical instability.
err_floor = 0.1

# signal-to-noise ratio of 5.
y_true = np.sin(k*x + phi)

meas_err = np.abs(y_true)*0.2

err = np.sqrt( meas_err**2  + err_floor**2)
# err = err_floor*np.ones(len(x))


y = y_true + np.random.randn(x.shape[0])*err
plt.plot(x, y, '.')
plt.show()

print("hello")