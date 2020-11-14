import numpy as np
import matplotlib.pyplot as plt 
import scipy.stats

# parameters
sample_sizes    = [1,2,5,10,30,50]
draws           = 1000
alpha           = 0.05

def axis_format():
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('lightgrey')
    ax.spines['left'].set_color('lightgrey')
    ax.tick_params(axis='x', colors='lightgrey')
    ax.tick_params(axis='y', colors='lightgrey')

fig, axs = plt.subplots(2,3,figsize = (16, 9))
fig.tight_layout(pad=5)
fig.suptitle("Distributions of the sample averages")

test_statistics = []
for ax, j in zip(axs.flatten(), sample_sizes):  
    # simulations
    averages = [np.mean(np.random.randint(2, size=j)) for i in range(0,draws)]
    
    # hypothesis testing
    test_statistic,_ = scipy.stats.jarque_bera(averages)
    test_statistics.append(test_statistic)
    
    # plot
    plt.axes(ax)
    plt.hist(averages,bins=50)  
    plt.xticks(np.arange(0, 1, step=0.25))
    plt.title('sample size '+str(j))  
    ax.set_title('sample size '+str(j),color='grey')
    plt.xlabel('avg. value')
    ax.xaxis.label.set_color('lightgrey')
    axis_format()
    xleft, xright = ax.get_xlim()
    ybottom, ytop = ax.get_ylim()
    ax.set_aspect(abs((xright-xleft)/(ybottom-ytop))*1) # set the axis square

test_critical = scipy.stats.chi2.isf(alpha, 2)
# plot
fig, ax = plt.subplots(figsize = (16, 9))
plt.plot(sample_sizes,test_statistics)
plt.axhline(y=test_critical, color='r', linestyle='-',label=r'significance level $\alpha$ ='+str(alpha))
plt.legend()  
plt.title('Test statistics for the Jarque–Bera test')
plt.xlabel('sample size')                                         
plt.ylabel('test statistic')                          
axis_format()