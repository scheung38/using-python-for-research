# Consider the following code:
import numpy as np
import matplotlib.pyplot as plt

# x = np.logspace(0, 1, 10)
# y = x ** 2
# plt.loglog(x, y, "bo-")
# plt.show()


# What does the above do?
# What does this return?

# x = np.random.normal(size=1000)
# plt.hist(x)
# plt.show()
#
# plt.plot([0,1,2,4,16])
# plt.show()

x = np.linspace(0,10,20)
y1 = x**2.0
y2 = x**1.5
plt.plot(x, y1, 'bo-', linewidth=2, markersize=12, label='First')
plt.plot(x, y2, 'gs-', linewidth=2, markersize=12, label='Second')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis([-0.5, 10.5, -5, 105])
plt.legend(loc='upper left')
plt.savefig('myplot.pdf')





