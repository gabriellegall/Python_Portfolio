# Code 

```
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt 

Sizes = 30                                                                      # Maximum sample size to be tested
Draws = 1000                                                                    # Number of times we draw the average - for each sample size
Alpha = 0.01                                                                    # Significance level

AlltStat = []                                                                   # Create a list to store all tstats
AllSizes = range (1,Sizes+1)
for j in AllSizes:                                                              # Loop through each sample size
    Averages = [np.mean(np.random.randint(2, size=j)) for i in range(0,Draws)]  # Store the average as many times as specified in the Draws variable
    tStat,_ = scipy.stats.jarque_bera(Averages)                                 # Test for the normality and get the tStat result
    AlltStat.append(tStat)                                                      # Store the tStat result
    
plt.plot(AllSizes,AlltStat)                                                     # Plot the tStat results
tCrit = scipy.stats.chi2.isf(Alpha, 2)                                          # Get the critical value for the test statistic (Chi² distribution with 2df)
plt.axhline(y=tCrit, color='r', linestyle='-',label=r'$\alpha$ ='+str(Alpha))   # Add a reference line for the significance level
plt.title('tStats for the JB test ('+str(Draws)+' draws)')                      # Add title
plt.xlabel('Sample size')                                                       # Add x label
plt.ylabel('tStat')                                                             # Add y label
plt.legend()                                                                    # Plot the label defined previously
```

# Code 2

```
import numpy as np
import matplotlib.pyplot as plt 

Sizes = [1,2,5,10,30,50]
Draws = 1000
fig, axs = plt.subplots(1,6)

c=0
for j in Sizes:
    Averages = [np.mean(np.random.randint(2, size=j)) for i in range(0,Draws)]
    
    plt.axes(axs[c])
    plt.hist(Averages,bins=50)
    plt.title('N = '+str(j))  
    plt.xticks(np.arange(0, 1, step=0.25))

    xleft, xright = axs[c].get_xlim()
    ybottom, ytop = axs[c].get_ylim()
    axs[c].set_aspect(abs((xright-xleft)/(ybottom-ytop))*1)
    
    axs[c].spines['top'].set_visible(False)
    axs[c].spines['right'].set_visible(False)
    axs[c].spines['bottom'].set_color('lightgrey')
    axs[c].spines['left'].set_color('lightgrey')
    axs[c].tick_params(axis='x', colors='lightgrey')
    axs[c].tick_params(axis='y', colors='lightgrey')
    axs[c].title.set_color('grey')        
    
    c+=1
```
