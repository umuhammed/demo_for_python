'''
Created on Dec 26, 2017

@author: redwan
'''
from mdatastructure.mycollection import MQueue, MLinkedList

class Edge:
    def __init__(self,v,u):
        self.v=v;
        self.u=u;
        return
class Graph:
    def __init__(self,edges):
        self.edges=edges;
        return
    def get_neighbours(self,vertex):
        neighbours=[];
        for edge in self.edges :
            if(edge.u==vertex):
                if(edge.v not in neighbours):neighbours.append(edge.v)
            elif(edge.v==vertex):
                if(edge.u not in neighbours):neighbours.append(edge.u)
        return neighbours
    def bfs(self, additional_processing):
        if(len(self.edges)==0):return
        root=self.edges[0].v
        visited=MLinkedList()
        visited.insert(root);
        additional_processing(root)
        queue=MQueue();
        queue.queue(root)
        while not queue.is_empty():
            vert=queue.dequeue();
            for neighbour in self.get_neighbours(vert):
                if(not visited.contains(neighbour)):
                    visited.insert(neighbour);
                    queue.queue(neighbour)
                    additional_processing(neighbour)
        return
    