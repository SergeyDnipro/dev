from datetime import datetime, date


class Car:
    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.fuel_consumption = 0

    def __del__(self):
        with open('ukraine_airports.csv', mode='a', encoding='utf-8') as file:
            file.write(f"{self.manufacturer};{self.model};{datetime.now().date()}\n")


class CargoCar(Car):
    def __init__(self, lift_weight: int, manufacturer: str, model: str):
        super().__init__(manufacturer, model)
        self.lift_weight = lift_weight

    def __str__(self):
        return f"{self.manufacturer}:{self.model}:{self.fuel_consumption}:{self.lift_weight}"


car1 = CargoCar(lift_weight=1000, manufacturer='Ford', model='F150')
print(car1)
del car1
