# CIT Python Quiz Week 4

1. Create a 2-D array and slice out the second number in the second column
import numpy as np

a = np.array([[2, 4, 6, 8], [10, 20, 30, 40]])
print(a)
b = a[0:2, 0:3]
print(b)


2. Write a python program to sort array element in the ascending/descending order

n=int(input(“Enter size of array\n“))
arr=list(map(int,input(“Enter elements of array\n“).split()))
arr.sort(reverse=False) #arr.sort() also be used
print(“Ascending order array”)
print(*arr)
arr.sort(reverse=True)
print(“Descending order array”)
print(*arr)

3. Write a python program to find the maximum and minimum value in a given 2-D array
# import numpy library
import numpy
 
# creating a numpy array of integers
arr = numpy.array([1, 5, 4, 8, 3, 7])
 
# finding the maximum and
# minimum element in the array
max_element = numpy.max(arr)
min_element = numpy.min(arr)
 
# printing the result
print('maximum element in the array is: ',
      max_element)
print('minimum element in the array is: ',
      min_element)

4.  Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on following criteria
    - percentage less than `50` (Grade C)
    - percentage equal to `50` and less than `80` (Grade B)
    - percentage equal to `80` and more than `80` (Grade A)
# Python Program to Calculate Total Marks Percentage and Grade of a Student

print("Enter the marks of five subjects::")

subject_1 = float (input ())
subject_2 = float (input ())
subject_3 = float (input ())
subject_4 = float (input ())
subject_5 = float (input ())

total, average, percentage, grade = None, None, None, None

# It will calculate the Total, Average and Percentage
total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
average = total / 5.0
percentage = (total / 500.0) * 100

if average >= 90:
    grade = 'A'
elif average >= 80 and average < 90:
    grade = 'B'
elif average >= 70 and average < 80:
    grade = 'C'

# It will produce the final output
print ("\nThe Total marks is:   \t", total, "/ 500.00")
print ("\nThe Average marks is: \t", average)
print ("\nThe Percentage is:    \t", percentage, "%")
print ("\nThe Grade is:         \t", grade)

5. Write a python program to fetch only Email ID from text file  which include following fields -:
    - Name
    - Mobile Number
    - Roll Number
    - Email ID

import re
fileToRead = 'readText.txt'
fileToWrite = 'emailExtracted.txt'
delimiterInFile = [',', ';']
def validateEmail(strEmail):
    # .* Zero or more characters of any type. 
    if re.match("(.*)@(.*).(.*)", strEmail):
        return True
    return False
def writeFile(listData):
    file = open(fileToWrite, 'w+')
    strData = ""
    for item in listData:
        strData = strData+item+'\n'
    file.write(strData)
listEmail = []
file = open(fileToRead, 'r') 
listLine = file.readlines()
for itemLine in listLine:
    item =str(itemLine)
    for delimeter in delimiterInFile:
        item = item.replace(str(delimeter),' ')
    
    wordList = item.split()
    for word in wordList:
        if(validateEmail(word)):
            listEmail.append(word)
if listEmail:
    uniqEmail = set(listEmail)
    print(len(uniqEmail),"emails collected!")
    writeFile(uniqEmail)
else:
    print("No email found.")
6. Write a function for checking the speed of drivers. This function should have one parameter: speed.
    - If speed is less than 70, it should print “Ok”.
    - Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
    - If the driver gets more than 12 points, the function should print: “`License suspended`”

def check_speed(speed):
    if speed <= 70:
        return 'Ok'
    elif speed >= 70:
        points = (speed - 70) // 5
        print('points = {}'.format(points))
        if points >= 12:
            return 'License suspended'
check_speed(80)
points = 2


7. Write a function called `show_stars(rows)`. If rows is 5, it should print the following:
```bash
*
**
***
****
*****
```
# number of rows
rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")

8. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
nl=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))

9. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:

```bash
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
```
values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)



10. Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
`100,150,180`
The output of the program should be:
`18,22,24`

import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))

11. Write a function to compute 5/0 and use try/except to catch the exceptions.
def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("Why on earth you are dividing a number by ZERO!!")
except:
    print("Any other exception")


12. Create a nesting list that prints out the color and the car brand.

13. Bonus Question: Algorithm challenge: Create your own sorting algorithm.
