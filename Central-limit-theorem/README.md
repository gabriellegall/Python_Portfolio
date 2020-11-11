# Code 

```
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt 

Sizes = 30                                                                      # Maximum sample size to be tested
Draws = 1000                                                                    # Number of times we draw the average - for each sample size
Alpha = 0.01                                                                    # Significance level

AlltStat = []                                                                   # Create a list to store all tstats
AllpValue = []

AllSizes = range (1,Sizes+1)
for j in AllSizes:                                                              # Loop through each sample size
    Sample = [np.mean(np.random.randint(2, size=j)) for i in range(0,Draws)]    # Store the average as many times as specified in the Draws variable
    tStat,_ = scipy.stats.jarque_bera(Sample)                                   # Test for the normality and get the tStat result
    AlltStat.append(tStat)                                                      # Store the tStat result
    
plt.plot(AllSizes,AlltStat)                                                     # Plot the tStat results
tCrit = scipy.stats.chi2.isf(Alpha, 2)                                          # Get the critical value for the test statistic (Chi² distribution with 2df)
plt.axhline(y=tCrit, color='r', linestyle='-')                                  # Add a reference line for the significance level
plt.title('tStats for the JB test ('+str(Draws)+' draws)')                      # Add title
plt.xlabel('Sample size')                                                       # Add x label
plt.ylabel('tStat')                                                             # Add y label
```
