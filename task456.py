#Python program to swap two variables

x = 5
y = 10

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


#Kilometers to Miles
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))





# choose a random element from a list
from random import seed
from random import choice
# seed random number generator
seed(1)
# prepare a sequence
sequence = [i for i in range(50)]
print(sequence)
# make choices from the sequence
for _ in range(5):
	selection = choice(sequence)
	print(selection)



# Python program to demonstrate the use of
# choice() method
 
import random
 
# prints a random value from the list
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))
 
# prints a random item from the string
string = "striver"
print(random.choice(string))
