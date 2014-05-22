# -*- coding:utf8 -*-
# author: Prof. Maucher // applied changes: Stefan Seibert
# File for task 3.2

import datetime
from matplotlib import finance
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import cluster


# Choose a time period reasonable calm (not too long ago so that we get
# high-tech firms, and before the 2008 crash)
d1 = datetime.datetime(2003, 01, 01)
d2 = datetime.datetime(2008, 01, 01)

symbol_dict = {
        'TOT'  : 'Total',
        'XOM'  : 'Exxon',
        'CVX'  : 'Chevron',
        'COP'  : 'ConocoPhillips',
        'VLO'  : 'Valero Energy',
        'MSFT' : 'Microsoft',
        'IBM'  : 'IBM',
        'TWX'  : 'Time Warner',
        'CMCSA': 'Comcast',
        'CVC'  : 'Cablevision',
        'YHOO' : 'Yahoo',
        'DELL' : 'Dell',
        'HPQ'  : 'Hewlett-Packard',
        'AMZN' : 'Amazon',
        'TM'   : 'Toyota',
        'CAJ'  : 'Canon',
        'MTU'  : 'Mitsubishi',
        'SNE'  : 'Sony',
        'F'    : 'Ford',
        'HMC'  : 'Honda',
        'NAV'  : 'Navistar',
        'NOC'  : 'Northrop Grumman',
        'BA'   : 'Boeing',
        'KO'   : 'Coca Cola',
        'MMM'  : '3M',
        'MCD'  : 'Mc Donalds',
        'PEP'  : 'Pepsi',
        #'KFT'  : 'Kraft Foods',
        'K'    : 'Kellogg',
        'UN'   : 'Unilever',
        'MAR'  : 'Marriott',
        'PG'   : 'Procter Gamble',
        'CL'   : 'Colgate-Palmolive',
        #'NWS'  : 'News Corporation',
        'GE'   : 'General Electrics',
        'WFC'  : 'Wells Fargo',
        'JPM'  : 'JPMorgan Chase',
        'AIG'  : 'AIG',
        'AXP'  : 'American express',
        'BAC'  : 'Bank of America',
        'GS'   : 'Goldman Sachs',
        'AAPL' : 'Apple',
        'SAP'  : 'SAP',
        'CSCO' : 'Cisco',
        'TXN'  : 'Texas instruments',
        'XRX'  : 'Xerox',
        'LMT'  : 'Lookheed Martin',
        'WMT'  : 'Wal-Mart',
        'WAG'  : 'Walgreen',
        'HD'   : 'Home Depot',
        'GSK'  : 'GlaxoSmithKline',
        'PFE'  : 'Pfizer',
        'SNY'  : 'Sanofi-Aventis',
        'NVS'  : 'Novartis',
        'KMB'  : 'Kimberly-Clark',
        'R'    : 'Ryder',
        'GD'   : 'General Dynamics',
        'RTN'  : 'Raytheon',
        'CVS'  : 'CVS',
        'CAT'  : 'Caterpillar',
        'DD'   : 'DuPont de Nemours',
    }

symbols, names = np.array(symbol_dict.items()).T

print "----------------------------Symbols---------------------------------------"
print symbols

print "----------------------------Names---------------------------------------"
print names

quotes = [finance.quotes_historical_yahoo(symbol, d1, d2, asobject=True)
                for symbol in symbols]

print "----------------------------Quotes---------------------------------------"
print "Number of quotes:        ",len(quotes)

#print "--------------------------open and close-----------------------------------"
open    = np.array([q.open   for q in quotes]).astype(np.float)
close   = np.array([q.close  for q in quotes]).astype(np.float)

print "--------------------------clustering tasks---------------------------------"
#difference vectors calculation for task 3.2.1
differenceVectors = pd.DataFrame(columns=symbols)
for business in range(0, len(symbols)):
    businessSymbol = symbols[business]
    differenceVectors[businessSymbol] = pd.Series(open[business]-close[business], index=quotes[business].date)

# relation matrix for task 3.2.2
# transponsed for having correlation between business and not days
relationMatrix = np.corrcoef(differenceVectors.T)

#affinity propagation calculation for task 3.2.3
af = cluster.AffinityPropagation(affinity="precomputed").fit(relationMatrix)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_
n_clusters_ = len(cluster_centers_indices)
print "In " + str(len(labels)) + " Companies were " + str(n_clusters_) + " Clusters found."

#plotting the clusters for task 3.2.4
for i in range(0, n_clusters_):
    plt.figure("Companies related in Cluster %d" % i)
    for y in range(0, len(labels)):
        if i == labels[y]:
            plt.plot(quotes[y].date, close[y], "b", color=plt.cm.RdYlBu(y*5), ms=2, label=symbols[y])
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2)
    plt.ylabel("prices")
    plt.xlabel("time")
    plt.grid()

plt.show()