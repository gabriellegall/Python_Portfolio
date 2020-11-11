Adapter le code pour utiliser un dictionnaire

# Code
```
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

url = 'https://raw.githubusercontent.com/gabriellegall/Python_Portfolio/main/data/sp500_stock_returns.csv'
RawData = pd.read_csv(url, error_bad_lines=False)

Y = RawData.drop(['Date','SP_500'], axis=1).pct_change().iloc[1:]               # Calculate the % change for all stocks and remove the first row
X = RawData[['SP_500']].pct_change().iloc[1:]                                   # Calculate the % change for S&P 500 and remove the first row

b   = np.array([])                                                              # Empty array for the regression coefficient Beta
bse = np.array([])                                                              # Empty array for the standard error of the regression coefficient Beta
t   = np.array([])                                                              # Empty array for the tStat of the regression coefficient Beta
p   = np.array([])                                                              # Empty array for the pValue of the regression coefficient Beta
r2  = np.array([])                                                              # Empty array for the adjusted R²

for column in Y:
    
    reg = sm.OLS(Y[column].values,sm.add_constant(X).values).fit()              # OLS model results
    b = np.append(b,reg.params[1])                                              # Store the regression coefficient Beta
    bse = np.append(bse,reg.bse[1])                                             # Store the standard error of the regression coefficient Beta
    t = np.append(t,reg.tvalues[1])                                             # Store the tStat of the regression coefficient Beta
    p = np.append(p,reg.pvalues[1])                                             # Store the pValue of the regression coefficient Beta
    r2 = np.append(r2,reg.rsquared_adj)                                         # Store the adjusted R²
    
    fig = sm.graphics.plot_fit(reg, 1)                                          # Plot fit against one regressor : x1
    plt.title(column+' Beta')                                                   # Add title
    plt.xlabel('S&P 500')                                                       # Add x label
    plt.ylabel('Stock Return')                                                  # Add y label
 ```

# Code 2
```
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

url = 'https://raw.githubusercontent.com/gabriellegall/Python_Portfolio/main/data/sp500_stock_returns.csv'
RawData = pd.read_csv(url, error_bad_lines=False)

Y = RawData.drop(['Date','SP_500'], axis=1).pct_change().iloc[1:]               # Calculate the % change for all stocks and remove the first row
X = RawData[['SP_500']].pct_change().iloc[1:]                                   # Calculate the % change for S&P 500 and remove the first row

b   = []                                                                        # Empty array for the regression coefficient Beta
bse = []                                                                        # Empty array for the standard error of the regression coefficient Beta
t   = []                                                                        # Empty array for the tStat of the regression coefficient Beta
p   = []                                                                        # Empty array for the pValue of the regression coefficient Beta
r2  = []                                                                        # Empty array for the adjusted R²

for column in Y:
    
    reg = sm.OLS(Y[column].values,sm.add_constant(X).values).fit()              # OLS model results
    b.append(reg.params[1])                                                     # Store the regression coefficient Beta
    bse.append(reg.bse[1])                                                      # Store the standard error of the regression coefficient Beta
    t.append(reg.tvalues[1])                                                    # Store the tStat of the regression coefficient Beta
    p.append(reg.pvalues[1])                                                    # Store the pValue of the regression coefficient Beta
    r2.append(reg.rsquared_adj)                                                 # Store the adjusted R²
    
    fig = sm.graphics.plot_fit(reg, 1)                                          # Plot fit against one regressor : x1
    plt.title(column+' Beta ='+str(round(reg.params[1],2)))                     # Add title
    plt.xlabel('S&P 500')                                                       # Add x label
    plt.ylabel('Stock Return')                                                  # Add y label
```
