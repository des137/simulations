import numpy as np
import matplotlib.pyplot as plt 
from celluloid import Camera

# plt.figure(figsize=(10, 10))
fig = plt.figure(figsize=(10, 10))
camera = Camera(fig)

running_list_x = [0]
running_list_y = [0]

def update_points(t):
    x = np.cos(t)
    y = np.sin(t)
    return x, y

for i in range(int(10 * 2 * np.pi)):
    x, y = update_points(i/10)
    plt.scatter(x, y, color='blue')
    camera.snap()

animation = camera.animate(interval=10)
plt.scatter(0, 0, color='red', s=1000)
plt.grid()
# plt.show()
animation.save('animation.gif')
