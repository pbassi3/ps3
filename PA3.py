import time

class Node:
    '''
    
    '''
    def __init__(self, data):
        '''
        
        '''
        self.data = data
        self.next = None
        
    def __str__(self):
        '''
        
        '''
        return str(self.data)

    def get_data(self):
        '''
        
        '''
        return self.data

    def get_next(self):
        '''
        
        '''
        return self.next

    def set_data(self, newdata):
        '''
        
        '''
        self.data = newdata

    def set_next(self, newnext):
        '''
        
        '''
        self.next = newnext
class LinkedList:
    def __init__(self):
        self.head = None    
       
        
    def __str__(self):
        '''
        
        '''
        list_str = ""
        curr = self.head
        while curr is not None:
            list_str += str(curr)
            list_str += "->"
            curr = curr.get_next()
        list_str += "None"
        return list_str
        
    def add(self, item):
        '''
        Adds a new item to the list. It needs the item and returns nothing. Assume the item is not already in the list.
        '''
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        
    def append(self, new_value): 
          
        # Allocate new node 
        new_node = Node(new_value) 
          
        # if head is None, initialize it to new node 
        if self.head is None: 
            self.head = new_node 
            return
        curr_node = self.head 
        while curr_node.next is not None: 
            curr_node = curr_node.next
              
        # Append the new node at the end 
        # of the linked list 
        curr_node.next = new_node 
        
    def insert(self, index, item):
        '''
        Adds a new item to the list at position pos. It needs the item and returns nothing. 
        Assume the item is not already in the list and there are enough existing items to have position pos.
        '''
        if index == 0:
            self.add(item)
        else: # not adding at front. stop one before location
            curr = self.head
            i = 0
            while curr.get_next() is not None and i < index - 1:
                curr = curr.get_next()
                i += 1
            temp = Node(item)
            temp.set_next(curr.get_next())
            curr.set_next(temp)
        
    def pop(self, index=None):
        '''
        Removes and returns the item at position index. It needs the position and returns the item. 
        If index is not specified, removes and returns the last item in the list.
        Assume the item is in the list.
        '''    
        if index is None:
            index = self.size() - 1

        if index == 0:
            curr = self.head
            self.head = self.head.get_next()
            return curr
        else: # not popping front. stop one before location
            curr = self.head
            i = 0
            while curr.get_next() is not None and i < index - 1:
                curr = curr.get_next()
                i += 1
            to_pop = curr.get_next()
            curr.set_next(to_pop.get_next())
            return to_pop
    
    def remove(self, item):
        '''
        Removes the item from the list. It needs the item and modifies the list. Assume the item is present in the list.
        '''
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
    
    def search(self, item):
        '''
        Searches for the item in the list. It needs the item and returns the index of the item (-1 if not found).
        Combined a Boolean search(item) with index(item) function.
        '''
        current = self.head
        found = -1
        loc = 0
        while current != None and found == -1:
            if current.get_data() == item:
                found = loc
            else:
                current = current.get_next()
            loc += 1

        return found
    
    def is_empty(self):
        '''
        Tests to see whether the list is empty. It needs no parameters and returns a boolean value.
        '''
        return self.head == None
    
    def size(self):
        '''
        Returns the number of items in the list. It needs no parameters and returns an integer.
        '''
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def asc_ordered_list(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        if temp.data > data:
            new_node.next = temp
            self.head = new_node
            return

        while temp.next:
            if temp.next.data > data:
                break
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def desc_ordered_list(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        if data > temp.data:
            new_node.next = temp
            self.head = new_node
            return

        while temp.next:
             if temp.data > data and temp.next.data < data:
                 break
             temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def display_list(self):
        temp = self.head
        while temp is not None:
            print("{0}".format(temp.data))
            temp = temp.next


# Using this for a descending linked list
#if __name__ == "__main__":
    #llist = LinkedList()
    
    #llist.desc_ordered_list(8)
    #llist.desc_ordered_list(3)
    #llist.desc_ordered_list(1)
    #llist.desc_ordered_list(4)
    #llist.desc_ordered_list(5)
    #llist.desc_ordered_list(7)
    #llist.desc_ordered_list(6)
    #llist.desc_ordered_list(2) 
    #llist.display_list()
   
    
  # For random linked list
    #llist2= LinkedList() 
    #llist2.add(4)
    #llist2.add(5)
   # llist2.add(1)
   # llist2.add(7)
   # llist2.add(8)
  #  llist.add(78)
  #  llist.add(56)
    #print(llist2)
   
    
    # Would use this for an ascending linked list
    # llist.asc_ordered_list(8)
    #llist.asc_ordered_list(4)
    #llist.asc_ordered_list(5)
    #llist.asc_ordered_list(7)
   # llist.asc_ordered_list(6)
   # llist.asc_ordered_list(2) 
  

    def sortedMerge(self, a, b): 
        result = None
          
        # Base cases 
        if a == None: 
            return b 
        if b == None: 
            return a 
              
        # pick either a or b and recur.. 
        if a.data <= b.data: 
            result = a 
            result.next = self.sortedMerge(a.next, b) 
        else: 
            result = b 
            result.next = self.sortedMerge(a, b.next) 
        return result 
      
    def mergeSort(self, h): 
          
        # Base case if head is None 
        if h == None or h.next == None: 
            return h 
  
        # get the middle of the list  
        middle = self.getMiddle(h) 
        nexttomiddle = middle.next
  
        # set the next of middle node to None 
        middle.next = None
  
        # Apply mergeSort on left list  
        left = self.mergeSort(h) 
          
        # Apply mergeSort on right list 
        right = self.mergeSort(nexttomiddle) 
  
        # Merge the left and right lists  
        sortedlist = self.sortedMerge(left, right) 
        return sortedlist 
      
    # Utility function to get the middle  
    # of the linked list  
    def getMiddle(self, head): 
        if (head == None): 
            return head 
  
        slow = head 
        fast = head 
  
        while (fast.next != None and 
               fast.next.next != None): 
            slow = slow.next
            fast = fast.next.next
              
        return slow 
          
# Utility function to print the linked list  
def printList(head): 
    if head is None: 
        print(' ') 
        return
    curr_node = head 
    while curr_node: 
        print(curr_node.data, end = " ") 
        curr_node = curr_node.next
    print(' ') 
      
# Driver Code 
if __name__ == '__main__': 
    li = LinkedList() 
      
    
    
    # The list shall be a: 2->3->20->5->10->15  
    li.append(15) 
    li.append(10) 
    li.append(5) 
    li.append(20) 
    li.append(3) 
    li.append(2) 
      
    # Apply merge Sort  
    li.head = li.mergeSort(li.head) 
    print (" The sorted Linked List using Merge Sort is:") 
    printList(li.head) 

# Function to sort a linked list  
# using selection sort algorithm 
# by swapping the next pointers  
def selectionSort(head):  
  
    a = b = head  
  
    # While b is not the last node  
    while b.next:  
  
        c = d = b.next
  
        # While d is pointing to a valid node  
        while d:  
  
            if b.data > d.data:  
  
                # If d appears immediately after b  
                if b.next == d:  
  
                    # Case 1: b is the head  
                    # of the linked list  
                    if b == head:  
  
                        # Move d before b  
                        b.next = d.next
                        d.next = b  
  
                        # Swap b and d pointers  
                        b, d = d, b  
                        c = d  
  
                        # Update the head  
                        head = b  
  
                        # Skip to the next element  
                        # as it is already in order  
                        d = d.next
                      
                    # Case 2: b is not the head  
                    # of the linked list  
                    else:  
  
                        # Move d before b  
                        b.next = d.next
                        d.next = b  
                        a.next = d  
  
                        # Swap b and d pointers  
                        b, d = d, b  
                        c = d  
  
                        # Skip to the next element  
                        # as it is already in order  
                        d = d.next
                      
                # If b and d have some non-zero  
                # number of nodes in between them  
                else: 
  
                    # Case 3: b is the head  
                    # of the linked list  
                    if b == head:  
  
                        # Swap b.next and d.next  
                        r = b.next
                        b.next = d.next
                        d.next = r  
                        c.next = b  
  
                        # Swap b and d pointers  
                        b, d = d, b  
                        c = d  
  
                        # Skip to the next element  
                        # as it is already in order  
                        d = d.next
  
                        # Update the head  
                        head = b  
                      
                    # Case 4: b is not the head 
                    # of the linked list  
                    else:  
  
                        # Swap b.next and d.next  
                        r = b.next
                        b.next = d.next
                        d.next = r  
                        c.next = b  
                        a.next = d  
  
                        # Swap b and d pointers  
                        b, d = d, b  
                        c = d  
  
                        # Skip to the next element  
                        # as it is already in order  
                        d = d.next
                      
            else: 
  
                # Update c and skip to the next element  
                # as it is already in order  
                c = d  
                d = d.next
  
        a = b  
        b = b.next
      
    return head  

# Function to print the list  
def printList(head):  
  
    while head:  
        print(head.data, end = " ")  
        head = head.next
  
# Driver Code  
if __name__ == "__main__": 
  
    head = Node(55)  
    head.next = Node(44)  
    head.next.next = Node(73)  
    head = selectionSort(head)  
    print(" The sorted linked list using Selection sort is: " )
    printList(head) 
    
    
count = 0
 
def bubbleSort(arr): 
    global count
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element
            count += 1 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
arr = [75,18,13,68,27,91,23,46] 
  
bubbleSort(arr) 
  
print ("\nThe Bubble sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]), 
  




for n in [500, 1000, 5000, 10000]:
    startTime = time.time()
    count = 0
    bubbleSort(list(range(n)))
    endTime = time.time()
    print(f"N : {n}, Time : {endTime-startTime}, Count of operations : {count}")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

s1 = pd.Series([124750, 499500, 12497500, 49995000], index=[500, 1000, 5000, 10000], name="s1")
#s2 = pd.Series([1000400, 3999374, 99946590, 399770054], index=[500, 1000, 5000, 10000], name="s2")
#s3 = pd.Series([2693079, 9860287, 251320053, 953027247], index=[500, 1000, 5000, 10000], name="s3")
#s4 = pd.Series([1139655, 4526769, 112543347, 449865228], index=[500, 1000, 5000, 10000], name="s4")
#s5 = pd.Series([1000689, 2885861, 108040588, 307912139], index=[500, 1000, 5000, 10000], name="s5")
#s6 = pd.Series([2127301, 4673410, 110782327, 414933108], index=[500, 1000, 5000, 10000], name="s6")
sers = [s1]

x_locs = np.arange(1, 5)
x_labels = [500, 1000, 5000, 10000]
f, ax = plt.subplots()
ax.set_title("Descending Sorted")
ax.set_ylabel("Total operations")
ax.set_xlabel("List size N")
ax.set_xticks(x_locs)
ax.set_xticklabels(x_labels)
for ser in sers:
    plt.plot(x_locs, ser, label=ser.name)
plt.legend(loc=0)


