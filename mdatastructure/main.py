from mdatastructure.mycollection import MLinkedList, MStack, MQueue
'''
Created on Dec 26, 2017

@author: redwan
'''
from mdatastructure.graph import Edge, Graph

if __name__ == '__main__':
    pass
def just_print(inp):
    print("-- "+inp+" --")

ab=Edge("a","b")
ac=Edge("a","c")
bd=Edge("b","d")
be=Edge("b","e")
bf=Edge("b","f")
dh=Edge("d","h")
de=Edge("d","e")
ei=Edge("e","i")
ef=Edge("e","f")
fg=Edge("f","g")
fc=Edge("f","c")
ck=Edge("c","k")

graph=Graph([ab,ac,bd,be,bf,dh,de,ei,ef,fg,fc,ck])
graph.bfs(just_print)

