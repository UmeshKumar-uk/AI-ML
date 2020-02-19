# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 09:43:49 2020

@author: moniu
"""

graph ={
        1:[1,2,6],
        2:[5],
        3:[4],
        4:[2,1],
        5:[None],
        6:[None]
        
    }
print(graph)
def edges(graph):
        edges = []
        for nodes in graph:
            for neighbour in graph[nodes]:
                edge.append((nodes,neighbour))
                return (edge)
        print("edges",edges(graph))
        def add_a_node():
            addnode= input("enter the value of node that needs to be added")
            a=int(addnode)
            addvalueofnode = input("how many value in this vertices")
            b=int(addvalueofnode)
            for i in range(b):
                c=int(input())
                graph[a]=[b]
                print(graph)
                print(edges(graph))
                
            def del_a_node():
                delanode = input("enter the value of node to be deleted")
                valuetobedeleted = int(delnode)
                for deletion in graph: 
                    if valuetobdeteled in graph: 
                        del graph[valuetobdeleted]
                        print(graph)
                        print(edges(graph))
                    else:
                        print("invalid number entered")
                        quit()
            def update_a_node():
                print("update a node")
                
            def display_a_node():
                print("display")
            
            switchdict = { 
                    1:add_a_node,
                    2:del_a_node,
                    3:update_a_node,
                    4:display_a_node,
                    
            }
            selection = 0
            while(selection !=4 ):
                print("press 1: to add a node")
                print("press 2: to del a node")
                print("press 3: to update a node")
                print("press 4 to display a node")
                selection = int(input("Enter the number"))
                if(selection>0)and (selection < 4):
                        switchdict[selection]()
            