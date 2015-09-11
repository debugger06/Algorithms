# TASK 3.1 -           #
# SPECTRAL CLUSTERING  #
########################
# Arash Nasirtafreshi  #
# Mana Azamat          #
# Mohammad Saifullah   # 
# Mudra Shah           #
# Tanya Agarwal        #
# Urmimala Majumdar    #
# Hasan Mahmud         #
########################

import numpy as np
import scipy
import numpy.linalg as lg
import networkx as nx
import matplotlib.pylab as plt
from pylab import plot,show
from scipy.cluster.vq import kmeans, kmeans2, vq, whiten
from math import sqrt
import Pycluster
import sklearn.cluster as skc


#Dictionary to calculate and store all positions
pos = {}										

#Distance between each node on x as well as y
dist = 1


def kMeans(X, K, maxIters = 10, centroids=None):
    """Credits: https://gist.github.com/bistaumanga/6023692 """
    if centroids is None:
        centroids = X[np.random.choice(np.arange(len(X)), K), :]
    for i in range(maxIters):
        # Cluster Assignment step
        C = np.array([np.argmin([np.dot(x_i-y_k, x_i-y_k) for y_k in centroids]) for x_i in X])
        # Move centroids step
        centroids = [X[C == k].mean(axis = 0) for k in range(K)]
    return np.array(centroids), C

#Getting positions in the graph
def get_positions(a_map_mirrored,rs,cs):
	element_keys = np.matrix(a_map_mirrored,dtype=int)
	newnode = 0
	for row in range(rs):
		for col in range(cs):
			if a_map_mirrored[row,col] == 0:
				pos[newnode] = (col, row)
				element_keys[row,col] = newnode
			else:
				element_keys[row,col] = -1
			newnode += 1

#Assigning edges and nodes
def initialize_graph(G,rs,cs):
	for n, p in pos.iteritems():
		G.node[n]['pos'] = p

		n_above = n - cs
		n_left = n - 1

		if n_above in pos.keys():
			G.add_edge(n,n_above)

		if n_left in pos.keys() and (G.node[n_left]['pos'][0] + dist == p[0]):
				G.add_edge(n,n_left)

#Calculating Normalized Laplacian 
def normalized_Laplacian(G):
	nodes = nx.nodes(G)
	total_nodes = nx.number_of_nodes(G)
	I = np.identity(total_nodes)
	D = np.identity(total_nodes)
	A = nx.adj_matrix(G)

	idx = 0
	for a_node in nx.nodes_iter(G):
		D[idx][idx] = G.degree(a_node)
		idx = idx + 1

	inv_sqrt_D = lg.inv(np.sqrt(D))
	M = (inv_sqrt_D * A * inv_sqrt_D)
	L = I - M
	return L

def spectral_clustering(a_map_mirrored, num_cluster):
	#Setting number of clusters
	k = num_cluster

	#Getting row and column size of array
	rs, cs = a_map_mirrored.shape

	#Getting the positions in the graph
	get_positions(a_map_mirrored,rs,cs)

	#Creating graph and setting the positions
	G = nx.Graph()
	G.add_nodes_from(pos.keys())

	#Assigning edges and nodes in the graph
	initialize_graph(G,rs,cs)

	#Calculating normalized Laplacian of graph
	L = normalized_Laplacian(G)

	#Computing the eigenvectors of L
	evals, evecs = lg.eig(L)

	#Sort the eigenvectors 
	sorted_evals_id = evals.argsort()
	evals = evals[sorted_evals_id]
	evecs = evecs[:,sorted_evals_id]

	#Get the first k eigenvectors
	U = evecs[:,:k]	

	#Applying k-means to U
	#_, labels = kmeans2(U, k, 1000, 'matrix')
	labels, _, _ = Pycluster.kcluster(U, k, dist='x', npass=1000, method='a')
	
	#Initializing color
	color = np.empty(len(labels), dtype=str)

	#Setting the value of color for different clusters
	for c in range(len(labels)):
		if labels[c] == 0:
			color[c] = 'r'
		elif labels[c] == 1:
			color[c] = 'g'
		elif labels[c] == 2:
			color[c] = 'b'
		elif labels[c] == 3:
			color[c] = 'y'
		elif labels[c] == 4:
			color[c] = 'c'
		elif labels[c] == 5:
			color[c] = 'm'
		elif labels[c] == 6:
			color[c] = 'k'
		elif labels[c] == 7:
			color[c] = 'w'

	#Drawing the graph
	nx.draw_networkx_nodes(G, pos, node_color=color, node_size = 100, with_labels=True)
	nx.draw_networkx_edges(G, pos, G.edges(),width=2.0,edge_color='k',style='solid')
	plt.axis('image')
	plt.show()	


if __name__ == '__main__':
	print "-----------------------------"
	print "Task 3.1: Spectral Clustering"
	print "-----------------------------"
	flag = True
	while flag: 
		#Converting the text data into array
		a_map_mirrored = np.flipud(np.loadtxt('simpleDungeonMap.txt'))

		#Getting the number of clusters from the user
		num_cluster = int (raw_input('Enter number of clusters: '))
		spectral_clustering(a_map_mirrored, num_cluster)
		
		continueVar = raw_input('Do you want to try again? (y/n): ')
		if continueVar != 'y':
			flag = False
		
	
