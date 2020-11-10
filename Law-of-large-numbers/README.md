# Code
```
import numpy as np
import matplotlib.pyplot as plt 

N       = 1000                                                                  # Maximum number of simulations (and maximum sample size)
minVal  = 0                                                                     # Random variable minimum value
maxVal  = 1                                                                     # Random variable maximum value
Mu      = (minVal+maxVal)/2                                                     # Store the theoretical mean

Results = np.zeros([N, 2])                                                      # Create an array to store all results

for i in range(N):
    Results[i,0] = i+1                                                          # Store the sample size                                     
    Results[i,1] = np.random.uniform(low=minVal,high=maxVal,size=i+1).mean()    # Calculate and store the average of the sample with size i

plt.plot(Results[:,0],Results[:,1])                                             # Plot the results
plt.axhline(y=Mu, color='r', linestyle='-')                                     # Add a reference line for the theoretical mean
```

# Code 2
```
import matplotlib.pyplot as plt 
import numpy as np

N       = 1000                                                                  # Maximum number of simulations (and maximum sample size)
minVal  = 0                                                                     # Random variable minimum value
maxVal  = 1                                                                     # Random variable maximum value
Mu      = (minVal+maxVal)/2                                                     # Store the theoretical mean

x       = list(range(1,N+1))                                                    # Create a list with all sample sizes
y       = [np.random.uniform(low=minVal,high=maxVal,size=i).mean() for i in x]  # Calculate and store the average of the sample with size i

plt.plot(x,y)                                                                   # Plot the results
plt.axhline(y=Mu, color='r', linestyle='-')                                     # Add a reference line for the theoretical mean
```
