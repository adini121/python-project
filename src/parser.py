import sys, getopt
from itertools import groupby, repeat
from sys import argv
from extract import extract
from itertools import count
import networkx
from networkx.algorithms import isomorphism
import matplotlib.pyplot as plt


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

idlist = extract.reg_current_id[1:]
# idlist = extract.reg_current_id
idlist_two = extract.reg_current_id

nidlist = extract.reg_nextState_id
nidlist_two = extract.reg_nextState_id


G1=networkx.Graph()
ctr1=count(1)
for id1 in nidlist_two:
    node1_num=ctr1.next()
    G1.add_node(node1_num, id=id1)
print(G1.nodes())

G2=networkx.Graph()
ctr2=count(1)
for id2 in idlist:
    node2_num = ctr2.next()
    G2.add_node(node2_num, id=id2)
G2_data=G2.nodes(data=True)
print(G2.nodes())
print(G2_data)

networkx.draw(G1, with_lables=True)
plt.savefig("out" + ".png", dpi = 1000)
plt.show()

# result=iso.is_isomorphic(G1, G2)
# result=isomorphism.GraphMatcher(G1,G2)
# result.is_isomorphic()
# print result