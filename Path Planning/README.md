
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


Image Courtesy: Wikipedia

![alt tag](http://s6.postimg.org/uhismkd75/Screen_Shot_2015_09_11_at_11_15_40.png)
![alt tag](http://s6.postimg.org/u61c9swr5/Screen_Shot_2015_09_11_at_11_17_35.png)

**Minmax Search for Connect four**

To determine how good a node in search tree is at a particular depth
- Our approach : Assign a score based on how close the player is to completing any particular feature and also taking into account how close the opponent is to completing any particular feature
For example, a feature could be : 3 in-a-row
- Based on the feature count, an evaluated value is assigned to the node and compared.

**￼Comparis**
![alt tag](http://s6.postimg.org/kpg4gx2a9/Screen_Shot_2015_09_11_at_13_40_23.png)
