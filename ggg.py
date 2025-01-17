class Pat:

    def __init__(self, name=None, height=50 , weight=2):
        self.name = name
        self.height = height
        self.weight = weight

    def __str__(self):
        return f'I am a pat and my name is {self.name}'

    def __len__(self):
        return f'I am pat and my height is {self.height}'

    def __bool__(self):
        return f'I am a pat and my weight is {self.weight}'


first_pat = Pat(name="Cat")
print(first_pat.__len__())
print(first_pat.__bool__())
print(first_pat)

print("_______________________________")

second_pat = Pat(name="Dog")
second_pat = Pat(height=80)
second_pat = Pat(weight=5)
print(second_pat.__str__())
print(second_pat.__len__())
print(second_pat.__bool__())
print(second_pat)

print("_______________________________")

Third_pat = Pat(name="Bird")
Third_pat = Pat(height=10)
Third_pat = Pat(weight=1)
print(Third_pat.__len__())
print(Third_pat.__bool__())
print(Third_pat)

print("_______________________________")

class Human:

    def __init__(self, name=None, height=156, weight=41 , pats="Cat,Dog,Bird"):
        self.name = name
        self.height = height
        self.weight = weight
        self.pats = pats



    def __str__(self):
        return f'Hi my name is {self.name}'


    def __len__(self):
        return f'And my height is {self.height}'


    def __bool__(self):
        return f'MY weight is  {self.weight}'

    def __del__(self):
        return f'I have pats,and their names is {self.pats}'

first_human = Human(name="Vika")
print(first_human.__del__())
print(first_human.__len__())
print(first_human.__bool__())
print(first_human)
