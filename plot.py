import numpy as np
from matplotlib import pyplot as plt

# readlines
text_file = open("PN_list.txt", "r")
PN_list = np.array(text_file.read().split(','), dtype="int32")

p = PN_list * [np.cos(PN_list), np.sin(PN_list)]
print(p)

fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(p[0], p[1], 'ok')
fig.tight_layout()
plt.show()
