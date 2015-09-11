
After getting inspiration from tic tac toe and implemented the game mechanics for connect four on a 6 × 7 board. Realize proper functionality for random moves and game termination tests; have a tournament between two players moving at random (but of course according to the game rules) and tried to collect statistics as to likely good moves;

![](http://s6.postimg.org/dtm8myc41/Connect_Four.gif) 
(Image Courtesy: Wikipedia)

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
