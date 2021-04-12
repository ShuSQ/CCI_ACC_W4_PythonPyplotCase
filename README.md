# CCI_ACC_W4_PythonPyplotCase

I used Python3 and Pyplot to do a small exercise. I chose to draw a butterfly curve and chose the colour values to make it look more beautiful! I also hope to make the butterfly really fly through the form of frame animation (although Python will do this very badly).

![](https://miro.medium.com/max/700/1*8NvxF0cQyJEvhAIzmPrq2w.png)

``` python
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#fig, ax = plt.subplots()

fig = plt.figure(figsize=(8, 4.5))

# function - zoom in and zoom out
def call_back(event):
    axtemp = event.inaxes
    x_min, x_max = axtemp.get_xlim()
    y_min, y_max = axtemp.get_ylim()
    z_min, z_max = axtemp.get_zlim()

    scope = (x_max - x_min) / 10
    if event.button == "up":
        axtemp.set(xlim = (x_min + scope, x_max - scope))
        axtemp.set(ylim = (y_min + scope, y_max - scope))
        axtemp.set(zlim = (z_min + scope, z_max - scope))

        print('up')
    elif event.button == 'down':
        axtemp.set(xlim = (x_min - scope, x_max - scope))
        axtemp.set(ylim = (y_min - scope, y_max - scope))
        axtemp.set(zlim = (z_min - scope, z_max - scope))

        print('down')
    fig.canvas.draw_idle()
fig.canvas.mpl_connect('scroll_event', call_back)
fig.canvas.mpl_connect('button_press_event', call_back)

ax = fig.add_subplot(111, projection = '3d')
ax.xaxis.set_major_formatter(plt.NullFormatter())
ax.yaxis.set_major_formatter(plt.NullFormatter())
ax.zaxis.set_major_formatter(plt.NullFormatter())

t = np.arange(0.0, 16 * np.pi, 0.01)
x = np.sin(t) * (np.e ** np.cos(t)-2 * np.cos(4 * t) -np.sin(t/12) ** 5)
y = np.cos(t) * (np.e ** np.cos(t)-2 * np.cos(4 * t) -np.sin(t/12) ** 5)
z = pow(x ** 2 + y ** 2, 1/2) + np.cos(t) * np.pi + t ** 1.01 * np.pi

#plt.figure(figsize=(8,6))
#plt.axis("off")

# def update(*args):
#     for i in range(100):
#         z = z + 1
#     return z

plt.scatter(x, y,z, c = t, cmap = 'magma', marker = '+', linestyle = ':')
#anim = animation.FuncAnimation(fig, update, interval=20)
# plt.colorbar()
plt.title("Butterfly Curve")
ax.text(4, 4, 0, "try scroll ❤( •̀_•́)و✧", color='#007aff')
plt.show()
```
