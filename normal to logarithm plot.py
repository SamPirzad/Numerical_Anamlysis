import numpy as np
import matplotlib.pyplot as plt
import pylab

dollar = np.array([ 1420, 1500, 1800, 2700, 4040, 4440, 4880, 6460,
                  8650, 8130, 7920, 7990, 8320, 8740, 9040, 9220, 
                  9400, 9660, 10000, 11000, 19800, 21000, 32850,
                  31500, 33200, 35500, 38260, 105770, 159918,
                  250000, 350000, 450000, ])

li = []
for i in range (1370, 1402):
  li.append(i)

fig = plt.figure()
axes = fig.add_subplot(2, 1, 1)
line, = axes.plot(t, dollar)
axes.set_yscale('log')

pylab.show()

