g=9.81
v=20
# cikls
for t in range(15):
    y=v*t-((g*(t**2))/2)
    print("Pie t=" + str(t) + " , y=" + str(y) +" .")
    
# plots
from numpy import linspace,array
t=linspace(0,15,15)
y=v*t-((g*(t**2))/2)
import matplotlib.pyplot as plt
plt.plot(t,y,color="#0000ff")
plt.legend()
plt.ylabel('y, m')
plt.xlabel('t, s')
plt.show()

