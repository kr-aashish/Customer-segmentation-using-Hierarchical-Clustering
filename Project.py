# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 09:47:18 2020

@author: AK
"""

#importing necessary libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#importing datasets
Dataset = pd.read_csv('Customers.csv')
X = Dataset.iloc[:, [3,4]].values

#Using dendogram to find optimal number of clusters
import scipy.cluster.hierarchy as sch
dendogram = sch.dendrogram(sch.linkage(X, method='ward'))   

plt.xlabel('Customers')
plt.ylabel('Euclidian distance')            
plt.title('Dendogram')
plt.show()
#numbe of clusters should be the number of longest vertical lines

#fitting the model to our dataset
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')
#ward - variance

y_hc = hc.fit_predict(X)

# Visualising the clusters and interpretation
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 100, c = 'cyan', label = '1st Cluster')
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'green', label = '2nd Cluster')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'red', label = '3rd Cluster')
#plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s = 100, c = 'blue', label = '4th Cluster')

plt.title('Clusters of customers')
plt.xlabel('Annual Salary (k$)')
plt.ylabel('Spendings (1 to 100)')
plt.legend()
plt.show()
