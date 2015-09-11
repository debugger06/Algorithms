
The file simpleMap-1-20x20.txt contains a 20 × 20 matrix of zeros and ones. Think of this matrix as the representation of a 2D game map where fields marked 0 are locations a player can be in whereas fields marked 1 represent parts of walls.
Implemented program reads data like these and transform them into a grid graph (a.k.a. a lattice) where there is a vertex for every zero and an edge between any two vertically or horizontally adjacent zeros. Fields marked 1 should not occur in graph. As a picture says a thousand words, here is an illustration as to how your graph should look like:
![](http://s6.postimg.org/u8c155ln5/Screen_Shot_2015_09_11_at_16_23_41.png) 

We confirmed way of reading map matrices and creating graphs therefrom works in general. It is Assumed the (0, 0) coordinate of our game world coincides with the vertex in the lower left corner of the graph. In the following picture, the vertex colored in red is thus located at grid coordinates (0, 10) and the green one resides at (15, 1).
![alt tag](http://s6.postimg.org/cmieoyymp/Screen_Shot_2015_09_12_at_00_23_24.png)

**Generating graph**
- Considered 1 as a wall
- For lower left corner to be (0,0) origin for all maps
    - Removed the extra walls from the input matrix
- grid_2d_graph() from networkx

**Algorithms**
- Dijkstra’s algorithm:
    - Select neighbors with minimum distance and move ahead
    - Instead of making a distance matrix from source
    - Stop calculating when destination is found
- A* Algorithm
    - Heuristic is the euclidean distance
    - If heuristic is taken as number of steps (edges to be traversed) then it works almost the same as Dijkstra’s algorithm.

**Result**
![alt tag](http://s6.postimg.org/udu13fe1d/Screen_Shot_2015_09_12_at_00_32_13.png)
![alt tag](http://s6.postimg.org/bms3t9jgx/Screen_Shot_2015_09_12_at_00_34_17.png)
![alt tag](http://s6.postimg.org/hozqjr7wx/Screen_Shot_2015_09_12_at_00_35_27.png)
![alt tag](http://s6.postimg.org/i35nx3he9/Screen_Shot_2015_09_12_at_00_36_27.png)
![alt tag](http://s6.postimg.org/y2obgndg1/Screen_Shot_2015_09_12_at_00_37_52.png)
