import matplotlib.pyplot as plt 
import numpy as np

# Parameter
max_sample_size = 1000

# Simulation
sample_sizes    = list(range(1,max_sample_size+1))
sample_averages = [np.random.randint(2, size=i).mean() for i in sample_sizes]

# Plot
plt.plot(sample_sizes,sample_averages)
plt.axhline(y=0.5, color='r', linestyle='-')                                    # Add a reference line for the theoretical mean