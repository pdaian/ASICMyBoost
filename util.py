from scipy.stats.kde import gaussian_kde
import matplotlib.pyplot as plt
from numpy import linspace

def kde(data, color):
        kde = gaussian_kde( data )
        # these are the values over wich your kernel will be evaluated
        dist_space = linspace( min(data), max(data), 1000 )
        # plot the results
        plt.plot( dist_space, kde(dist_space) , color = color)

