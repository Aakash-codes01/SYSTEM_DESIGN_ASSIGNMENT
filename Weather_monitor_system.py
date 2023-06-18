from abc import ABC, abstractmethod

# Step 1: Define Subject interface
class WeatherStationSubject(ABC):
    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def unregister_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# Step 2: Define Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, weather_data):
        pass
    
    @abstractmethod
    def display_weather(self,weather_data):
        pass

# Step 3: Implement Weather Station class
class WeatherStation(WeatherStationSubject):
    def __init__(self):
        self.observers = {}
        self.weather_data = {}

    def notify_observers(self):
        for observer in self.observers.values():
            observer.update(self.weather_data)

    def register_observer(self, observer,name):
        self.observers[name] = observer
        self.notify_observers()

    def unregister_observer(self,name):
        self.observers.pop(name)

   

    def update_weather_data(self, temperature, humidity, pressure):
        self.weather_data = {
            'temperature': temperature,
            'humidity': humidity,
            'pressure': pressure
        }
        self.notify_observers()

# Step 4: Implement Display Device classes
class MobileAppDisplay(Observer):
   
    def __init__(self):
        self.local_weather_data = {}
        self.name = "MobileAppDisplay"
    def update(self, weather_data):
        # Update mobile app UI with weather data
        self.local_weather_data = weather_data
        # Update mobile app UI with the weather information
    def display_weather(self):
        for key in self.local_weather_data:
            print(f"{key}:{self.local_weather_data[key]}")

class WebInterfaceDisplay(Observer):
    
    def __init__(self):
        self.local_weather_data = {}
        self.name = "WebInterfaceDisplay"
    def update(self, weather_data):
        # Update web interface UI with weather data
        self.local_weather_data = weather_data
        # Update web interface UI with the weather information
    def display_weather(self ):
         for key in self.local_weather_data:
            print(f"{key}:{self.local_weather_data[key]}")

class DesktopApplicationDisplay(Observer):
    def __init__(self):
        self.local_weather_data = {}
        self.name = "DesktopApplicationDisplay"
    def update(self, weather_data):
        # Update desktop application UI with weather data
        self.local_weather_data = weather_data
        # Update desktop application UI with the weather information
    def display_weather(self ):
        print(self.name)
        for key in self.local_weather_data:
            print(f"{key}:{self.local_weather_data[key]}")

def display_menu():
    print("Weather Monitoring System")
    print("1. Add Observer")
    print("2. Show Weather")
    print("3. Update Weather")
    print("4. unregister user")
    print("5. Exit")
# Usage example

def main():
    weather_station = WeatherStation()
    temperature = 25
    humidity = 60
    pressure = 1012.3
    weather_station.update_weather_data(temperature, humidity, pressure)
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            observer_type = input("Enter observer type (mobile/web/desktop): ")

            if observer_type == 'mobile':
                name = input("Enter Display Name: ")
                observer = MobileAppDisplay()
            elif observer_type == 'web':
                observer = WebInterfaceDisplay()
            elif observer_type == 'desktop':
                observer = DesktopApplicationDisplay()
            else:
                print("Invalid observer type!")
                continue

            weather_station.register_observer(observer,name)
            print("Observer added successfully!")

        elif choice == '2':
            if not weather_station.observers:
                print("No observers registered!")
                continue
            print()
            print("Current Weather:")
            for observer in weather_station.observers :
                print(observer)
                weather_station.observers[observer].display_weather()
                print()
        
        elif choice == '3':
            if not weather_station.observers:
                print("No observers registered!")
                continue

            temperature = float(input("Enter temperature (in Celsius): "))
            humidity = float(input("Enter humidity (in %): "))
            pressure = float(input("Enter pressure (in hPa): "))

            weather_station.update_weather_data(temperature, humidity, pressure)
            print("Weather data updated successfully!")
        elif(choice=='4'):
            print("enter device name")
            name = input()
            weather_station.unregister_observer(name)
            print("user unregistered successfully!")
        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")
        print()

if __name__ == '__main__':
    main()



# Simulate weather data update

