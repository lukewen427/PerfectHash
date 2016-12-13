import matplotlib.pyplot as plt
import numpy as np
ip_types = ["/24", "/22", "/20", "/18", "/16"]
N = 5
x = np.arange(N)
offset_table = [0, 98, 100, 95, 95]
# plt.xticks(x, ip_types)
# line, = plt.plot(x, offset_table)
fig, ax = plt.subplots()
rects = ax.bar(x, offset_table, 0.35, color="b")
ax.set_ylabel('Size of offset table')
ax.set_title('Ip address types')
ax.set_xticks(x + 0.35)
ax.set_xticklabels(ip_types)

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')
autolabel(rects)
plt.ylim([0, 120])
plt.show()
