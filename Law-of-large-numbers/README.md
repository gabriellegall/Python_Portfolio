# Code
```
import numpy as np
import matplotlib.pyplot as plt 

N       = 1000                                                                  # Maximum number of simulations (and maximum sample size)
minVal  = 0                                                                     # Random variable minimum value
maxVal  = 1                                                                     # Random variable maximum value
mu      = (minVal+maxVal)/2                                                     # Store the theoretical mean

Results = np.zeros([N+1, 2])                                                    # Create an array to store all results

for i in range(1,N+1):
    Results[i,0] = i                                                            # Store the sample size
    Results[i,1] = np.random.uniform(low=minVal,high=maxVal,size=i).mean()      # Calculate and store the average of the sample with size i
Results = np.delete(Results, (0), axis=0)                                       # Remove the first dummy row

plt.plot(Results[:,0],Results[:,1])                                             # Plot the results
plt.axhline(y=mu, color='r', linestyle='-')                                     # Add a reference line for the theoretical mean
```
