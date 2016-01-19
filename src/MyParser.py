from itertools import count
import networkx
from networkx.algorithms import isomorphism
import matplotlib.pyplot as plt
## !!!! ## Important Logic ## !! ##
idlist = extract.reg_current_id[1:]
# idlist = extract.reg_current_id
idlist_two = extract.reg_current_id

nidlist = extract.reg_nextState_id
nidlist_two = extract.reg_nextState_id

## Till here !! ##

nos=len(nidlist_two)

# G1=networkx.path_graph(nos)
# ctr1=count(1)
# for id1 in nidlist_two:
#     node1_num=ctr1.next()
#     networkx.set_node_attributes(G1,id,id1)
# print(G1.nodes())
# print ">>>>>>>>>>>", ctr1

G1=networkx.DiGraph()
ctr1=count(1)
for id2 in idlist:
    node1_num = ctr1.next()
    G1.add_node(node1_num, id=id2)
    G1.add_edge(node1_num, node1_num + 1, id=id2)
# G1_data=G1.nodes(data=True)
# G1_edge_data=G1.edges(data=True)

G2=networkx.DiGraph()
ctr2=count(1)
for id2 in idlist:
    node2_num = ctr2.next()
    # G2.add_node(node2_num, id=id2)
    G2.add_edge(node2_num, node2_num + 1, id=id2)
# G2_data=G1.nodes(data=True)
# G2_edge_data=G1.edges(data=True)
# print idlist
# print(G1.nodes())
# print(G1.edges())
# print(G2_data)
# print(G2_edge_data)
#
# labels=dict((n,d['id']) for n,d in G2.nodes(data=True))
# labels
# networkx.draw(G2, data=True, with_lables=True)
# # pos=networkx.graphviz_layout(G2,prog='dot')
# plt.savefig("di" + ".png", dpi = 100)
# plt.show()

# result=iso.is_isomorphic(G1, G2)
result=isomorphism.DiGraphMatcher(G1,G2)
# result.is_isomorphic()
# result=networkx.is_isomorphic(G1, G2)

print result