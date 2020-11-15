import numpy as np
import matplotlib.pyplot as plt 
import scipy.stats

# parameters
sample_sizes    = [1,2,5,10,30,50]
draws           = 1000
alpha           = 0.05

fig, axs = plt.subplots(2,3,figsize = (16, 9))
fig.tight_layout(pad=5)
fig.suptitle("Distributions of the sample averages")

def axis_format():
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('lightgrey')
    ax.spines['left'].set_color('lightgrey')
    ax.tick_params(axis='x', colors='grey')
    ax.tick_params(axis='y', colors='grey')

test_statistics = []
for ax, j in zip(axs.flatten(), sample_sizes):  
    # simulations
    averages = [np.mean(np.random.randint(2, size=j)) for i in range(0,draws)]
    
    # hypothesis testing
    test_statistic,_ = scipy.stats.jarque_bera(averages)
    test_statistics.append(test_statistic)
    
    # plot the distributions
    plt.axes(ax)
    plt.hist(averages,bins=50)  
    plt.xticks(np.arange(0, 1, step=0.25))
    ax.set_title('sample size '+str(j),color='grey')
    ax.set_xlabel('avg. value',color='lightgrey')
    axis_format()
    xleft, xright = ax.get_xlim()
    ybottom, ytop = ax.get_ylim()
    ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*1) # set the axis square

test_critical = scipy.stats.chi2.isf(alpha, 2)
# plot the test statistics
fig, ax = plt.subplots(figsize = (16, 9))
plt.plot(sample_sizes,test_statistics)
plt.axhline(y=test_critical, color='r', linestyle='-',label=r'significance level $\alpha$ ='+str(alpha))
plt.legend()  
plt.title('Test statistics for the Jarque–Bera test')
plt.xlabel('sample size')                                         
plt.ylabel('test statistic')                          
axis_format()

# credit : thanks to u/YesLod (Reddit) for helping me on this code
