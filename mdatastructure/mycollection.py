'''
Created on Dec 25, 2017

@author: redwan
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def set_data(self,data):
        self.data = data

    def set_next(self,nextNode):
        self.next = nextNode
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next
    
class MLinkedList:
        def __init__(self):
            self.head=None
            self.size=0
        def insert(self,newData):
            newNode=Node(newData)
            if(self.head is None):
                self.head=newNode
            else:
                tempNode=self.head;
                while(tempNode.get_next() is not None):
                    tempNode=tempNode.get_next()
                tempNode.set_next(newNode)
            self.size=self.size+1;
            return
        def delete_head(self):
            if (self.head is None):  return
            self.head=self.head.get_next()
            self.size=self.size-1
            return
        def delete_at_index(self,index):
            if(index>=self.size): return None
            if(index==0):
                self.delete_head()
                return
            if(self.head is None):
                return 
            else:
                i=0;
                tempNodeC=self.head;
                tempNodeP=None
                while(i<index):
                    tempNodeP=tempNodeC
                    tempNodeC=tempNodeC.get_next()
                    i=i+1
                tempNodeP.set_next(tempNodeC.get_next())
                tempNodeC.set_next(None)
                self.size=self.size-1
            return
        def get_size(self):
            return self.size
        def contains(self,nodeData):
            if(self.head is None):
                return False
            else:
                tempNode=self.head;
                while(tempNode is not None):
                    if(tempNode.get_data()==nodeData):
                        return True
                    tempNode=tempNode.get_next()
            return False
        def get_element_at(self,index):
            if(index>=self.size): return None
            if(self.head is None):
                return None
            else:
                i=0;
                tempNode=self.head;
                while(i<index):
                    tempNode=tempNode.get_next()
                    i=i+1
                return   tempNode.get_data()                  
        
class MStack:
    def __init__(self):
        self.list=MLinkedList()
        self.size=0;
        return
    def push(self,newData):
        self.list.insert(newData)
        self.size=self.size+1;
        return
    def pop(self):
        if(self.list.get_size()==0):return None
        top=self.list.get_element_at(self.size-1)
        self.list.delete_at_index(self.size-1)
        self.size=self.size-1;
        return top
    def peek(self):
        if(self.list.get_size()==0):return None
        top=self.list.get_element_at(self.size-1)
        return top
    def is_empty(self):
        return self.size==0
    def get_size(self):
        return self.size
      
class MQueue:
    def __init__(self):
        self.stack=MStack()
        self.stackTemp=MStack()
        self.size=0;
        return
    def queue(self,newData):
        self.stack.push(newData)
        self.size=self.size+1;
    def dequeue(self):
        if(self.stackTemp.is_empty()):
            while(self.stack.is_empty()!=True):
                tempo=self.stack.pop()
                self.stackTemp.push(tempo)
        topVal= self.stackTemp.pop()
        if(topVal is not None):self.size=self.size-1;
        return topVal
    def is_empty(self):
        return self.size==0
    def get_size(self):
        return self.size     
        
        