# SYSTEM_DESIGN_ASSIGNMENT

 ## Question 1
 
- the code follows a clear structure and addresses the requirements of the weather monitoring system. It utilizes the Observer design pattern to establish a one-to-many relationship between the weather station (subject) and the display devices (observers).

- The WeatherStation class serves as the subject and manages the observers and weather data. It provides methods to register/unregister observers, notify all observers when weather data is updated, and update the weather data.

- The Observer class is an abstract base class that defines the update method. The concrete observer classes (MobileAppDisplay, WebInterfaceDisplay, DesktopApplicationDisplay) inherit from it and implement their own update methods to display the weather data.

- The display_menu function displays the menu options for the user to interact with the system.

- The main function is the entry point of the program. It creates an instance of the WeatherStation class and enters a loop to handle user input based on the selected menu option.

- In the main function, option '1' allows the user to add an observer. They can specify the type of observer (mobile, web, desktop), and the corresponding observer object is created and registered with the weather station.

- Option '2' shows the current weather by notifying all registered observers. If no observers are registered, a message is displayed.

- Option '3' allows the user to update the weather data by providing the temperature, humidity, and pressure. The weather station's update_weather_data method is called to update the data.

- Option '4' allows the user to deregister a already defined user

- Option '5' allows user to exit

 ## Question 2

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
