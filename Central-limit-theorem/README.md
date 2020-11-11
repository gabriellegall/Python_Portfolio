# Code 

```
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt 

Sizes = 30                                                                      # Maximum sample size to be tested
Draws = 1000                                                                    # Number of times we draw the average - for each sample size
Alpha = 0.05                                                                    # Significance level

AlltStat = []                                                                   # Create a list to store all tstats
AllpValue = []
for j in range (1,Sizes+1):                                                     # Loop through each sample size
    Sample = [np.mean(np.random.randint(2, size=j)) for i in range(0,Draws)]    # Store the average 
    tStat,pValue = scipy.stats.jarque_bera(Sample)                              # Test for the normality and get the tStat result
    AlltStat.append(tStat)                                                      # Store the tStat result
    
plt.plot(AlltStat)                                                              # Plot the tStat results
tCrit = scipy.stats.chi2.isf(0.1, 2)                                            # Get the critical value for the test statistic (Chi² distribution with 2df)
plt.axhline(y=5.991, color='r', linestyle='-')                                  # Add a reference line for the significance level
plt.title('tStats for the JB test ('+str(Draws)+' draws)')                      # Add title
plt.xlabel('Sample size')                                                       # Add x label
plt.ylabel('tStat')                                                             # Add y label
```
