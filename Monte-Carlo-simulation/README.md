
# Code

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# Settings
Ga = 0.05                       # Minimum growth
Gb = 0.1                        # Most likely growth
Gc = 0.15                       # Maximum growth
Pa = 0.05                       # Minimum profit margin
Pb = 0.1                        # Most likely profit margin
Pc = 0.15                       # Maximum profit margin

R0 = 23.5                       # Revenue today
K  = [2, 2.5, 2.5]              # Strike prices in 1,2,3 years
# K  = [2.5, 3, 3, 3.5, 3.5]    # Strike prices in 1,2,3,4,5 years
D  = 0.12                       # Discount rate
N  = 1000000                    # Number of simulations

# Simulation
R       = pd.DataFrame([[R0]], index=range(0,N)) # Repeat R0 throughout N rows
O       = pd.DataFrame()        # Create an empty dataframe
P       = pd.DataFrame()        # Create an empty dataframe
PVP     = pd.DataFrame()        # Create an empty dataframe
E       = pd.DataFrame()        # Create an empty dataframe

for i in range(1,len(K)+1):                 # Loop for each future year : i = 1,2,..,len(K)

    RandG   = pd.DataFrame(np.random.triangular(Ga, Gb, Gc, N)) # Generate N growth random variables
    RandP   = pd.DataFrame(np.random.triangular(Pa, Pb, Pc, N)) # Generate N profit margin random variables
 
    R[i]    = R[i-1]*(1+RandG[0])           # Calculate the revenue at year i based on the previous year
    O[i]    = R[i] * RandP[0]               # Calculate the operating income at year i
    P[i]    = O[i] - K[i-1]                 # Calculate the payoff at year i (step 1)
    P[P<0]  = 0                             # Calculate the payoff at year i (step 2) : Max(P,0)
    PVP[i]  = P[i] / (1+D) ** i             # Discount the payoff to get the present value
    
E[0] = PVP.sum(axis=1)                      # Earnout values across N simulations

# Analysis
Summary = E.describe()

# Plot
E.hist(bins=100)
plt.title('Distribution of earnout valuations')                                 # Add title
plt.xlabel('Earnout valuations')                                                # Add x label
plt.ylabel('Number of results')                                                 # Add y label
                    

figure, axes = plt.subplots(nrows=1, ncols=2)                                   # Create two subplots
ratio = 1                                                                       # Define the aspect ratio of the plots

axes[0].hist(RandG.values,bins=100)                                             # Plot a histogram
axes[0].set_title('Growth variables')                                           # Set the titre
axes[0].tick_params(axis='both', which='major', labelsize=8)                    # Resize x and y labels
xleft, xright = axes[0].get_xlim()                                              # Get the x limits
ybottom, ytop = axes[0].get_ylim()                                              # Get the y limits
axes[0].set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)                    # Set the x and y axis square

axes[1].hist(RandP.values,bins=100)                                             # Plot a histogram
axes[1].set_title('Profit margin variables')                                    # Set the titre
axes[1].tick_params(axis='both', which='major', labelsize=8)                    # Resize x and y labels
xleft, xright = axes[1].get_xlim()                                              # Get the x limits
ybottom, ytop = axes[1].get_ylim()                                              # Get the y limits
axes[1].set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)                    # Set the x and y axis square

# Source square ratio : https://jdhao.github.io/2017/06/03/change-aspect-ratio-in-mpl/
```
