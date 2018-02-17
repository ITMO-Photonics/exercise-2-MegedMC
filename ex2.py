#Plot a function $f(x)=\sqrt{|x|}\sin{x^2}$ on the interval [-5,5].
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5.,5.,1000)
y1=np.sqrt(abs(x))*np.sin(x*x)
fig, ax = plt.subplots()
ax.plot(x,y1,color='black')
plt.show()
