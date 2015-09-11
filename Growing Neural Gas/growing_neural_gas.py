import imp
from matplotlib import lines
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import choice
import math
import operator
import time


pos = {}
def calc_positions(a_map_mirrored):
    newnode = 0
    for row in range(rs):
        for col in range(cs):
            if a_map_mirrored[row,col] == 0:
                pos[newnode] = (col, row)
            newnode += 1
            


def initialize_graph(G):
    #Assign positions to the nodes and other attributes (size,color)
    for n, p in pos.iteritems():
        G.node[n]['pos'] = p
        B.node[n]['err'] = 0
        n_above = n - cs
        n_left = n - 1

        if n_above in pos.keys():
            G.add_edge(n,n_above)

        if n_left in pos.keys() and (G.node[n_left]['pos'][0] + 1 == p[0]):
                G.add_edge(n,n_left)


def get_pos(file_loc):
    f = open('simpleDungeonMap.txt')
    lines1 = f.readlines()
    pos_temp = {}
    counter = 0
    for i in range(0, lines1.__len__()):
        # clear the line and free it from space and next line character
        l = lines1[i].replace(" ", "")
        l = l.replace("\n", "")
        # read each character which is data
        for j in range(0, len(l)):
            counter += 1
            if l[j] == str(0):
                pos_temp.update({counter: (j, (lines1.__len__()-i))})
        #pos_temp.update({i: l})
    f.close()
    return pos_temp



if __name__ == '__main__':
    print "Start ..."
    file_loc = ""
    delta_w = 0.05
    delta_n = 0.0005
    max_age = 25
    lam = 100
    N = 100
    alfa = 0.05
    beta = 0.0005
    # B = nx.Graph()
    # my_pos = get_pos(file_loc)
    # B.add_nodes_from(my_pos.keys())

    a_map_mirrored = np.flipud(np.loadtxt('simpleDungeonMap.txt'))
    # a_map_mirrored = np.rot90(np.rot90(np.rot90(np.loadtxt('simpleDungeonMap.txt',dtype=int))))
    rs, cs = a_map_mirrored.shape

    calc_positions(a_map_mirrored)

    #create Graph with the evaluated positions
    B = nx.Graph()
    B.add_nodes_from(pos.keys())

    initialize_graph(B)
    nx.draw(B, pos, node_color = 'w', node_size = 50, with_labels = False)


    # # Good to know
    # for n, p in my_pos.iteritems():
    #     if B.has_node(n):
    #         B.node[n]['pos'] = p
    #         B.node[n]['err'] = 0


    # draw edges
    for y in B.nodes():
        if B.has_node(y+1) :
            B.add_edge(y, y+1)

        if B.has_node(y+22) :
            B.add_edge(y, y+22)

    # initializing the algorithm

    # init V and err
    V = nx.Graph()
    # init 1st node
    V.add_node(1)
    V.node[1] = B.node[383]
    V.node[1]["err"] = 0
    #V.node[1]["w"] = B.node[383]["pos"]
    rv1 = choice(B.nodes())
    V.node[1]["w"] = B.node[choice(B.nodes())]["pos"]
    # init 2nd node
    V.add_node(2)
    V.node[2] = B.node[275]
    V.node[2]["err"] = 0

    do_check = True
    while do_check:
        rv2 = B.node[choice(B.nodes())]["pos"]
        if V.node[1]["w"] != rv2:
            V.node[2]["w"] = rv2
            do_check = False
    # counter for new nodes
    node_counter = 2

    # init E and age
    V.add_edge(1, 2)
    V.edge[1][2]["age"] = 0

    # fig = plt.figure(1)
    # fig.clf()
    # plt.ion()
    # plt.show()

    # Beginning of the loop ************************************************
    for t in range(1, 10000):
        # Sample data
        x = choice(B.nodes())

        # determine 2 closest vertices
        s = 0
        r = 0

        # 1st
        min_dist = 10000000000000000
        for n in V.nodes():
            dist = (V.node[n]["w"][0] - B.node[x]["pos"][0])**2 + (V.node[n]["w"][1] - B.node[x]["pos"][1])**2
            if dist < min_dist:
                min_dist = dist
                s = n

        # 2nd
        min_dist = 1000000000000000
        for n in V.nodes():
            dist = (V.node[n]["w"][0] - B.node[x]["pos"][0])**2 + (V.node[n]["w"][1] - B.node[x]["pos"][1])**2
            if dist < min_dist and (n != s):
                min_dist = dist
                r = n

        #

        # update err of winner s
        V.node[s]["err"] += ((V.node[s]["w"][0] - B.node[x]["pos"][0])**2 + (V.node[s]["w"][1] - B.node[x]["pos"][1])**2)

        # Move winner s toward x
        t1 = tuple(map(operator.sub, B.node[x]["pos"], V.node[s]["w"]))
        t1 = tuple(map(operator.mul, t1, (delta_w, delta_w)))
        V.node[s]["w"] = tuple(map(operator.add, t1, V.node[s]["w"]))

        # Move all neighbors of s toward x
        for n in nx.neighbors(V, s):
            t1 = tuple(map(operator.sub, B.node[x]["pos"], V.node[n]["w"]))
            t1 = tuple(map(operator.mul, t1, (delta_n, delta_n)))
            V.node[n]["w"] = tuple(map(operator.add, t1, V.node[n]["w"]))


        # increment age of edges incidental to s
        for e in nx.edges(V, s):
            V.edge[e[0]][e[1]]["age"] += 1

        # If s and r are connected:
        if V.has_edge(s, r):
            V.edge[s][r]["age"] = 0

        else:
            V.add_edge(s, r)
            edge = V.edge[s][r]
            V.edge[s][r]["age"] = 0

        # check ages
        for e in V.edges():
            if V.edge[e[0]][e[1]]["age"] > max_age:
                V.remove_edge(e[0], e[1])

        # check isolated nodes
        for n in V.nodes():
            if V.degree(n) == 0:
                V.remove_node(n)

        if ((t % lam) == 0) and (V.number_of_nodes() <= N):
            # Add new node
            node_counter += 1
            V.add_node(node_counter)
            # find vu
            max_err = 0
            vu = 0
            vv = 0
            for n in V.nodes():
                if (n != node_counter) and V.node[n]["err"] >= max_err:
                    max_err = V.node[n]["err"]
                    vu = n

            # find vv
            max_err = 0
            for n in V.neighbors(vu):
                if not V.neighbors(vu):
                    print "error"
                if V.node[n]["err"] >= max_err:
                    max_err = V.node[n]["err"]
                    vv = n
            print node_counter

            # init new node's w

            V.node[node_counter]["w"] = tuple(map(operator.add, V.node[vu]["w"], V.node[vv]["w"]))
            V.node[node_counter]["w"] = tuple(map(operator.div, V.node[node_counter]["w"], (2, 2)))

            # update errors
            V.node[vu]["err"] *= alfa
            V.node[vv]["err"] *= alfa
            V.node[node_counter]["err"] = V.node[vu]["err"]

            # add edge for new node
            V.add_edge(vu, node_counter)
            V.add_edge(node_counter, vv)
            V.remove_edge(vv, vu)

            # set age
            V.edge[vu][node_counter]["age"] = 0
            V.edge[vv][node_counter]["age"] = 0
        # update all err value of all nodes
        for n in V.nodes():
            V.node[n]["err"] *= beta
        v_pos2 = {}
        for n in V.nodes():
            v_pos2.update({n: V.node[n]["w"]})
        # fig.clf()
        # nx.draw(B, pos, node_color = 'w', node_size = 50, with_labels = False)
        # nx.draw(V, v_pos2, node_color='r', with_labels=False, node_size=150)
        # nx.draw_networkx_edges(V , v_pos2, edge_color='b', width=5)
        # plt.draw()
    # end of loop ******************************************************
    v_pos = {}
    for n in V.nodes():
        v_pos.update({n: V.node[n]["w"]})
    #print v_pos
    #nx.draw(B, pos)
    #nx.draw(B, my_pos)
    nx.draw(V, v_pos, node_color='r', with_labels=False, node_size=150)
    nx.draw_networkx_edges(V , v_pos, edge_color='b', width=5)
    plt.axis('image')
    plt.show()
