# Code 

```
import numpy as np
import random as rd
import scipy.stats
import matplotlib.pyplot as plt 

Pop     = np.random.randint(2, size=1000)                                       # Binary random variable (1 or 0)

N = 500                                                                         # Number of times we draw the average for each sample size
AlltStat = []                                                                   # Create a list to store all tstats

for j in range (1,100):                                                         # Look for each sample size
    Sample = [np.mean(rd.sample(Pop.tolist(),j)) for i in range(0,N)]           # Calculate an store the average N times for each sample size j
    tStat,_ = scipy.stats.jarque_bera(Sample)
    AlltStat.append(tStat)

plt.figure(0)                                                                   # Declare the new figure
plt.plot(AlltStat)
```
