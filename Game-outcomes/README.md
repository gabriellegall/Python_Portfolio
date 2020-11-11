# Code
```
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

nMax   = 11 # Maximum number of hidden cards
kMax   = 5  # Maximum number of desired hidden cards (condition : k < n)
iMax   = 3  # Maximum number of draws

N = list(range(kMax,nMax+1))
K = list(range(1,kMax+1))
I = list(range(1,iMax+1))

def getproba(n,k,i): 
    pF = 1
    pX = 0
    for i in list(range(0,i)):                                                  # Loop over each draw
        pS   = pF * k/(n-i)                                                     # probability of a success at draw "i" given previous failure(s)
        pF   = pF * (n-k-i)/(n-i)                                               # probability of a failure at draw "i" given previous failure(s)
        pX   = pX + pS                                                          # probability of a success at any draw
    return pX                                                                   

for i in I:
    Results = np.zeros([len(N), len(K)])
    for k in K:
        for n in N:
            Results[n-kMax,k-1] = getproba(n, k, i)

    plt.figure(i)
    ax = sns.heatmap(Results, annot=True, vmin=0, vmax=1, xticklabels=K, yticklabels=N)
    ax.invert_yaxis()
    plt.title('Probability of a sucess with '+str(i)+' draws')
    plt.xlabel('Number of desired hidden cards (k)')
    plt.ylabel('Number of hidden cards (n)')
```
    
# Code 2
```
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

nMax   = 11 # Maximum number of hidden cards
kMax   = 5  # Maximum number of desired hidden cards (condition : k < n)
iMax   = 3  # Maximum number of draws

N = list(range(kMax,nMax+1))
K = list(range(1,kMax+1))
I = list(range(1,iMax+1))

def getproba(n,k,i): 
    pF = 1
    pX = 0
    for i in list(range(0,i)):                                                  # Loop over each draw
        pS   = pF * k/(n-i)                                                     # probability of a success at draw "i" given previous failure(s)
        pF   = pF * (n-k-i)/(n-i)                                               # probability of a failure at draw "i" given previous failure(s)
        pX   = pX + pS                                                          # probability of a success at any draw
    return pX                                                                   

TrackRecord = []
for i in I:
    for k in K:
        for n in N:
            TrackRecord.append([i,n,k,getproba(n, k, i)])                       # Keep track of the results
            
TrackRecord  = pd.DataFrame(TrackRecord,columns=(['i','n','k','pX']))
for i in I:
    plt.figure(i)
    TrackRecordi = TrackRecord[TrackRecord['i'] == i]
    TrackRecordi = TrackRecordi.pivot('n','k','pX')
    ax = sns.heatmap(TrackRecordi, annot=True, vmin=0, vmax=1, xticklabels=K, yticklabels=N)
    ax.invert_yaxis()
    plt.title('Probability of a sucess with '+str(i)+' draws')
    plt.xlabel('Number of desired hidden cards (k)')
    plt.ylabel('Number of hidden cards (n)')
```
