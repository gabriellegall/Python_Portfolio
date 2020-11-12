import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Data
max_sample_size  = 500
theoretical_mean = 0.5
sample_sizes     = list(range(1,max_sample_size+1))
sample_averages  = [np.random.randint(2, size=i).mean() for i in sample_sizes]

# Dynamic plot
x = sample_sizes
y = sample_averages
fig, ax = plt.subplots(1, 1, figsize = (16, 9))

def animate(i):
    ax.cla()
    ax.plot(x[:i], y[:i])
    ax.set_title('Illustration of the Law of Large Numbers')
    ax.set_xlabel('Sample size', fontsize=10)
    ax.set_ylim([min(y), max(y)])
    plt.axhline(y=theoretical_mean, color='r', linestyle='-')   
    plt.legend(('Sample average','Theoretical average'))
    
anim = animation.FuncAnimation(fig, animate, frames = len(x) + 1, interval = 1, blit = False)
plt.show()

f = r"D://Gabriel/animation.gif" 
writergif = animation.PillowWriter(fps=30) 
anim.save(f, writer=writergif)