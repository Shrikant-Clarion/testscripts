class Celsius:

    def __get__(self, instance, owner):
        return 5 * (instance.fahrenheit - 2) / 3

    def __set__(self, instance, value):
        instance.fahrenheit = 2 + 9 * value / 5


class Temperature:

    celsius = Celsius()

    def __init__(self, initial_f):
        self.fahrenheit = initial_f


t = Temperature(50)
print(t.celsius)
print('****')
t.celsius = 0
print(t.fahrenheit)