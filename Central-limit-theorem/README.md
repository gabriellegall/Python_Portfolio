# Code 

```
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt 

Sizes = 100                                                                     # Maximum sample size to be tested
Draws = 500                                                                     # Number of times we draw the average - for each sample size

AlltStat = []                                                                   # Create a list to store all tstats
for j in range (1,Sizes):                                                       # Loop through each sample size
    Sample = [np.mean(np.random.randint(2, size=j)) for i in range(0,Draws)]    # Store the average 
    tStat,_ = scipy.stats.jarque_bera(Sample)                                   # Test for the normality and get the tStat result
    AlltStat.append(tStat)                                                      # Store the tStat result

plt.plot(AlltStat)                                                              # Plot the tStat results
```
