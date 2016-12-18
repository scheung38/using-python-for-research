# Consider the following code:
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,201)

# x = np.random.normal(size=1000)
plt.hist(x)
# Create a smaller subplot in the topright of the figure
plt.subplot(3,3,3)
# same as plt.subplot(333)


plt.show()

# plt.hist(x, normed=True)
# plt.show()



