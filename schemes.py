import numpy as np
import plotly.graph_objects as go
import statistics
from scipy.stats import shapiro
from scipy.stats import norm
def Euler_Maruyama(a,b,x_0, T, N):
    values = np.zeros(N)
    values[0]=x_0
    delta=T/N
    W = np.sqrt(delta)*np.random.randn(N)
    for i in range(1,N):    
        values[i] = values[i-1] + a*delta + b*W[i]
    return values    


def distributions(u,D,M,T,N):
    #place for defining delta(x) distribution
    starting_vals = np.zeros(M)
    
    values = np.zeros((M,N))
    means = np.zeros(N)
    sigma = np.zeros(N)
    p_val = np.zeros(N)
    for i in range(M):
        values[i]=Euler_Maruyama(-u,np.sqrt(2*D),starting_vals[i],T,N)
    for i in range(N):
        means[i] = statistics.mean(values[:,i])
        sigma[i] = statistics.stdev(values[:,i])
        test = shapiro(values[:,i])
        p_val[i] = test.pvalue
    return values, means, sigma, p_val

