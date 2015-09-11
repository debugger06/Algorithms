
After getting inspiration from tic tac toe and implemented the game mechanics for connect four on a 6 × 7 board. Realize proper functionality for random moves and game termination tests; have a tournament between two players moving at random (but of course according to the game rules) and tried to collect statistics as to likely good moves;

![Image Courtesy: Wikipedia](http://s6.postimg.org/dtm8myc41/Connect_Four.gif)



- Have both players play many games (at least 1000) of tic tac toe in order to create a statistic of auspicious positions on the board;
- After each game, test if a player has won and if so, determine the fields this player occupied in order to count for each field how often it contributed to a win;
- After the tournament, plot a histogram of wins and draws;
- Properly normalized count data (such that they sum to one); 
- Afterwords implemented a function that realizes a game move using the probabilities you just determined;
- Used this function for the moves of player X and have player O move at random;
- Start another tournament and plot the new histogram of wins and draws

Analysis:
* ![alt tag](http://s6.postimg.org/wry0oedht/Screen_Shot_2015_09_11_at_09_52_08.png)
* ![alt tag](http://s6.postimg.org/b6sy0sgr5/Screen_Shot_2015_09_11_at_09_56_22.png)
* ![alt tag](http://s6.postimg.org/69fdfoes1/Screen_Shot_2015_09_11_at_10_07_10.png)
* ![alt tag](http://s6.postimg.org/6ngpf9yvl/Screen_Shot_2015_09_11_at_10_07_24.png)

