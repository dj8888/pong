from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()

chart=fig.add_subplot(1,1,1,projection="3d")

x,y,z=axes3d.get_test_data(0.05)
chart.plot_wireframe(x,y,z,rstride=10,cstride=10)

chart.set_xlabel("X")
chart.set_ylabel("Y")
chart.set_zlabel("Z")

plt.show()
