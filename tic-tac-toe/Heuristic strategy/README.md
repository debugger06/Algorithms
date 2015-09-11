Implemented strategy where the moving player evaluates all free po- sitions on the board and selects the most auspicious one;
use this function for the moves of player X and have player O move at random; start another tournament and plot the new histogram of wins and draws.


**Our Observation:**

We Played many times and observed:
- If 1st player plays -> any of the corner or diagonal centre
- 2nd player does not play -> any of the corner or diagonal centre Then, 2nd player will inevitable lose.
- The same thing also applies to 1st player. Main Idea: Use Diagonal corner and Corners

![alt tag](http://s6.postimg.org/cgvctkzwx/Screen_Shot_2015_09_11_at_10_38_48.png)

Initial Idea

1. Build game tree
2. Apply minmax algorithm on it
3. Try to avoid loss -> select either Winning or Draw game states

Problem: Original complete game tree has 9! nodes


