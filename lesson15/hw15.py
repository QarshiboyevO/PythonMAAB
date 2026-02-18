

import matplotlib.pyplot as plt
import numpy as np


#%%


import math

from openpyxl.styles.builtins import styles

from lesson12.hw12 import title

x=np.arange(-10,10,0.01)
y=x**2-4*x+4
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph of x^2-4*x+4')
plt.show()
#%%
x=np.arange(0,2*np.pi,0.01)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y,color='blue')
plt.plot(x,z,color='red')
plt.show()
#%%
x=np.arange(-5,5,0.1)
y=x**2
plt.subplot(2,2,1)
plt.plot(x,y,color='blue')
plt.title('plot of y=x**2')


y=np.sin(x)
plt.subplot(2,2,2)
plt.plot(x,y,color='red')
plt.title('plot of y=sin(x)')

y=np.e**x
plt.subplot(2,2,3)
plt.plot(x,y,color='green')
plt.title('plot of y=e**x')


x=np.arange(0,10,0.1)
y=np.log(x+1)
plt.subplot(2,2,4)
plt.plot(x,y,color='pink')
plt.title('plot of y=log(x)')

plt.show()
#%%
y=np.random.randn(100)
x=np.random.randn(100)
plt.scatter(x,y)
plt.show()
#%%
x=np.random.normal(0,1,1000)
plt.hist(x,alpha=0.5,color='red')
plt.title('Distribution of x')
plt.show()
#%%
x=np.arange(-5,5,0.01)
y=np.arange(-5,5,0.01)
X,Y=np.meshgrid(x,y)
r=np.sqrt(X**2+Y**2)
z=np.cos(r)
fig=plt.figure(figsize=(10,10))
ax=fig.add_subplot(1,1,1,projection='3d')

surf=ax.plot_surface(X,Y,z)



plt.show()
#%%
x=['Product A','Product B','Product C','Product D','Product E']
y=[200,150,250,175,225]
color=['red','green','blue','yellow','purple']
plt.bar(x,y,color=color)
plt.xlabel('Products',fontsize=10)
plt.ylabel('Products values',fontsize=10)
plt.show()
#%%
x=['T1','T2','T3','T4']
y1=np.array([100,150,120,130])
y2=np.array([150,120,140,90])
y3=np.array([150,100,120,150])
y4=y2+y1
plt.bar(x,y1,color='b')
plt.bar(x,y2,bottom=y1,color='r')
plt.bar(x,y3,bottom=y4,color='g')

plt.show()