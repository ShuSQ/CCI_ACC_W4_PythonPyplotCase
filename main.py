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









# ------------- Below is a garbage dump -------------------

# import numpy as np
# import math
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
#
# fig, ax = plt.subplots()
#
# def function(x, y):
#     return np.sin(x) + np.cos(y)
#     # return pow(np.sin(x), np.sin(y)) + pow(np.cos(y), np.cos(x))
#
# x = np.linspace(0, 2 * np.pi, 120)
# y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
# # ims is a list of lists, each row is a list of artists to draw in the
# # current frame; here we are just animating one artist, the image, in
# # each frame
# ims = []
#
# for i in range(120):
#     x += np.pi / 300.
#     y += np.pi / 100.
#     im = ax.imshow(function(x, y), animated=True, cmap='gray')
#     if i == 0:
#         ax.imshow(function(x, y))  # show an initial one first
#     ims.append([im])
#
# ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
#                                 repeat_delay=1000)
# plt.axis('off')
# plt.show()




#
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.colors as colors
# import time
#
# """
# SymLogNorm: two humps, one negative and one positive, The positive
# with 5-times the amplitude. Linearly, you cannot see detail in the
# negative hump.  Here we logarithmically scale the positive and
# negative data separately.
#
# Note that colorbar labels do not come out looking very good.
# """
#
# time = time.time()
# N = 100
# X, Y = np.mgrid[-4:4:complex(0, N), -4:4:complex(0, N)]
# Z1 = np.exp(-X**2 - Y**2)
# Z2 = np.exp(-(X-2)**2 - (Y-2)**2)
# Z = (Z1 - Z2) * 2
#
# fig, ax = plt.subplots()
#
#
#
# pcm = ax.pcolormesh(X, Y, Z, cmap='PuOr_r')
#
# plt.axis('off')
# plt.show()


# import numpy as np
# print('numpy:' + np.version.full_version)
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.animation as animation
# import matplotlib
# print('matplotlib:' + matplotlib.__version__)
#
# N = 150
# fps = 10
# frn = 50
#
# x = np.linspace(-4,4,N+1)
# fps = 10
# frn = 50
#
# x  = np.linspace(-4, 4, N+1)
# x, y = np.meshgrid(x, x)
# zarray = np.zeros((N+1, N+1, frn))
#
# f = lambda x, y, slg: 1/np.sqrt(slg)*np.exp(-(x**2 + y**2) / slg**2)
#
# for i in range(frn):
#     zarray[:,:,i] = f(x,y,1.5 + np.sin(i*2*np.pi/frn))
#
# def update_plot(frame_number, zarray, plot):
#     plot[0].remove()
#     plot[0] = ax.plot_surface(x, y, zarray[:,:, frame_number], cmap="magma")
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# plot = [ax.plot_surface(x, y, zarray[:,:,0], color = '0.75', rstride = 1, cstride = 1)]
# ax.set_zlim(0,1.1)
#
# ani = animation.FuncAnimation(fig, update_plot, frn, fargs = (zarray, plot), interval = 1000/ fps)
#
# fn = 'plot_surface_animation_funcanimation'
# ani.save(fn+'.mp4',writer='ffmpeg',fps=fps)
# ani.save(fn+'.gif',writer='imagemagick',fps=fps)
#
# import subprocess
# cmd = 'magick conver %s.gif - fuzz 5%% -layers Optimize %s_r.gif'%(fn,fn)
# subprocess.check_output(cmd)
#
# plt.rcParams['animation.html'] = 'html5'
# ani




# --! animation function !--
# def function(x):
#     return pow(x ** 2 - x ** 6, -6)
#
# ims = []
# def update(i):
#     x = np.sin(t) * (np.e ** np.cos(t)-2 * np.cos(4 * t) -np.sin(t/12) ** 5) + i
#     y = np.cos(t) * (np.e ** np.cos(t)-2 * np.cos(4 * t) -np.sin(t/12) ** 5) + i
#     im = ax.imshow(function(x), animated = True, cmap= 'gray')
#     if i == 0:
#         ax.imshow(function(x))
#     ims.append([im])
#
# ani = animation.FuncAnimation(fig, update, range(len(t)), interval=30)
# plt.axis("off")
# plt.show()


