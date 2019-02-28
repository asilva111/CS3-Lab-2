# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 13:15:17 2019
CS 2302 - Andres Silva
> Teacher: Olac Fuentes
> TAs: Anindita Nath  & Maliheh Zargaran
> Lab #2
> The purpose of this lab is to implement different sorting algorithms and compare their efficiency based on the size 
of the provided list to be sorted.
> LAST MODIFIED: FEB 27th, 2019
"""
import random
import time
from LinkedListModelCode import *

counter = 0 #Counts number of comparasions.

def CreateLL(n):
    LL = List()
    for i in range(n):
        LL.Append(random.randint(0,1000))
    return LL  

def MedianBB(L):
    C = Copy(L)
    BubbleSort(C)
    
    return ElementAt(C, C.getLength()//2)

def MedianQS(L):
    C = Copy(L)
    QuickSort(C)
    
    return ElementAt(C, C.getLength()//2 )



def Copy(L):
    tempHead = L.head
    C = List()
    while L.head != None:
        C.Append(L.head.item)
        L.head = L.head.next 
    L.head = tempHead
    
    return C
        
def ElementAt(L,n): #median is middle element when list is odd.
        for i in range(n):
                L.head = L.head.next
        return L.head.item
  
    
def SplitLeft(L,p): #Returns List with items smaller than pivot 
    OgNode = L.head #Store original node to keep L intact
    L1 = List() #Empty list to be filled
   
    while L.head != None: #Append all items smaller than pivot
        if L.head.item < p:
            L1.Append(L.head.item)
        L.head = L.head.next
    
    L.head = OgNode #Repoint L's head
    return L1 #Return L1, filled with items smaller than p

def SplitRight(L,p): #Returns List with items greater than pivot 
    OgNode = L.head #Store original node to keep L intact
    L2 = List() #Empty list to be filled
    
    while L.head != None: #Append all items greater than pivot
        if L.head.item > p: 
            L2.Append(L.head.item)
        L.head = L.head.next
   
    L.head = OgNode#Repoint L's head
    return L2 #Return L2, filled with items greater than p
        

def BubbleSort(L): 
    global counter
    counter = 0
    Status = False
    while Status is not True: #Status variable that will check if list is sorted.
        Status = True
        temp = L.head
        while temp.next is not None: #Go through all the list until the end is reached.
            if temp.item > temp.next.item: #If the current item is larger thant he next:
                counter += 1
#                print(counter)
                temp2 = temp.item #Swap items
                temp.item = temp.next.item
                temp.next.item = temp2
                Status = False #Set status to false in order to tell code that list is not sorted yet.
            temp = temp.next #Advance List.

def QuickSort(L):
    global counter 
    
    temp = L #Work with temp to not modify L.
    if L.getLength() > 1: #If current list has more than 1 element, it might not be sorted
        
        tempNode = L.head #Store Head of Original List to repoint later and keep intact L.
        
        while temp.head.next != None: #Take the last item as pivot
            temp.head = temp.head.next
        
        pivot = temp.head.item    #Pivot is the last item of list   
#        DEBUG: print("\nPivot is: ", pivot, "\n")
        
        temp.head = tempNode #repoint head to first node
        
        L1 = SplitLeft(L,pivot) #Store all items smaller than pivot into L1
        L2 = SplitRight(L,pivot) #Store all items greater than pivot into L2
       
        QuickSort(L1) #Sort smaller lists.
        QuickSort(L2)
 
       
        #Glue list 
        if L.head == None:#If head is empty
            counter += 1
            L1.Append(pivot)#Insert pivot at end of List 1
            
        else:
            counter += 1
            L2.Prepend(pivot) #If the head is not empty, insert it at the begining of List 2
        
        if L1.head == None: #If L1 is empty, 
            counter += 1
            L.head = L2.head #Make head of Original list the head of L2
            L.tail = L2.tail #Point the tail to last element of L2
            
        else:
            L1.tail.next = L2.head #If L1 is not empty
            L.head = L1.head #The head of L1 becomes the head of the original list
            L.tail = L2.tail#The tail of the original list becomes the tail
    
    else:  #List has 1 element, it is sorted, return.
        return 
   
def MergeSort(L):

    
    tempHead = L.head #save the node of the head
    
    if L.getLength() > 1 :
#        print("if: ")
        L1 = List()
        L2 = List()
        
        for i in range(L.getLength()//2):
            L1.Append(L.head.item)
            L.head = L.head.next
        while L.head != None:
            L2.Append(L.head.item)
            L.head = L.head.next
            
        L.head = tempHead #Restore L's head.
        
        print("L1:")
        L1.Print()
        print("L2:")
        L2.Print()
        
        tempL = List()
        SmallestList = L1
        LargestList = List()
        
        if L1.getLength() > L2.getLength():
            SmallestList = L2
            LargestList = L1
        else:
            SmallestList = L1
            LargestList = L2
        
        MergeSort(L1)
        MergeSort(L2)
        
#        print("smallest List length: ",SmallestList.getLength())
#        for i in range(SmallestList.getLength()):
#            if L1.head.item < L2.head.item:
#                print(L1.head.item, " < ", L2.head.item)
#                tempL.Append(L1.head.item)
#                L1.head = L.head.next
#                
#                print("temp inside loop")
#                tempL.Print()
#                
#            else:
#                tempL.Append(L2.head.item)
#                L2.head = L2.head.next
#        
#        while LargestList.head != None:
#            tempL.Append(LargestList.head.item)
#            LargestList.head = LargestList.head.next
        

        
        print("temp")
        tempL.Print()
        
#        L.head = tempL.head

    else:
        return
    
#Create a list of size n
A = CreateLL(100)




#A.Print()

start = time.time()
x = MedianBB(A)
end = time.time()


print("\nBubbleSort Total time: ", start - end )
print("Median: ", x)
print("Passes: ", counter)


counter = 0



start = time.time()
print("Median: ", MedianQS(A))
end = time.time()
print("Passes: ", counter)
print("\nQuickSort Total time: ", start - end )

















