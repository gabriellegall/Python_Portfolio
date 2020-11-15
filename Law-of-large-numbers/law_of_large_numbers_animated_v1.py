import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# parameters
max_sample_size  = 500
theoretical_mean = 0.5

# initiate the plot
sample_sizes, sample_averages = [0], [0]
fig, ax = plt.subplots(1, 1, figsize = (16, 9))
line, = ax.plot(sample_sizes, sample_averages)
plt.axhline(y=theoretical_mean, color='r', linestyle='-')
plt.legend(('sample average','theoretical average'))
plt.ylim(0, 1)
ax.set_title('Sample average per sample size')
ax.set_xlabel('sample size')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color('lightgrey')
ax.spines['left'].set_color('lightgrey')
ax.tick_params(axis='x', colors='grey')
ax.tick_params(axis='y', colors='grey')

# dynamic plot
def animate(i):
    sample_sizes.append(i)
    sample_averages.append(np.random.randint(2, size=i).mean())
    line.set_data(sample_sizes,sample_averages)
    plt.xlim(min(sample_sizes), max(sample_sizes))

anim = animation.FuncAnimation(fig,
    animate,
    max_sample_size,
    interval = 1,
    repeat=False)
plt.show()

# save the .gif image
f = r"D://Gabriel/animation.gif" 
writergif = animation.PillowWriter(fps=30) 
anim.save(f, writer=writergif)
