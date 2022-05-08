import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

def tanh(x):
    return np.tanh(x)

def logistic_regression(x,y,alpha,epochs):
    x=np.array(x)
    y=np.array(y)
    m=len(x)
    n=len(x[0])
    w=np.zeros(n)
    for i in range(epochs):
        for j in range(m):
            y_pred=sigmoid(np.dot(x[j],w))
            w=w+alpha*(y[j]-y_pred)*x[j]
    return w

def loss(y,y1):
    return -(y*np.log(y1)+(1-y)*np.log(1-y1)).sum()

def loss1(x,y,w):
    return -(y*np.log(sigmoid(np.dot(x,w)))+(1-y)*np.log(1-sigmoid(np.dot(x,w)))).sum()

#Ema=alpha*Close+(1-alpha)*Ema_prev
#alpha=2/span+1
def EMA(x):
    return x.ewm(span=20,adjust=False).mean()

