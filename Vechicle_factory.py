from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def display_details(self):
        pass


class Car(Vehicle):
    def display_details(self):
        print("Car Details:")
        print("Number of Wheels: 4")
        print("Seating Capacity: 4")
        print("Maximum Speed: 200 km/h")


class Motorcycle(Vehicle):
    def display_details(self):
        print("Motorcycle Details:")
        print("Number of Wheels: 2")
        print("Seating Capacity: 2")
        print("Maximum Speed: 180 km/h")


class Truck(Vehicle):
    def display_details(self):
        print("Truck Details:")
        print("Number of Wheels: 6")
        print("Seating Capacity: 2")
        print("Maximum Speed: 120 km/h")


class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass


class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()


class MotorcycleFactory(VehicleFactory):
    def create_vehicle(self):
        return Motorcycle()


class TruckFactory(VehicleFactory):
    def create_vehicle(self):
        return Truck()


def main():
    print("Vehicle Manufacturing System")

    while True:
        print("\nChoose the type of vehicle to manufacture:")
        print("1. Car")
        print("2. Motorcycle")
        print("3. Truck")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            factory = CarFactory()
        elif choice == "2":
            factory = MotorcycleFactory()
        elif choice == "3":
            factory = TruckFactory()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")
            continue

        vehicle = factory.create_vehicle()
        vehicle.display_details()


if __name__ == "__main__":
    main()
