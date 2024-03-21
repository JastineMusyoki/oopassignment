class Person:
    def __init__(self, name, age, gender):
     self.name=name
     self.age=age
     self.gender=gender
    def introduce(self):
        print(f'Hello, my name is {self.name}. I am {self.age} years old and im {self.gender}')
p1=Person('Mark', 'ten', 'Male')
p1.introduce()              
              
    
    
