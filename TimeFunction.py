import numpy as np
import matplotlib.pyplot as plt

# Define the corrected logarithmic decay function
def corrected_log_decay_function(t):
    return np.log(1 + 24 - t) / np.log(25)

# Generate data points for the function
t_values = np.linspace(0, 24, 100)
weights = corrected_log_decay_function(t_values)

# Plot the corrected function
plt.figure(figsize=(8, 6))
plt.plot(t_values, weights, label='Corrected Logarithmic Decay Function', color='blue')
plt.title('Corrected Logarithmic Decay of Weighting Over Time')
plt.xlabel('Time (months)')
plt.ylabel('Weighting')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()

from scipy.integrate import quad
import numpy as np

# Define the corrected logarithmic decay function
def corrected_log_decay_function(t):
    return np.log(1 + 24 - t) / np.log(25)

# Perform the definite integral of the function from 0 to 24
integral_result, _ = quad(corrected_log_decay_function, 0, 24)

# Print the result of the integral
print(f"The result of the integral is: {integral_result}")

import numpy as np
import matplotlib.pyplot as plt

# Define the function ln(3-t)/ln(3)
def log_decay_simple(t):
    return np.log(3 - t) / np.log(3)

# Generate data points for t in the range of 0 to 3 (as 3-t must be positive)
t_values = np.linspace(0, 2, 100, endpoint=False)  # Avoid reaching t=3 where log(0) is undefined
weights = log_decay_simple(t_values)

# Plot the function
plt.figure(figsize=(8, 6))
plt.plot(t_values, weights, label='Logarithmic Function: ln(3-t)/ln(3)', color='blue')
plt.title('Graph of ln(3-t)/ln(3)')
plt.xlabel('t')
plt.ylabel('Weighting')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()
