import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import statsmodels.api as sm

url = 'https://raw.githubusercontent.com/gabriellegall/Python_Portfolio/main/data/sp500_stock_returns.csv'
data = pd.read_csv(url, error_bad_lines=False)

stocks_returns = data.drop(['Date','SP_500'], axis=1).pct_change().iloc[1:]               
market_returns = data[['SP_500']].pct_change().iloc[1:]

beta           = []
beta_std_error = []
test_statistic = []
p_value        = []
r_squared      = []

fig, axs = plt.subplots(1,3,figsize = (16, 9))
fig.tight_layout(pad=5)
fig.suptitle(r'$\beta$ coefficients for various companies (monthly)')

for stock, ax in zip(stocks_returns,axs):
    
    # linear regression
    linear_regression = sm.OLS(stocks_returns[stock].values,sm.add_constant(market_returns).values).fit()
    
    # regression results
    beta.append(linear_regression.params[1])
    beta_std_error.append(linear_regression.bse[1])
    test_statistic.append(linear_regression.tvalues[1])
    p_value.append(linear_regression.pvalues[1])
    r_squared.append(linear_regression.rsquared_adj)
    
    # plot the regressions
    sm.graphics.plot_fit(linear_regression,1,ax=ax)
    ax.set_ylim([-0.3, 0.3])
    ax.set_title(r'$\beta$ '+stock+' = '+str(round(linear_regression.params[1],2)),pad=20)
    ax.set_xlabel('market returns',color='grey')
    ax.set_ylabel('stock returns',color='grey')
    ax.legend(labels=('historical returns','fitted returns'),loc='upper left')
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1,decimals=0))
    ax.xaxis.set_major_formatter(mtick.PercentFormatter(1,decimals=0))
    ax.spines['top'].set_color('lightgrey')
    ax.spines['right'].set_color('lightgrey')
    ax.spines['bottom'].set_color('lightgrey')
    ax.spines['left'].set_color('lightgrey')
    ax.tick_params(axis='x', colors='grey')
    ax.tick_params(axis='y', colors='grey')
    xleft, xright = ax.get_xlim()
    ybottom, ytop = ax.get_ylim()
    ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*1)
