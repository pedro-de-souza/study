import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,1000) # 1darray of length 1000
# plt.plot(x, np.sin(x))
# plt.plot(x, np.cos(x))
# plt.show()

plt.plot(x, np.sin(x), color='k')
plt.plot(x, np.cos(x), color='r', linestyle ='--')
plt.show()