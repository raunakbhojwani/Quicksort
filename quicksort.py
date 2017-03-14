#Author: Raunak Bhojwani
#Created: November 2 2014
#Lab3: Quicksort
#Creating functions that implement the quicksort

def compare_int(a, b):                                                      # Compare function for integers
    return a <= b

def swap(the_list, i, j):                                                   # Swap function to swap the elements at indexes i and j
    temp = the_list[i]
    the_list[i] = the_list[j]
    the_list[j] = temp
  
def partition(the_list, p, r, compare_func):                                # Partition function
    pivot = the_list[r]                         # Initialize the pivot, i and j
    i = p-1                                     
    j = p
    while j != r:
        if compare_func(the_list[j], pivot):    # Compare the element at index j and the pivot
            i += 1                              # increment i
            swap(the_list, i, j)                # do the necessary swap
        j += 1                                                              # Always increment j
    swap(the_list, i+1, r)                      # swap the pivot to between two sublists
    return i+1                                  # return q
  
def quicksort(the_list, p, r, compare_func):                                # Recursive quicksort function
    if len(the_list[p:r+1]) >= 2:                   # Base case (if length is less than 2, it is sorted)
        q = partition(the_list, p, r, compare_func)                         # Partition the original list
        quicksort(the_list, p, q-1, compare_func)                           # Recursively call quick sort on both sublists
        quicksort(the_list, q+1, r, compare_func)
  
def sort(the_list, compare_func):                                           # Sort function for whole lise (p=0 and r = length -1)
    quicksort(the_list, 0, len(the_list)-1, compare_func)
    
# the_list = [1]
# print sort(the_list, compare_int)
# print the_list
    