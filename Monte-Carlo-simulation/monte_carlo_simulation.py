import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# parameters
min_growth      = 0.05
likely_growth   = 0.1
max_growth      = 0.15
min_margin      = 0.05
likely_margin   = 0.1
max_margin      = 0.15

revenue         = 23.5
strike_prices   = [2, 2.5, 2.5]
# strike_prices = [2.5, 3, 3, 3.5, 3.5]
discount_rate   = 0.12
nb_simulations  = 1000000

# simulations
revenues        = pd.DataFrame([[revenue]], index=range(0,nb_simulations))
op_income       = pd.DataFrame()
payoff          = pd.DataFrame()
pv_payoff       = pd.DataFrame()
earnout_value   = pd.DataFrame()

for i in range(1,len(strike_prices)+1):

    growths           = pd.DataFrame(np.random.triangular(min_growth, likely_growth, max_growth, nb_simulations))
    margins           = pd.DataFrame(np.random.triangular(min_margin, likely_margin, max_margin, nb_simulations))
 
    revenues[i]       = revenues[i-1]*(1+growths[0])      
    op_income[i]      = revenues[i] * margins[0]
    payoff[i]         = op_income[i] - strike_prices[i-1]
    payoff[payoff<0]  = 0
    pv_payoff[i]      = payoff[i] / (1+discount_rate) ** i
    
earnout_value[0] = pv_payoff.sum(axis=1)

# analysis
earnout_value_stats = earnout_value.describe()

# plot
fig, ax = plt.subplots(figsize = (16, 9))
earnout_value.hist(bins=100, ax=ax)
ax.set_title('Distribution of earnout valuations',pad=20)
ax.set_xlabel('earnout valuation (K$)',color='grey')
ax.set_ylabel('number of results',color='grey')
ax.spines['top'].set_color('lightgrey')
ax.spines['right'].set_color('lightgrey')
ax.spines['bottom'].set_color('lightgrey')
ax.spines['left'].set_color('lightgrey')
ax.tick_params(axis='x', colors='grey')
ax.tick_params(axis='y', colors='grey')
ax.grid(False)
