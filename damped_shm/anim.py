import numpy as np
import matplotlib.pyplot as plt 
from celluloid import Camera

fig = plt.figure(figsize=(10, 10))
camera = Camera(fig)

def update_points(t):
    omega = .5
    amplitude = 1.3
    theta = amplitude * np.cos(omega * t) * np.exp(-0.05 * t)
    x = np.cos(3*np.pi/2 + theta) 
    y = np.sin(3*np.pi/2 + theta) 
    return x, y

for i in range(100):
    x, y = update_points(i/10)
    plt.plot([0, x], [0, y], color='blue')
    camera.snap()

animation = camera.animate(interval=10)
plt.scatter(0, 0, color='red', s=10)
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.grid()
# plt.show()
animation.save('animation.gif')
