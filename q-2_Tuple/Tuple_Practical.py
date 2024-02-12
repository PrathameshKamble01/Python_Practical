'''
Title:
  Tuple Exercises

Prerequisites:
  Basic understanding of Python programming, including tuples and lists.

Objectives:

  Create a tuple of favorite foods and access the second food.
  Attempt to change the second food in the tuple.
  Create a new tuple containing only the first and last foods from the original tuple.
  Determine the number of foods in the tuple using the len() function.
  Convert the tuple to a list and print the list.

'''

#create a tuple of your favorite foods and print the second food in the tuple
myTuple = ('Dragon Fruit', 'Mango', 'Banana', 'Pineapple', 'Watermelon', 'Grapes')
print(myTuple)
print(myTuple[1])

#Try to change the second food in the tuple and see what happens.
'''
myTuple[1] = 'Cherry'
print(myTuple)
'''

#--------------------ERROR----------------------
'''
Traceback (most recent call last):
  File "d:\Python\Python_Course\MCA-SEM-II\Practical_python\Tuple\Tuple_Practical.py", line 7, in <module>
    myTuple[1] = 'Cherry'
    ~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
'''
#--------------------END-----------------------------

#Create a new tuple that contains only the first and last foods in the original tuple and print it.

newTuple = (myTuple[0] + ', ' + myTuple[-1])
print (newTuple)

#Use the len() function to find the number of foods in the tuple and print it.
tupleLength = len(myTuple)
print (tupleLength)

# Convert the tuple to a list and print the list.

convertedList = list(myTuple)
print (convertedList)