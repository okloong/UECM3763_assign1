import numpy as np
import matplotlib.pyplot as plt

# Replace '1234' in the bracket with your numeric ID
np.random.seed(805689)

n = 300
x = np.random.random(n)
y = np.random.random(n)
c = np.random.random(n)  # color of points
s = 100 * np.random.random(n)  # size of points

fig, ax = plt.subplots()
im = ax.scatter(x, y, c=c, s=s, cmap=plt.cm.jet)

# Add a colorbar
fig.colorbar(im, ax=ax)

# save the figure
plt.savefig('plot_rnd.png')
plt.show()