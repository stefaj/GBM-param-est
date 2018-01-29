import pandas as pd
import numpy as np
from numpy.random import normal
import quandl

data = pd.read_csv('djia', index_col='Date', parse_dates=True)
data.sort_index(inplace=True)
r = np.log(data['Close']).diff().as_matrix()[1:]

sigma = np.std(r)
mu = np.mean(r) +0.5*sigma*sigma

T = 5000 
N = 20000 
epsilon = normal(size=[T, N])

start_close = data['Close'][-1]
start_close = 25000
paths = start_close*np.exp(np.cumsum(mu-0.5*sigma*sigma +sigma*epsilon, axis=0))

print('data from %s to %s' % (data.index[0].date(), data.index[-1].date()))
print('%d scenarios of %d periods, starting from close %f' % (N, T, start_close))

reach20K= 0
reach30K = 0

for n in range(N):
    for price in paths[:,n]:
        if price < 20000:
            reach20K += 1
            break
        if price > 30000:
            reach30K += 1
            break


total = reach20K + reach30K

print("20K: ", reach20K / total * 100.0, "%")
print("30K: ", reach30K / total * 100.0, "%")
