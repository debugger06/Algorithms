import numpy as np
import pylab as pl

data = np.loadtxt("/Users/vessilli/Desktop/self-learn/data/electrn.txt")

pl.scatter(data[:,1],data[:,2],marker = 'o',c='b')
pl.title('Data')
pl.xlabel('X')
pl.ylabel('Y')
#pl.show()
X = data[:,1]
y = data[:,2]
m = y.size
it = np.ones(shape=(m,2))
it[:,1] = X

theta = np.zeros(shape =(2,1))

iteration = 1500
alpha = 0.01


def compute_cost(X,y,theta):
    m = y.size
    predictions = X.dot(theta).flatten()

    sqe = (predictions - y)**2
    J = (1.0/(2*m))*sqe.sum()
    return J
def gradient_descent(X,y,theta,alpha,num_iters):
    m = y.size
    J_history = np.zeroes(shape = (num_iters,1))
    
