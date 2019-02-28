# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 19:19:10 2019
CS 2302 - Andres Silva
> Teacher: Olac Fuentes
> TAs: Anindita Nath  & Maliheh Zargaran
> Lab #2  - Linked list Class
> LAST MODIFIED: FEB 27th, 2019
"""
#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
def PrintNodes(N):
    if N != None:
        print(N.item, end=' ')
        PrintNodes(N.next)
        
def PrintNodesReverse(N):
    if N != None:
        PrintNodesReverse(N.next)
        print(N.item, end=' ')
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
    def IsEmpty(L):  
        return L.head == None     
        
    def Append(L,x): 
    # Inserts x at end of list L
        if L.head == None:
            L.head = Node(x)
            L.tail = L.head
        else:
            L.tail.next = Node(x)
            L.tail = L.tail.next
        
    def Print(L):
        # Prints list L's items in order using a loop
        temp = L.head
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
        print()  # New line 

    def PrintRec(L):
        # Prints list L's items in order using recursion
        PrintNodes(L.head)
        print() 
        
    def Remove(L,x):
        # Removes x from list L
        # It does nothing if x is not in L
        if L.head==None:
            return
        if L.head.item == x:
            if L.head == L.tail: # x is the only element in list
                L.head = None
                L.tail = None
            else:
                L.head = L.head.next
        else:
             # Find x
             temp = L.head
             while temp.next != None and temp.next.item !=x:
                 temp = temp.next
             if temp.next != None: # x was found
                 if temp.next == L.tail: # x is the last node
                     L.tail = temp
                     L.tail.next = None
                 else:
                     temp.next = temp.next.next
         
    def PrintReverse(L):
        # Prints list L's items in reverse order
        PrintNodesReverse(L.head)
        print()     
        
    def getLength(L):
        if L.head == None:
            #print("Empty head")
            return 0
        
        else:
            tempHead = L.head
            counter = 0
            
            while L.head != None:
                L.head = L.head.next
                counter += 1
            
            L.head = tempHead
            
            return counter
        
        
    def Prepend(L, x):#Insert data at begining of list
        if L.head == None:
            L.head = Node(x)
            L.tail = L.head
        else:
            new_node = Node(x)
            new_node.next = L.head
            L.head = new_node
                    
                    
    
       
    
