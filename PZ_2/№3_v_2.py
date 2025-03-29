from matplotlib import pyplot as plt
import numpy as np

sozivi = [1, 2, 3, 4]
partii = ['pisa','popa','biba','boba','xyi']
mesta = [
    [198, 99, 59, 58, 36],
    [220, 79, 69, 49, 33],
    [243, 90, 49, 40, 28],
    [180, 120, 69, 45, 36]
]
colors = ['r', 'g', 'b', 'orange', 'pink']

fig, ax = plt.subplots()
bottom = np.zeros(len(sozivi))
for i, partia in enumerate(partii):
    ax.bar(sozivi, [mesta[j][i] for j in range(len(partii)-1)], label=partia, color = colors[i], bottom=bottom, edgecolor='k')
    bottom += [mesta[j][i] for j in range(len(partii)-1)]
ax.set_ylabel('mesta')
ax.set_xlabel('№ soziva')
ax.legend()

plt.show()