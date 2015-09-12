import csv
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math as m
import random
import Pycluster

fig = plt.figure(1)
fig.clf()
ax = Axes3D(fig)

pointsX = []
pointsY = []
pointsZ = []

"""
Load prototypical game states from file
"""
s = np.loadtxt('prototypical_gamestates.out', dtype=float, delimiter=',')


with open('q3dm1-path1.csv', 'rb') as f:
	reader = csv.reader(f)
	k = 0
	for row in reader:
		data = map(float,row)
		pointsX.append(data[0])
		pointsY.append(data[1])
		pointsZ.append(data[2])


point = np.ndarray(shape=(len(pointsX),3), dtype=float, order='F')
activity = np.zeros(shape=(len(pointsX),3), dtype=float, order='F')

for i in range(0,len(pointsX)):
	point[i,0] = pointsX[i]
	point[i,1] = pointsY[i]
	point[i,2] = pointsZ[i]


"""
Activity vector
"""
for i in range(0, len(point)-1):
	activity[i] = point[i+1] - point[i]
activity[len(activity)-1] = activity[0]- activity[len(activity)-1]
# print activity
np.savetxt('test.out', activity, delimiter=',')



"""
Cluster activity into k cluster
"""
number_of_cluster = 5
label,errors,nfound= Pycluster.kcluster(activity,number_of_cluster)
centroid, a =Pycluster.clustercentroids(activity,clusterid=label)

np.savetxt('label.out', label, delimiter=',')



# """
# plot clustered data
# """
# zl = m.ceil(min(activity[0])) - 10
# zh = m.ceil(max(activity[0])) + 10
# # for i in range(0,len(label)):
# 	if(label[i]==0):
# 		ax.scatter(activity[i,0], activity[i,1], activity[i,2], s=200, marker='.', c='r')
# 	if(label[i]==1):
# 		ax.scatter(activity[i,0], activity[i,1], activity[i,2], s=200, marker='.', c='g')
# 	if(label[i]==2):
# 		ax.scatter(activity[i,0], activity[i,1], activity[i,2], s=200, marker='.', c='b')
# 	if(label[i]==3):
# 		ax.scatter(activity[i,0], activity[i,1], activity[i,2], s=200, marker='.', c='y')
# 	if(label[i]==4):
# 		ax.scatter(activity[i,0], activity[i,1], activity[i,2], s=200, marker='.', c='w')

# ax.set_zlim3d([zl, zh])




"""
joint probability calculations
"""
pair = np.zeros(shape=(len(s),len(label)), dtype=float, order='F')
p_state = np.zeros(len(point), dtype=int)
for t in range(len(point)):
	diff = np.zeros(len(s),dtype=float)
	for i in range(len(s)):
		diff[i] = np.linalg.norm(s[i]-point[t])
	si = np.argmin(diff)			#This will return the si cluster index of the data point x at t=i
	p_state[t] = si
	rj = label[t]		#This will return the si cluster of the position x at t=i
	pair[si,rj] = round(pair[si,rj],2) + 1
# print pair
pair = pair[:,:]/(sum(sum(pair)))

# print pair




"""
recreating the trajectory data
"""
t = random.randint(0,len(point)-2)
new_num_nodes = 130
a = np.ndarray(shape=(new_num_nodes,1), dtype=int, order='F')
for tt in range(new_num_nodes):
	p_si = sum(pair[p_state[t],:])
	p_si_rj = pair[p_state[t],:]
	a[tt] = np.argmax(p_si_rj/p_si)
	# print p_si, p_si_rj, a[tt]
	t += 1
	# raw_input()

# print a

newpoint = np.ndarray(shape=(new_num_nodes,3), dtype=float, order='F')

for idx in range(len(newpoint)-1):
	newpoint[idx+1] = point[idx] + activity[a[idx]]
	ax.scatter(newpoint[idx+1,0], newpoint[idx+1,1], newpoint[idx+1,2], s=200, marker='.',c='r')

zl = m.ceil(min(newpoint[:,2])) - 10
zh = m.ceil(max(newpoint[:,2])) + 10
ax.set_zlim3d([zl, zh])

plt.draw()
plt.show()