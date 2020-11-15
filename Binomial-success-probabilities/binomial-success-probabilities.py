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
 
fig, axs = plt.subplots(1,3,figsize = (16, 9))
fig.tight_layout(pad=5)
fig.suptitle("Probability of a success per number of draws")

for i, ax in zip(nb_draws, axs):
    sns.heatmap(results[results['nb_draws']==i].pivot('nb_hidden_cards','nb_desired_cards','proba_success'), annot=True, vmin=0, vmax=1, ax = ax, cbar=False)
    ax.set_title('Probability of at least a sucess with '+str(i)+' draw(s)',color='grey',pad=20)
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
