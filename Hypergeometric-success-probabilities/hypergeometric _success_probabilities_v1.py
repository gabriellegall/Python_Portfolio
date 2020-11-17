import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import itertools
import scipy.stats

max_nb_hidden_cards     = 11 # the population size (N)
max_nb_desired_cards    = 5  # the number of success states in the population (K)
max_nb_draws            = 3  # the number of draws (n)
max_nb_min_success      = 2  # the minimum number of success(es) (k), for Pr(X>k)

nb_hidden_cards         = list(range(max_nb_desired_cards,max_nb_hidden_cards+1))
nb_desired_cards        = list(range(1,max_nb_desired_cards+1))
nb_draws                = list(range(1,max_nb_draws+1))
nb_min_success          = list(range(0,max_nb_min_success))

results = pd.DataFrame(itertools.product(nb_min_success, nb_draws, nb_desired_cards, nb_hidden_cards), columns=('nb_min_success','nb_draws', 'nb_desired_cards', 'nb_hidden_cards'))
results['proba_success'] = [scipy.stats.hypergeom.sf(k, N, K, n) for k, N, K, n in results[['nb_min_success','nb_hidden_cards','nb_desired_cards','nb_draws']].values]

for k in nb_min_success:
    fig, axs = plt.subplots(1,3,figsize = (16, 9))
    fig.tight_layout(pad=5)
    fig.suptitle('Probability of at least '+str(k+1)+' success(s) per number of draws')
    
    for n, ax in zip(nb_draws, axs):
        sns.heatmap(results[(results['nb_draws']==n) & (results['nb_min_success']==k)].pivot('nb_hidden_cards','nb_desired_cards','proba_success'), annot=True, vmin=0, vmax=1, ax = ax, cbar=False)
        ax.set_title('Probability of at least '+str(k+1)+' sucess(es) with '+str(n)+' draw(s)',color='grey',pad=20)
        ax.set_xlabel('Number of desired hidden cards',color='grey')
        ax.set_ylabel('Number of hidden cards',color='grey')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_color('lightgrey')
        ax.spines['left'].set_color('lightgrey')
        xleft, xright = ax.get_xlim()
        ybottom, ytop = ax.get_ylim()
        ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*1)

# credit : thanks to u/familytreebeard (Reddit) for helping me on this code
