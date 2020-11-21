import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest

url = 'https://raw.githubusercontent.com/gabriellegall/Python_Portfolio/main/data/random_ab_testing.csv'
data = pd.read_csv(url, error_bad_lines=False)

AB_summary           = data.pivot_table(values='converted', index='group', aggfunc=np.sum)
AB_summary['size']   = data.pivot_table(values='converted', index='group', aggfunc=lambda x: len(x))
AB_summary['proba']  = data.pivot_table(values='converted', index='group')

#%% using scipy.stats.proportions_ztest
z_score, p_value = proportions_ztest(AB_summary['converted'].values,AB_summary['size'].values)

#%% theory behind the function
size_A          = AB_summary['size'].loc['A']
size_B          = AB_summary['size'].loc['B']
proba_A         = AB_summary['proba'].loc['A']
proba_B         = AB_summary['proba'].loc['B']
proba_C         = proba_A - proba_B
proba_C_pooled  = (proba_A*size_A+proba_B*size_B)/(size_A+size_B) # weighted average of proba_A and proba_B
sem_A           = np.sqrt(proba_A*(1-proba_A)/size_A)
sem_B           = np.sqrt(proba_B*(1-proba_B)/size_B)
sem_C           = np.sqrt(proba_C_pooled*(1-proba_C_pooled)*(1/size_A+1/size_B))

z_score         = proba_C/sem_C # null hypothesis : difference = 0
p_value         = stats.norm.sf(abs(z_score))*2 # two-sided test

fig, axs = plt.subplots(1,2,figsize = (16, 9))
def axis_format():
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('lightgrey')
    ax.spines['left'].set_color('lightgrey')
    ax.tick_params(axis='x', colors='grey')
    ax.tick_params(axis='y', colors='grey')
    xleft, xright = ax.get_xlim()
    ybottom, ytop = ax.get_ylim()
    ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*1) # set the axis square
    plt.legend(loc='upper right')

def get_axis(p,sem):
    x = np.linspace(p-3*sem,p+3*sem, 100)
    return x

x_A      = get_axis(proba_A,sem_A)
x_B      = get_axis(proba_B,sem_B)
x_C      = get_axis(proba_C,sem_C)
x_C_null = get_axis(0,sem_C)

ax = axs[0]
plt.axes(ax)
plt.plot(x_A, stats.norm.pdf(x_A, proba_A, sem_A),label='sample A', color='blue')
plt.plot(x_B, stats.norm.pdf(x_B, proba_B, sem_B),label='sample B', color='green')
ax.set_title('Estimated distribution of the average success probabilities',pad=20)
axis_format()

ax = axs[1]
plt.axes(ax)
plt.plot(x_C, stats.norm.pdf(x_C, proba_C, sem_C),label='sample C | alternative', color='black')
plt.plot(x_C_null, stats.norm.pdf(x_C_null, 0, sem_C),label='sample C | null', color='lightgrey')
ax.set_title('z = '+str(round(z_score,2))+' | pvalue = '+str(round(p_value,2))+'\n\nHypothesis test for the difference in average success probabilities',pad=20)
axis_format()
