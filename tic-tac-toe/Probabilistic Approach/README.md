
Probabilistic Strategy for Tic-Tac-Toe: Implemented a probabilistic strategy. 

- Have both players play many games (at least 1000) of tic tac toe in order to create a statistic of auspicious positions on the board;
- After each game, test if a player has won and if so, determine the fields this player occupied in order to count for each field how often it contributed to a win;
- After the tournament, plot a histogram of wins and draws;
- Properly normalized count data (such that they sum to one); 
- Afterwords implemented a function that realizes a game move using the probabilities you just determined;
- Used this function for the moves of player X and have player O move at random;
- Start another tournament and plot the new histogram of wins and draws

Analysis:
