Source : https://en.wikipedia.org/wiki/Binomial_test

![illustration](https://github.com/gabriellegall/Python_Portfolio/blob/main/images/image1.PNG?raw=true)

```
import scipy
import numpy as np
import matplotlib.pyplot as plt 

# Settings
N       = 235                                                                   # Number of draws
p       = 1/6                                                                   # Probability that the event occurs
alpha   = 0.05                                                                  # Significance level

# Simulations
Results = np.zeros(shape=(N+1,4))                                               # Create an array to store all results                            
for k in range(0,N+1):
    pK = scipy.stats.binom.pmf(k, N, p)                                         # P(X=k)       Probability that the event X with probability p occurs k times in N draws
    Results[k,[0,1]] = [k,pK]                                                   # k, P(X=k)  : Generate the pdf (probability density function)
Results[:,2] = np.cumsum(Results[:,1])-Results[:,1]                             # P(X<k)     : Generate the cdf (cumulative pdf), i.e. the probability to obtain lower results than the current one
Results[:,3] = 1-Results[:,2]                                                   # P(X>=k)    : Generate the inverse cdf, i.e. the probability to obtain equal or more extreme results than the current one

# Plots
plt.figure(0)                                                                   # Declare the new figure
plt.plot(Results[:,1])                                                          # Plot the pdf
plt.title('Probability density function')                                       # Add title
plt.xlabel('k')                                                                 # Add x label
plt.ylabel('P(X=k)')                                                            # Add y label

plt.figure(2)                                                                   # Declare the new figure
plt.plot(Results[:,3])                                                          # Plot the inverse cdf
plt.title('Inverse cumulative probability density function')                    # Add title
plt.xlabel('k')                                                                 # Add x label
plt.ylabel('P(X>=k)')                                                           # Add y label
alphaIdx = np.abs(Results[:,3]-alpha).argmin()                                  # Row index corresponding to the closest inverse cdf value relative to the significance level
plt.vlines(alphaIdx, 0, 1, linewidth=1, colors ='red',                          # Add a reference line to the plot to identify the significance threshold
           label=' k='+str(alphaIdx)
           +' (alpha='+str(round(Results[alphaIdx,3],2))+')')                   # Set the label for the reference line
plt.legend()                                                                    # plot the label defined previously

# Hypothesis testing
pValue2 = Results[51,3]                                                         # Probability to obtain equal or more extreme results than 51 times the event
pValue1 = scipy.stats.binom_test(51,N,p, alternative='greater')                 # Probability to obtain equal or more extreme results than 51 times the event (using the function)

# Best Practice
# https://stackoverflow.com/questions/568962/how-do-i-create-an-empty-array-matrix-in-numpy
```
