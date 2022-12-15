import numpy as np
def longest_slide_down(pyramid):
    if len(pyramid) == 1:
        return pyramid[0][0]
    
    pyramid = np.array(pyramid)
    pyramid[-2] += np.maximum(pyramid[-1][:-1], pyramid[-1][1:])
    return longest_slide_down(pyramid[:-1])
