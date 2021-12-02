import numpy as np
import matplotlib.pyplot as plt

mean = 6.0
std = 1.0
size = 100000

x = np.random.normal(mean , std , size)
plt.plot(x)