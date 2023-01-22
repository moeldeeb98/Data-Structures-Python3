
# PROS
# - you can add and remove elements quickly. 
#   this also doesn't require reorganizing the data structure unlike arrays or lists.
# - Linked lists also don't require a fixed size or initial size due to their chainlike structure

# CONS
# - More memory is required when compared to an array. 
#   This is because you need a pointer (which takes up its own memory) to point you to the next element.
# - Search operations on a linked list are very slow. 
#   Unlike an array, you don't have the option of random access.

# When Should You Use a Linked List over an array ?
# - you don't know how many items will be in the list
# - you don't need random access to any elements
# - you want to be able to insert items in the middle of the list
# - you need constant time insertion/deletion from the list 
#   (you don't have to shift every other item in the list first)
if __name__ == "__main__":

    ar = [1,2,3,4,5]
    len(ar)

    print("HI") 