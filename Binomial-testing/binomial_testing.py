import scipy.stats
import numpy as np
import matplotlib.pyplot as plt 

# parameters
max_nb_draws    = 235
nb_success      = 51
proba_success   = 1/6
alpha           = 0.05

# simulations
draws                   = list(range(0,max_nb_draws+1))
proba_distrib           = np.array([scipy.stats.binom.pmf(i, max_nb_draws, proba_success) for i in draws]) # P(X=k)
cum_proba_distrib       = np.cumsum(proba_distrib)-proba_distrib                # P(X<k)
inv_cum_proba_distrib   = 1-cum_proba_distrib                                   # P(X>=k)

# plots
def axis_format():
    ax.spines['top'].set_color('lightgrey')
    ax.spines['right'].set_color('lightgrey')
    ax.spines['bottom'].set_color('lightgrey')
    ax.spines['left'].set_color('lightgrey')
    ax.tick_params(axis='x', colors='grey')
    ax.tick_params(axis='y', colors='grey')

fig, ax = plt.subplots(figsize = (16, 9))
plt.plot(draws,proba_distrib)
ax.set_title('Probability distribution function',pad=20)
ax.set_xlabel('number of successes (k)',color='grey')
ax.set_ylabel('probability of k successes P(X=k)',color='grey')
axis_format()

fig, ax = plt.subplots(figsize = (16, 9))
plt.plot(draws,inv_cum_proba_distrib)
ax.set_title('Inverse cumulative probability distribution function',pad=20)
ax.set_xlabel('number of successes (k)',color='grey')
ax.set_ylabel('probability of at least k successes P(X>=k)',color='grey')
alphaIdx = np.abs(inv_cum_proba_distrib-alpha).argmin()                         # Retrive the critical value
plt.vlines(alphaIdx, 0, 1, linewidth=1, colors ='red',
           label=' critical value k='+str(alphaIdx)
           +r' ($\alpha$='+str(round(inv_cum_proba_distrib[alphaIdx],2))+')')
plt.legend()
axis_format()

# hypothesis testing
p_value_1 = scipy.stats.binom_test(nb_success,max_nb_draws,proba_success, alternative='greater') # right tailed test (probability of getting more extreme results)
p_value_2 = inv_cum_proba_distrib[nb_success] # p_value_1 = p_value_2