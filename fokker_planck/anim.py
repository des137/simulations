import numpy as np
from matplotlib import pyplot as plt
from celluloid import Camera

fig, axes = plt.subplots()
camera = Camera(fig)
x = np.linspace(0, 100, 1000)


def PDF_GBM(x, t, σ=0.2, x0=4, μ=0.1, speed=0.01):
    t = speed * t
    exp_factor = -(np.log(x/x0) - (μ - σ**2/2)*t)**2 / (2 * σ**2 * t)
    y = 1/(x * σ * np.sqrt(2 * np.pi * t)) * np.exp(exp_factor)
    return y    

def monte_carlo(x, t, σ=0.2, x0=4, μ=0.1, speed=0.01):
    t = speed * t
    μlog = (μ - σ**2/2)
    x = 4 * np.ones(1000)
    x *= np.exp(μlog * t + σ * np.random.randn(1000) * np.sqrt(t))
    return x

for t in range(100):
    speed = 1/2
    plt.plot(x, PDF_GBM(x, t, speed), color='orange')
    plt.hist(monte_carlo(x, t, speed), density=True, color='blue', 
        alpha=0.7, bins=30)
    plt.ylim(0, 1)
    plt.xlim(0, 20)
    plt.title('Equivalence Between Fokker-Planck and Monte Carlo') 
    camera.snap()

animation = camera.animate()
animation.save('animation.gif')
# plt.show()
