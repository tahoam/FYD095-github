import matplotlib.pyplot as plt

circle1 = plt.Circle((0.28, 0.6), 0.1, color='b', fill=False)
circle2 = plt.Circle((0.5, 0.6), 0.1, color='k', fill=False)
circle3 = plt.Circle((0.72, 0.6), 0.1, color='r', fill=False)
circle4 = plt.Circle((0.39, 0.5), 0.1, color='y', fill=False)
circle5 = plt.Circle((0.61, 0.5), 0.1, color='g', fill=False)


fig, ax = plt.subplots() # note we must use plt.subplots, not plt.subplot
# (or if you have an existing figure)
# fig = plt.gcf()
# ax = fig.gca()

ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)
ax.add_patch(circle4)
ax.add_patch(circle5)

fig.savefig('plotcircles.png')