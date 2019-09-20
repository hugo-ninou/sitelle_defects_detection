import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def perturbation(ampl = 2):
    return ampl*np.random.randn()

def amplitude_satellite(beta=1):
    return np.random.exponential(beta)
    
def gaussienne(x, y, sigma=3, mu=[0,0]):
    r = np.sqrt((x-mu[0])**2+(y-mu[1])**2)
    return (1/(sigma * np.sqrt(2*np.pi)))*np.exp(-(r)**2/(2*sigma**2))


def satellite(surech = 3):
    
    size = 400 * surech + 40
    sample = np.zeros([size,size])

    center = [np.random.randint(20,size - 20), np.random.randint(20,size - 20)]
    theta = np.random.random() * np.pi
    slope = np.tan(theta)
    b = (center[1] - slope * center[0])
    
    def f(x, a = slope, b = b):
        return (a * x + b)
    
    for x in range(size):
        y = int(f(x) + perturbation())
        if y in range(size):
            sample[x][y] += 1
    
    for y in range(size):
        x = int( (y-b)/slope + perturbation())
        if x in range(size):
            sample[x][y] += 1
    
    psf = np.zeros([41,41])
    for x in range(41):
        for y in range(41):
            psf[x][y] = gaussienne(x,y,9,[20,20])
    
    psf = amplitude_satellite() * psf
    
    conv = signal.convolve2d(sample, psf, 'valid')
    
    m, n = conv.shape
    
    res = conv[:m//surech*surech, :n//surech*surech].reshape(m//surech, surech, n//surech, surech).mean(axis=(1,3))
    return res


res = satellite()

def satellite_mask(sat):
    max = np.max(sat)
    threshold = 0.1 * max
    mask = (sat > threshold)
    return mask

mask = satellite_mask(res)

plt.close()
plt.imshow(mask)
plt.show()