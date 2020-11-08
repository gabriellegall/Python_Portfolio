Source : https://en.wikipedia.org/wiki/Binomial_test

```
import scipy
import numpy as np
import matplotlib.pyplot as plt 

N = 235                                                                         # Number of draws
p = 1/6                                                                         # Probability that the event occurs

Results = np.zeros(shape=(N+1,4))                                               # Create an array to store all results                            

for k in range(0,N+1):
    pK = scipy.stats.binom.pmf(k, N, p)                                         # P(X=k)       Probability that the event X with probability p occurs k times in N draws
    Results[k,[0,1]] = [k,pK]                                                   # k, P(X=k)  : Generate the pdf (probability density function)
Results[:,2] = np.cumsum(Results[:,1])-Results[:,1]                             # P(X<k)     : Generate the cdf (cumulative pdf), i.e. the probability to obtain lower results than the current one
Results[:,3] = 1-Results[:,2]                                                   # P(X>=k)    : Generate the inverse cdf, i.e. the probability to obtain equal or more extreme results than the current one

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

pValue2 = Results[51,3]                                                         # Probability to obtain equal or more extreme results than 51 times the event
pValue1 = scipy.stats.binom_test(51,N,p, alternative='greater')                 # Probability to obtain equal or more extreme results than 51 times the event (using the function)

# Best Practice
# https://stackoverflow.com/questions/568962/how-do-i-create-an-empty-array-matrix-in-numpy
```
