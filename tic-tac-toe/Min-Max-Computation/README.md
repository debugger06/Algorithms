Implement the minmax algorithm and used our implementation to compute mmv(n0) for the following tree:
![alt tag](http://s6.postimg.org/exg09rsgh/Screen_Shot_2015_09_11_at_13_15_02.png)

After applying MaxNodeUtil method on n0, the tree looks like:
![alt tag](http://s6.postimg.org/a02fonqhd/Screen_Shot_2015_09_11_at_13_25_23.png)

If there are more than one node having same utility, it does not create exact result. For example for the following case for maxNodeUtil(n0):

![alt tag](http://s6.postimg.org/nv0q74kwh/Screen_Shot_2015_09_11_at_13_27_10.png)

- The implementation may create inappropriate result for selecting next move from n0 as there is a tie on its successors.
- This has been handled by selecting the next move from tie moves which have higher utility on their successors. So, in this case n1 has been selected as it has higher utility on its successors. In case of minNodeUtil, the node with minimum utility on their successor will be selected.


