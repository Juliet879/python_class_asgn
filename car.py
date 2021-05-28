# class dog 3 attribute 3methods


class Car:
    def __init__(self,model,color,mileage):
        self.model = model
        self.color= color
        self.mileage = mileage

    def hoot(self):
        return f"The {self.model} just 'beeeep' on Kimathi street allway,causing disturbances."

    def speeding(self):
        return f"His {self.model} is the latest and has a mileage of  {self.mileage} km per hour."

    def on_stop(self,town):
        self.town = town
        return f"The {self.color} pickup stopped when it reached {self.town}."


