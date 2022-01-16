import numpy as np
from matplotlib import pyplot as plt

number_list = np.arange(999999)
p = number_list * [np.cos(number_list), np.sin(number_list)]

SIZE = 20000

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(p[0], p[1], s=0.2, c='#fbf00f')
ax.axis('off')
fig.set_facecolor("k")
fig.tight_layout()

ax.set_xlim(-SIZE, SIZE)
ax.set_ylim(-SIZE, SIZE)
plt.show()
