# car Class.3 attribute,3methods

class Dog:
    def __init__(self,name,color,age):
        self.name = name
        self.color= color
        self.age = age

    def eat(self,food):
        self.food = food
        return f"My dog {self.name} likes eating {self.food} in the evening"

    def bark(self):
        return f"Yesterday night I saw a {self.color} dog barking wowowow"

    def birthday(self):
        return f"{self.name} will be {self.age} years old come next year"


