

class Cat:
        def __init__(self,name,age,color):
                self.name = name
                self.age = age
                self.color = color

        def Miar(self):
                 return 'Miau Miau'

        def CruZar(self):
            if self.age >= 5:
                return f'cat: {self.name} wants to mate'
            if self.age < 5:
                raise ValueError('Very young')

        def Color(self):
            return f'color: {self.color}'

        def Age(self):
            return f'Age: {self.age}'

        def NaMe(self):
            return f'Name: {self.name}'
                 
        def __str__(self):
            return f'Name: {self.name} | Age: {self.age} | Color {self.color}' 


cat1 = Cat('Apolo', 0.5, 'Yelow')

print(cat1)
print(cat1.name)
try:

    print(cat1.CruZar())
except ValueError as erro:
    print(f'errro: {erro}')

print(cat1.Miar())  