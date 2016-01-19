import sys, getopt
from itertools import groupby, repeat
from sys import argv
from extract import Dummie



# import numpy as np
# import matplotlib.pyplot as plt

def search(d):
    """Key function used to group our dataset"""

    return d[0] == "\n"

def read_data(filename):
    """Read data from filename and return a nicer data structure"""

    data = []
    with open(filename, "r") as f:
        for idValue, nextIdValue in groupby(f, search):
             for row in nextIdValue:
                    data.append([row])
                    # print row
    return data

Output=read_data("/Users/adityanisal/arbit/io/fileOutput.txt")
# o1=Output[0]
# o2=Output[1]
# o3=Output[2]
# o4=Output[3]
# print Output
# print o1, o2, o3, o4

## !!!! ## Important Logic ## !! ##
idlist = Dummie.reg_current_id[1:]
idlist_two = Dummie.reg_current_id[1:]
print "IDLIST", idlist_two


nidlist = Dummie.reg_nextState_id[1:]
print "NID",nidlist

try:
    if len(idlist_two)>=len(nidlist):
        for i in range(len(idlist_two)):
            if idlist_two[i]!=nidlist[i]:
                print "Here is the error", nidlist[i+1], "for Id list", idlist[i]
except IndexError:
    print "Index Error"


if len(idlist_two)==len(nidlist):
    for i in range(len(idlist_two)): # assuming the lists are of the same length
        if idlist_two[i]==nidlist[i]:
            print "Following is the error", nidlist[i]
## Till here !! ##

# nos=len(nidlist_two)
#
# # G1=networkx.path_graph(nos)
# # ctr1=count(1)
# # for id1 in nidlist_two:
# #     node1_num=ctr1.next()
# #     networkx.set_node_attributes(G1,id,id1)
# # print(G1.nodes())
# # print ">>>>>>>>>>>", ctr1
#
# G1=networkx.DiGraph()
# ctr1=count(1)
# for id2 in idlist:
#     node1_num = ctr1.next()
#     G1.add_node(node1_num, id=id2)
#     G1.add_edge(node1_num, node1_num + 1, id=id2)
# # G1_data=G1.nodes(data=True)
# # G1_edge_data=G1.edges(data=True)
#
# G2=networkx.DiGraph()
# ctr2=count(1)
# for id2 in idlist:
#     node2_num = ctr2.next()
#     # G2.add_node(node2_num, id=id2)
#     G2.add_edge(node2_num, node2_num + 1, id=id2)
# G2_data=G1.nodes(data=True)
# G2_edge_data=G1.edges(data=True)
# # print idlist
# # print(G1.nodes())
# # print(G1.edges())
# # print(G2_data)
# # print(G2_edge_data)
# #
# # labels=dict((n,d['id']) for n,d in G2.nodes(data=True))
# # labels
# # networkx.draw(G2, data=True, with_lables=True)
# # # pos=networkx.graphviz_layout(G2,prog='dot')
# # plt.savefig("di" + ".png", dpi = 100)
# # plt.show()
#
# # result=iso.is_isomorphic(G1, G2)
# result=isomorphism.DiGraphMatcher(G1,G2)
# # result.is_isomorphic()
# # result=networkx.is_isomorphic(G1, G2)
#
# print result