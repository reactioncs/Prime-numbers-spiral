import numpy as np
from matplotlib import pyplot as plt

# readlines
text_file = open("PN_list.txt", "r")
PN_list = np.array(text_file.read().split(','), dtype="int32")

PN_list_part = PN_list[:]
p = PN_list_part * [np.cos(PN_list_part), np.sin(PN_list_part)]

# biggest: 999983
SIZE = 400000

fig, ax = plt.subplots(figsize=(10, 10))
ax.scatter(p[0], p[1], s=0.2, c='#fbf00f')
ax.axis('off')
fig.set_facecolor("k")
fig.tight_layout()

ax.set_xlim(-SIZE, SIZE)
ax.set_ylim(-SIZE, SIZE)
plt.show()
