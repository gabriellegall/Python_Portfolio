import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# parameters
max_sample_size  = 500
theoretical_mean = 0.5

# simulations
sample_sizes     = list(range(1,max_sample_size+1))
sample_averages  = [np.random.randint(2, size=i).mean() for i in sample_sizes]

# dynamic plot
x = sample_sizes
y = sample_averages
fig, ax = plt.subplots(1, 1, figsize = (16, 9))

def animate(i):
    ax.cla()
    ax.plot(x[:i], y[:i])
    ax.set_ylim([min(y), max(y)])
    plt.axhline(y=theoretical_mean, color='r', linestyle='-')   
    plt.legend(('sample average','theoretical average'))
    ax.set_title('Sample average per sample size')
    ax.set_xlabel('sample size')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color('lightgrey')
    ax.spines['left'].set_color('lightgrey')
    ax.tick_params(axis='x', colors='grey')
    ax.tick_params(axis='y', colors='grey')
        
anim = animation.FuncAnimation(fig, animate, frames = len(x) + 1, interval = 1, blit = False)
plt.show()

f = r"D://Gabriel/animation.gif" 
writergif = animation.PillowWriter(fps=30) 
anim.save(f, writer=writergif)
