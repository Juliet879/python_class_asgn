# Question1
# Given list x = [100,110,120,130,140,150], use list comprehension to create another list containing each number in the list multiplied by 5.  
x = [100,110,120,130,140,150]
new_list = [ i*5 for i in x]
print(new_list)




# Question2
# Write a function named divisible_by_three that accepts a number n and prints all numbers from 1 to n that are divisible by 3. 
def divisible_by_three(n):
    for number in range(1,n):
        if number%3==0:
            print(number)

divisible_by_three(16)



# Question3
# Given the nested list x = [[1,2],[3,4],[5,6]], write a function that flattens the list and returns it as [1,2,3,4,5,6]
x = [[1,2],[3,4],[5,6]]
new_list = []

for lists in x:
    for numbers in lists:
        new_list.append(numbers)

print(new_list)
 




# Question4
# Write a Python function named smallest that accepts a list of unsorted integers and returns the smallest number in the list. Example:smallest([3,6,8,2,4,1,5,7]) returns 1

def smallest(collection):
    small = min(collection)
    print( small)

smallest([2,54,12,4366,34,52,25])



# Question5
# Write a function that accepts list x below and uses a set to remove the duplicate letters and returns the list without duplicates x = ['a','b','a','e','d','b','c','e','f','g','h']

x = ['a','b','a','e','d','b','c','e','f','g','h']

new_one = set(x)
print(new_one)



# Question6
# Write a function named divisible_by_seven that; using the range function and a for loop returns a list containing all the numbers between 100 and 200 that are divisible by 7.

def divisible_by_seven():
    all_numbers = []
    for number in range(100,200):
        if number%7==0:
            all_numbers.append(number)
    print(all_numbers)

divisible_by_seven()



# Question7
# Given this list of students containing age and name,  students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}], write a function that greets each student and tells them the year they were born. e.g Hello Eunice, you were born in the year 2002.

students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
def greeting():
    for student in students:
        year_of_birth = 2021- student["age"]
        name = student["name"]
        print(f"Hello {name},you were born in the year {year_of_birth}")
greeting()



# Question8
# Create a Class Rectangle with the following Attributes and Methods
# Attributes: The class has attributes width and length that represent the two sides of a rectangle 
# Methods:
#  Add a method named area which returns the area (A) of the rectangle using the formula A=width*length
# Add a method named perimeter which returns the perimeter (P) of the rectangle using the formula P=2(length+width)

class Rectangle:
    def __init__(self,width,length):
        self.width = width
        self.length = length

    def area(self):
        A = self.width * self.length
        return A
    def perimeter(self):
        P = 2*(self.length + self.width)
        return P


rectangle = Rectangle(20,15)
print(rectangle.area())
print(rectangle.perimeter())

        
  