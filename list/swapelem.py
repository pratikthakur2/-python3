#Given a list, write a Python program to swap first and last element of the list.

def swapList(newList):
    size = len(newList)

    #swapping 
    temp = newList[0]
    newList[0] = newList[size]
