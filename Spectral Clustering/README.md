
An appropriate way of clustering (waypoint) graphs is to consider spectral decompositions of the graph Laplacian L. simpleDungeonMap.txt generates a waypoint graph. Normalized Laplacian can be computed as:
      ![](http://s6.postimg.org/davulnmq5/Screen_Shot_2015_09_12_at_01_07_08.png) 

where I is the unit matrix of appropriate size and D^-1 is the inverse of
the matrix square root of D. Given L, This program computes it spectral decomposition and cluster the vertices of the waypoint graph into k clusters as discussed in the lecture. Following image Visualizes result; for k = 4

![](http://s6.postimg.org/m8gkj0f69/Screen_Shot_2015_09_12_at_01_13_29.png) 

**Result**
![](http://s6.postimg.org/5lz09xm8h/Screen_Shot_2015_09_12_at_01_16_45.png) 
![](http://s6.postimg.org/dfzlvbu1d/Screen_Shot_2015_09_12_at_01_18_09.png) 
![](http://s6.postimg.org/ihblafqvl/Screen_Shot_2015_09_12_at_01_19_03.png) 
![](http://s6.postimg.org/e9gt1opg1/Screen_Shot_2015_09_12_at_01_19_58.png) 
