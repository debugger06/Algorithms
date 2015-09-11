Implemented strategy where the moving player evaluates all free po- sitions on the board and selects the most auspicious one;
use this function for the moves of player X and have player O move at random; start another tournament and plot the new histogram of wins and draws.


**Our Observation:**

We Played many times and observed:
- If 1st player plays -> any of the corner or diagonal centre
- 2nd player does not play -> any of the corner or diagonal centre Then, 2nd player will inevitable lose.
- The same thing also applies to 1st player. Main Idea: Use Diagonal corner and Corners

![alt tag](http://s6.postimg.org/cgvctkzwx/Screen_Shot_2015_09_11_at_10_38_48.png)

**Initial Idea**

1. Build game tree
2. Apply minmax algorithm on it
3. Try to avoid loss -> select either Winning or Draw game states

Problem: Original complete game tree has 9! nodes

What can be the best strategic move?

Ans: From our observation - First 3 moves should be any of the 5 highlighted positions:

![alt tag](http://s6.postimg.org/gv3u5fahd/Screen_Shot_2015_09_11_at_10_56_25.png)

**Heuristic**

1. Initial 3 Moves:
Select from 5 highlighted positions & do not miss diagonal centre At this stage, we already reduced 3 levels from game tree !
2. Build game tree for the rest of the moves (6! nodes)
3. Apply minmax algorithm on it
4. Try to avoid loss -> select either Winning or Draw game states.
5. Make it faster by re-using evaluated branches rather generating them each
time.

![alt tag](http://s6.postimg.org/j282tcfrl/Screen_Shot_2015_09_11_at_10_59_01.png)


