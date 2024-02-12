'''
Title:
    List Exercises

Prerequisites:
    Basic understanding of Python lists.

Objectives:

    Create a list of favorite movies.
    Access specific elements from the list.
    Add and remove movies from the list.
    Sort the list.
    Create a new list with specific elements from the original list.

'''

myList = ['Pulp Fiction', 'Weathering with You', 'Catch Me If You Can', 'Toradora', 'Bakuman']
print(myList[2])

myList.append('Doraemon')
print(myList)

myList.sort()
print(myList)

newList = [myList[0], myList[-1]]
print(newList)