
import numpy as np
import networkx as nx
import matplotlib.pylab as plt
import heapq


def dijkstra_path(G,source, destination):
	# Distance initialized to 0, the node which will later work as previous node, fringe nodes
	dist_previous_fringe = [(0, source, [])]
	closed = set()
	while True:
		# heapq will return the tuple having minimum distance : will work instead of argmin
		(dist, u, path) = heapq.heappop(dist_previous_fringe)
		if u not in closed:
			# Add the node with minimum distance to the path only if not in closed
			path = path + [u]
			closed.add(u)
			if u == destination:
				return path
			for v_neighbor in G[u]:
				# Add new node with new distamce
				heapq.heappush(dist_previous_fringe, (dist + 1, v_neighbor, path))



def calculate_heuristic(G,destination):
	for r in range(rs):
		for c in range(cs):
			if a_map_mirrored[r,c] != 1:
				# Euclidean distance taken as heuristic
				dx = destination[0]-r
				dy = destination[1]-c
				G.node[(r,c)]['heuristic'] = round(np.sqrt(dx*dx + dy*dy),2)



def astar_path(G,source, destination):
	g = {}
	predecessor = {}
	fringe = [source]
	closed = set()
	g[source] = 0
	f = np.array([[g[source] + G.node[source]['heuristic'] , source[0], source[1]]])	# (f, x, y) when f is the f value of (x,y) coordinate

	while len(fringe) > 0:
		minIndex = f.argmin(axis=0)[0]	# argmin from 1st column - here 'f' values
		u = (int(f[minIndex][1]), int(f[minIndex][2]))	# node coordinates of the minIndex

		# Check if node is destination
		if u == destination:
			# Arrange path using predecessors
			the_path = [destination]
			prev = destination
			while prev != source:
				the_path.append(predecessor[prev])
				prev = predecessor[prev]

			return the_path
		
		closed.add(u)
		fringe.remove(u)
		f = np.delete(f,minIndex,0)
		
		for v_neighbor in G[u]:
			if v_neighbor in closed:
				pass
			else:
				# Only 1 step can be taken at a time so constant 1 is added
				newg = g[u] + 1
				if v_neighbor not in fringe or g[u] > newg: # second condition not possible in case of this graphs without weights
					g[v_neighbor] = newg
					f = np.vstack([f,[g[v_neighbor] + G.node[v_neighbor]['heuristic'], v_neighbor[0], v_neighbor[1]]])
					predecessor[v_neighbor] = u
					if v_neighbor not in fringe and v_neighbor not in closed:
						fringe.append(v_neighbor)

	# Should return 0 only in the case of disjoint graph
	return 0



def get_source():
	s_x = raw_input('Enter x-coordinate of source : ')
	s_y = raw_input('Enter y-coordinate of source : ')
	source = (int(s_x),int(s_y))
	return source


def get_destination():
	d_x = raw_input('Enter x-coordinate of destination : ')
	d_y = raw_input('Enter y-coordinate of destination : ')
	destination = (int(d_x),int(d_y))
	return destination



if __name__ == '__main__':

	# Load map from the file - rotate 270 degrees to display as needed
	# a_map_mirrored = np.rot90(np.rot90(np.rot90(np.loadtxt('simpleMap-1-20x20.txt',dtype=int))))
	# a_map_mirrored = np.rot90(np.rot90(np.rot90(np.loadtxt('simpleMap-3.txt',dtype=int))))

	filename = raw_input('Enter file name with txt extension : ')
	a_map_mirrored = np.rot90(np.rot90(np.rot90(np.loadtxt(filename,dtype=int))))
	rs, cs = a_map_mirrored.shape

	# Remove all the boundry walls near origin
	line = 0 	# Row or column index
	for c in range(cs):
		if all( a_map_mirrored[:,line] == 1 ):
			a_map_mirrored = np.delete(a_map_mirrored, line, axis=1)
			rs, cs = a_map_mirrored.shape
		else:
			break

	for r in range(rs):
		if all( a_map_mirrored[line,:] == 1 ):
			a_map_mirrored = np.delete(a_map_mirrored, line, axis=0)
			rs, cs = a_map_mirrored.shape
		else:
			break

	rs, cs = a_map_mirrored.shape
	G_dijkstra = nx.grid_2d_graph(rs, cs)
	G_a_star = nx.grid_2d_graph(rs, cs)

	# Decide positions in (x,y) form
	pos = dict(zip(G_dijkstra,G_dijkstra))

	# Remove all nodes representing wall from the graph
	for r in range(rs):
		for c in range(cs):
			if a_map_mirrored[r,c] == 1:
				G_dijkstra.remove_node((r,c))
				G_a_star.remove_node((r,c))


	# Get the coordinates as input OR specify below
	print 'Assume origin - (0,0) in the lower-left corner & row - column : ', rs,'-', cs

	# Given for simpleMap-1-20x20.txt
	# source = (0,10)
	# destination = (15,1)

	# Given for explained in the Lecture 09 Slide 23
	# source = (0,4)
	# destination = (14,19)


	# Input source and Destination
	while True:
		source = get_source()
		if a_map_mirrored[source] == 0:
			break
		else:
			print 'Sorry, it is a wall. Please enter other source'
			print
	while  True:
		destination = get_destination()
		if a_map_mirrored[destination] == 0:
			break
		else:
			print 'Sorry, it is a wall. Please enter other destination'
			print

	# Calculate A Star path and plot in a subfigure
	plt_a_star = plt.subplot(1,2,2)
	# Provide size and color to all the nodes in graph G_a_star
	nx.draw(G_a_star, pos, node_size = 40, node_color = 'w', with_labels = False)
	# Call Astar
	calculate_heuristic(G_a_star,destination)
	path_a = astar_path(G_a_star,source,destination)
	title_a_star = 'A Star - Route length ' + str(len(path_a))
	plt.title(title_a_star)
	if path_a == 0 : #in case of destination not reached or found
		print 'no path possible'
	else:
		# Color the route with Yellow
		for idx in range(len(path_a)):
			nx.draw_networkx_nodes(G_a_star, pos, nodelist=[path_a[idx]], node_color='m', node_size = 100)
			if idx != len(path_a)-1:
				nx.draw_networkx_edges(G_a_star, pos, edgelist=[(path_a[idx], path_a[idx+1])], edge_color='m', width = 3)

		#Overwrite the color as red-green and size of source-estination nodes
		nx.draw_networkx_nodes(G_a_star, pos, nodelist=[source, destination], node_color=['r','g'], node_size = 200)
		plt.axis('image')
	

	#Plot both figures
	plt.show()