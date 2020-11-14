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

# Code 3

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

pdAllRecord = pd.DataFrame()

for i in I:
    Record = []
    for k in K:
        for n in N:
            Record.append([i,n,k,getproba(n, k, i)])                       # Keep track of the results
            
    pdRecord = pd.DataFrame(Record,columns=(['i','n','k','pX']))
    pdAllRecord.append(pdRecord)

    plt.figure(i)
    ax = sns.heatmap(pdRecord.pivot('n','k','pX'), annot=True, vmin=0, vmax=1)
    ax.invert_yaxis()
    plt.title('Probability of a sucess with '+str(i)+' draws')
    plt.xlabel('Number of desired hidden cards (k)')
    plt.ylabel('Number of hidden cards (n)')
```
# Code 4
```
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import itertools

max_nb_hidden_cards     = 11
max_nb_desired_cards    = 5
max_nb_draws            = 3

nb_hidden_cards         = list(range(max_nb_desired_cards,max_nb_hidden_cards+1))
nb_desired_cards        = list(range(1,max_nb_desired_cards+1))
nb_draws                = list(range(1,max_nb_draws+1))

def get_proba_success(hidden_cards,desired_cards,draws): 
    proba_failure               = 1
    proba_success               = 0
    for i in list(range(0,draws)):
        proba_success_step      = proba_failure*desired_cards/(hidden_cards-i) 
        proba_failure           = proba_failure*(hidden_cards-desired_cards-i)/(hidden_cards-i)
        proba_success           = proba_success+proba_success_step                                    
    return proba_success                                                             

results = pd.DataFrame(itertools.product(nb_draws, nb_desired_cards, nb_hidden_cards), columns=('nb_draws', 'nb_desired_cards', 'nb_hidden_cards'))
results['proba_success'] = [get_proba_success(n, k, i) for i, k, n in results[['nb_draws', 'nb_desired_cards', 'nb_hidden_cards']].values]

for i in nb_draws:
    plt.figure(i)
    ax = sns.heatmap(results[results['nb_draws']==i].pivot('nb_hidden_cards','nb_desired_cards','proba_success'), annot=True, vmin=0, vmax=1)
    ax.invert_yaxis()
    plt.title('Probability of at least a sucess with '+str(i)+' draws')
    plt.xlabel('Number of desired hidden cards')
    plt.ylabel('Number of hidden cards')
```

[bp](https://stackoverflow.com/questions/26309962/appending-a-list-or-series-to-a-pandas-dataframe-as-a-row)
