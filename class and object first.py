class Contact:
    def __init__(self, name, telephone):
        self.name=name
        self.tel=telephone

    def get_name(self):
        print(self.name)

    def get_tel(self):
        print(self.tel)

person1=Contact("suramy",11134223546)
person2=Contact("sunakoy",19471223549)

print(person1.name)
print(person2.tel)

person1.get_name()
person1.get_tel()




class CuteDog:
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color

    def think(self,content):
        print(f"{self.name} is thinking about {content}")

Dog1=CuteDog("su",18,"blue")
print(f"Dog1's name is {Dog1.name},it's age is {Dog1.age},it's color is {Dog1.color}")

Dog1.think("eating what")


class Mammal:
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
    def breathing(self):
        print(f"{self.name} is breathing")

    def  sleeping(self):
        print(f"{self.name} is sleeping")

class CuteCat(Mammal):
    def __init__(self,name,age,color):
        super().__init__(name,age, color)
        self.hoster=None

    def scratch_sofa(self):
        print(f"{self.name} is scratching sofa")

cat1=CuteCat("koy",17,"blue")
cat1.scratch_sofa()
cat1.breathing()
cat1.sleeping()
