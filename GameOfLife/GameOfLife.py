import numpy as np
import time
from scipy import signal
from matplotlib import pyplot as plt
plt.ion()

class Conway:
    def __init__(self, state, size, res):
        self.size = size
        self.res = res
        self.state = state
        
    def run(self):
        convo = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        b = signal.convolve2d(self.state, convo, mode = 'same', boundary = 'fill')
        c = np.zeros(self.size)
        c[np.where((b == 2) & (self.state == 1))] = 1
        c[np.where((b == 3) & (self.state == 1))] = 1

        c[np.where((b == 3) & (self.state == 0))] = 1

        self.state = c


if __name__ == "__main__":
    
    size = [100, 100]
    res = []
    intial_state = np.random.random(size[0] * size[1])
    intial_state = intial_state.reshape(size[0], size[1]).round()
    print(intial_state.shape)
    

    A = Conway(intial_state, size, res)
    print(A.state.shape)
    fig = plt.figure()
    img_plot = plt.imshow(A.state, interpolation="nearest", cmap = plt.cm.gray)
    
    
    while True:
        A.run()
        img_plot.set_data(A.state)
        plt.show()
        plt.pause(0.01)
        

        #time.sleep(0.01)
