%matplotlib inline
import random
from scipy import stats as ss
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from math import sqrt, pi
import scipy.stats
def normal_pdf(x, mu, sigma):
    return 1 / (sigma * sqrt(2 * pi)) * np.exp(-(x - mu)**2 / (2. * sigma))
mpl.style.use(['seaborn-notebook', 'seaborn-darkgrid'])

N = 25

# Create an array of p parameters to use for our distributions
some_ps = np.random.random(N)
# Create our M (trial number) parameters for binomial between 1 and 15.
# We do not go past 15 because it is time consuming to compute the numbers
some_Ms = np.random.randint(1, 15, N)
# Create a place to store our data
data = []
for i in range(10000):
    point = 0
    for j in range(N):
         # We use the jth distribution parameters to sample
        point += ss.binom.rvs(some_Ms[j], some_ps[j])
    # We cast to float, since everything is done until now in integers
    data.append(float(point) / N)


sns.distplot(data)
plt.title('CLT with 25 Binomial Dist')
plt.show()
