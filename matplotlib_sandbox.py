import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 5, 11)
y = x**2

# # FUNCTIONAL
# plt.plot(x, y,'r-')
# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title('X v Y')

# plt.subplot(1,2,1)
# plt.plot(x, y, 'r')
# plt.subplot(1,2,2)
# plt.plot(y, x, 'b')

# # Object Oriented
# fig = plt.figure()
# axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# # axes = fig.add_axes([0,0,1,1])
# # axes.plot(x, y)
# axes.set_xlabel('X Label')
# axes.set_ylabel('Y Label')
# axes.set_title('Title')
# axes.plot(x, x**2, label='x^2')
# axes.plot(x, x**3, label='x^3')
# axes.plot(x, x**4, label='x^4')
# # axes.legend(loc=10)
# axes.legend(loc=(0.1, 0.1))

# # For creating plots embedded in other plots
# fig = plt.figure()
# axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
# axes1.plot(x, y)
# axes2.plot(y, x)
# fig.tight_layout()

# fig, axes = plt.subplots(nrows=3, ncols=4)
# # subplots returns a numpy array if there is more than 1; loops are required to plot each figure
# for row in axes:
#     for p in row:
#         # plot based on the figure's grid coordinates
#         coor = np.where(axes == p) # returns tuple of single value numpy arrays
#         coor_sum = coor[0][0] + coor[1][0]
#         if (coor_sum % 2 == 0):
#             p.plot(x, y)
#         else:
#             p.plot(y, x)

# fig = plt.figure(figsize=(3, 2), dpi=200) # figsize tuple is size in inches
# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8,2))
# axes[0].plot(x,y)
# axes[1].plot(y,x)
# fig.tight_layout()

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# ax.plot(x, y, color='#ff8c00', linewidth='15', alpha=0.5, linestyle='dotted') # 1 is default line width
# ax.plot(x, y, color='#ff8c00', lw='2', alpha=0.5, ls='-.', marker='o', markersize=20, markerfacecolor='purple', markeredgewidth=3, markeredgecolor='red') 
ax.plot(x, y, color='#ff8c00')
ax.set_xlim([0, 4])
ax.set_ylim([0, 7])




# dpi is also a savefig argument
plt.savefig('plots/mpl_sandbox.png')

