class Driver:
    def __init__(self, name):
        self.name = name

    def turn_on_car(self):
        print(f'{self.name} turns on the car!')
        return self

    def drive_the_car(self):
        print(f'{self.name} drives a car!')
        return self

    def stop_the_car(self):
        print(f'{self.name} stops the car!')
        return self


dr = Driver('Max').turn_on_car().drive_the_car().stop_the_car()
