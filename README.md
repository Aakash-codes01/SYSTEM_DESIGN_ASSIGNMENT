# SYSTEM_DESIGN_ASSIGNMENT

Question 2

 - importing the necessary modules, including the abc module for defining abstract base classes.

 - an abstract base class called Vehicle is defined. It contains one abstract method, display_details(), which will be implemented by the concrete vehicle classes.

 - Concrete vehicle classes (Car, Motorcycle, Truck) inherit from the Vehicle abstract base class and provide their own implementations of the display_details() method. Each class displays specific details of the corresponding vehicle type.

 - Another abstract base class called VehicleFactory is defined. It also inherits from abc.ABC and contains one abstract method, create_vehicle(), which will be implemented by the concrete factory classes.

 - Concrete factory classes (CarFactory, MotorcycleFactory, TruckFactory) inherit from the VehicleFactory abstract base class and provide their own implementations of the create_vehicle() method. Each factory class creates a specific type of vehicle object.

 - The main() function is defined, which serves as the entry point of the program. It displays a menu to the user and allows them to choose the type of vehicle they want to manufacture.

 - Inside the main() function, a while loop is used to keep the program running until the user chooses to exit. Based on the user's choice, the corresponding factory is assigned to the factory variable.

 - The selected factory's create_vehicle() method is called, which returns a concrete vehicle object of the appropriate type. This object is assigned to the vehicle variable.

 - Finally, the display_details() method of the created vehicle object is called, which displays the specific details of the vehicle type.

 - The program continues looping until the user chooses to exit by selecting option 4 in the menu.
