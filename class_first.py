class Person:
    def __init__(self, name: str, salary):
        self.name = name
        self.money = 0
        self.salary = salary


class CommonClass:
    def __init__(self):
        self.money = 10000
        self.people = []

    def money_paid(self):
        for person in self.people:
            if person.salary <= self.money:
                person.money += person.salary
                self.money -= person.salary
            else:
                print('not enough money')
                return


class SimplePerson(Person):
    def __init__(self, name: str, salary, height: int = 0):
        super().__init__(name, salary)
        self.height = height


human1 = SimplePerson(name='Alex', salary=1000, height=100)
human1.height = 100


a1 = Person('Alex', 550)
a2 = Person('Sergey', 1000)
print(a1.money)
print(a2.money)

common = CommonClass()
common.people.append(a1)
common.people.append(a2)

for i in range(10):
    common.money_paid()

    print(f"alex={a1.money}")
    print(f"sergey={a2.money}")
    print(common.money)
