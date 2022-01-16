import numpy as np
from matplotlib import pyplot as plt

# readlines
text_file = open("PN_list.txt", "r")
PN_list = np.array(text_file.read().split(','), dtype="int32")

p = PN_list * [np.cos(PN_list), np.sin(PN_list)]

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(p[0], p[1], s=0.1, c="white")
ax.set_facecolor('black')
fig.tight_layout()
plt.show()
