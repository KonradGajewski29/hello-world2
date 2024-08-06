# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 14:10:24 2021

@author: Konrad
"""
#help('modules') to see all modules
def Minkowski_add(A,B):
    #works on tuples and numpy
    if isinstance(A,int) or isinstance(A,float):
        A=[A]
    if isinstance(B,int) or isinstance(B,float):
        B=[B]
    #try:
     #   len(A)
      #  len(B)
    #except:
    #    raise Exception('A,B must be lists or ndarray')
    summation=zeros((len(A)*len(B)))
    cursor=0
    for i in range(len(A)):
        for j in range(len(B)):
            summation[cursor]=A[i]+B[j]
            cursor+=1
    return summation
def pair(A,B):
    new_array=[]
    cursor=0
    for i in range(len(A)):
        for j in range(len(B)):
            new_array.append((A[i], B[j]))
            cursor+=1
    return new_array
            
def array_to_tuple(A):
    tup=[]
    for i in range(len(A)):
        tup.append(tuple(A[i]))
    return tup

def unique_order(A): 
    a=[]
    for i in range(len(A)):
        if A[i] not in a:
            a.append(A[i])
    return array(a)
from networkx import *
import numpy
from numpy import *
from matplotlib import *
A=numpy.matrix([[0,1],[0,0]])
G=from_numpy_matrix(A)
#G=G.to_directed
print 'number of nodes', G.number_of_nodes()
print 'nodes', G.nodes()
print 'edges', G.edges()
#NE=[list(array(5*ones((1000000,1))))]
#NE=random.randint(50, size=100)
NE=[[-1,1]]
www=unique_order([2,3,1,2,2,2])
print 'www', www
S_0=(0,0)
a=DiGraph()
parent_node=[S_0]
a.add_nodes_from(parent_node)

parent_S=[S_0[1]]
new_nodes=Minkowski_add(parent_S,NE[0])
new_array=concatenate((ones((len(new_nodes),1)), new_nodes.reshape(len(new_nodes),1)),axis=1)

child_node=array_to_tuple(new_array)
a.add_nodes_from(child_node)
edges=pair(parent_node,child_node)
a.add_edges_from(edges)
time=0
all_children_nodes=child_node
print 1
for i in [2]:
   parent_node=all_children_nodes
   parent_S=unique_order(array(parent_node)[:,1])
   all_children_nodes=[]    
   #parent_S=array(parent_node)[:,1]
   for j in range(len(parent_S)):
       
       new_nodes=unique_order(Minkowski_add(parent_S[j],NE[0]))
       new_array=concatenate((i*ones((len(new_nodes),1)), new_nodes.reshape(len(new_nodes),1)),axis=1)

       child_node=array_to_tuple(new_array)
       a.add_nodes_from(child_node)
       edges=pair([parent_node[j]],child_node)
       a.add_edges_from(edges)
       print parent_S[j]
       print child_node
       for k in range(len(child_node)):
           if child_node[k] not in all_children_nodes:
               all_children_nodes.append(child_node[k])
      
print len(a.nodes())
print len(a.edges())
draw(a,with_labels=True,arrows=True)

print 'end'







def numpy_matrix_to_directed_graph(A):
    try:
        A.shape[0]==A.shape[1]
    except:
            raise Exception('Must be a square matrix')
    G=DiGraph()
    G.add_nodes_from(range(len(A)))
    edges=[]
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            if A[i,j]==1:
                edges.append((i,j))
    G.add_edges_from(edges)
    return G
q=numpy_matrix_to_directed_graph(A)
#print 'nodes', q.nodes()
#print 'edges', q.edges()

        
    