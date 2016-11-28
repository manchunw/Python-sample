# line model
import numpy as np

class Line(object):
    def __init__(self, w0, w1):
        self.w0 = w0
        self.w1 = w1
        
    def predict(self, x, noise=0):
        return (x*self.w1 + self.w0 + noise*np.random.normal())

    # Input: data, a 2D array with each (x, t) pair on a row
    # Return: w0 and w1, the intercept and slope of the fitted line
    def learn(self, data):
        # replace the default code below which simply does random computation 
        # with your math equations derived above
        # w0 = np.asscalar(np.random.random(1))*2-1
        # w1 = np.asscalar(np.random.random(1))*2-1

        # my calculation:
        # first calculate the sum of T and X, and count n
        tsum = 0
        xsum = 0
        n = 0
        for x, t in data:
            tsum += t
            xsum += x
            n += 1
        # calculate w1 and w0
        w1deno = 0
        w1domi = 0
        for x, t in data:
            w1deno += (t*x - (tsum*x/n))
            w1domi += (x*x - (xsum*x/n))
        w1 = w1deno / w1domi
        w0 = (tsum - w1*xsum) / n
        return w0, w1

# test
np.random.seed()

w0 = np.asscalar(np.random.random(1))*2-1
w1 = np.asscalar(np.random.random(1))*2-1

line = Line(w0, w1)

N = 20
noise = 0.05
X = np.random.random([N])
T = []
for x in X:
    T.append(np.sum(line.predict(x, noise)))
T = np.array(T)    

#data = np.vstack((X, T)).transpose()
data = np.array([X, T]).transpose()

w0_fit, w1_fit = line.learn(data)

line_fit = Line(w0_fit, w1_fit)

print('truth:   ' + str(w0) + ' ' + str(w1))
print('predict: ' + str(w0_fit) + ' ' + str(w1_fit))