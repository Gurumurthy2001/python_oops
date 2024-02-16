'''Python oops concepts are explained very simply This content may definitely helps to the beginners'''


# Classes and Objects
class Car:
    """
    Represents a simple Car with attributes such as make, model, and methods like start and stop.
    
    Attributes:
    - make (str): The make of the car.
    - model (str): The model of the car.
    - car_running (bool): Indicates whether the car is running or not.
    """
    def __init__(self, make, model):
        """
        Initializes a Car object with the provided make and model.
        
        Parameters:
        - make (str): The make of the car.
        - model (str): The model of the car.
        """
        self.make = make
        self.model = model
        self.car_running = False
    
    def start(self):
        """
        Starts the car if it is not already running.
        """
        if not self.car_running:
            self.car_running = True
            print(f"{self.make} {self.model} is started")
        else:
            print("The car is already running.")
    
    def stop(self):
        """
        Stops the car if it is currently running.
        """
        if self.car_running:
            self.car_running = False
            print(f"{self.make} {self.model} is stopped")
        else:
            print("The car is already stopped.")

car1 = Car('Toyota', 'Lexus')
car2 = Car('Tata', 'Thor')
car1.start()
car2.stop()


# Encapsulation
class Car:
    """
    Represents a Car with encapsulation by using private attributes (_make, _model, _car_running)
    and providing getter and setter methods.
    
    Attributes:
    - _make (str): The make of the car (private).
    - _model (str): The model of the car (private).
    - _car_running (bool): Indicates whether the car is running or not (private).
    """
    def __init__(self, make, model):
        """
        Initializes a Car object with the provided make and model.
        
        Parameters:
        - make (str): The make of the car.
        - model (str): The model of the car.
        """
        self._make = make
        self._model = model
        self._car_running = False
    
    def get_make(self):
        """
        Gets the make of the car.
        """
        return self._make
    
    def get_model(self):
        """
        Gets the model of the car.
        """
        return self._model
    
    def car_running(self):
        """
        Gets the running state of the car.
        """
        return self._car_running
    
    def start(self):
        """
        Starts the car if it is not already running.
        """
        if not self._car_running:
            self._car_running = True
            print(f"{self._make} {self._model} is started")
        else:
            print("The car is already running.")
    
    def stop(self):
        """
        Stops the car if it is currently running.
        """
        if self._car_running:
            self._car_running = False
            print(f"{self._make} {self._model} is stopped")
        else:
            print("The car is already stopped.")

car1 = Car('Toyota', 'Lexus')
car2 = Car('Tata', 'Thor')
car1.start()
car2.stop()
print(car1.get_make())


# Inheritance
class Car:
    """
    Represents a Car with basic functionalities like starting and stopping.
    
    Attributes:
    - _make (str): The make of the car.
    - _model (str): The model of the car.
    - _is_running (bool): Indicates whether the car is running or not.
    """
    def __init__(self, make, model):
        """
        Initializes a Car object with the provided make and model.
        
        Parameters:
        - make (str): The make of the car.
        - model (str): The model of the car.
        """
        self._make = make
        self._model = model
        self._is_running = False
    
    def start(self):
        """
        Starts the car if it is not already running.
        """
        if not self._is_running:
            self._is_running = True
            print(f"{self._make} {self._model} is started")
        else:
            print(f"{self._make} {self._model} is already running")
    
    def stop(self):
        """
        Stops the car if it is currently running.
        """
        if self._is_running:
            self._is_running = False
            print(f"{self._make} {self._model} is stopped")
        else:
            print(f"{self._make} {self._model} is already stopped")

class ElectricCar(Car):
    """
    Represents an Electric Car, inheriting from the Car class.
    
    Attributes:
    - _battery_state (int): The battery state of the electric car.
    """
    def __init__(self, make, model, battery_state):
        """
        Initializes an ElectricCar object with the provided make, model, and battery state.
        
        Parameters:
        - make (str): The make of the electric car.
        - model (str): The model of the electric car.
        - battery_state (int): The initial battery state of the electric car.
        """
        super().__init__(make, model)
        self._battery_state = battery_state
    
    def charge(self):
        """
        Checks and displays the charge status of the electric car.
        """
        if self._battery_state > 20:
            print(f"{self._make} {self._model}'s charge is {self._battery_state}")
        else:
            print("Please plug in charge")

electric_car1 = ElectricCar('Tesla', 'Model-1', 21)
electric_car1.stop()
electric_car1.start()
electric_car1.charge()
print(electric_car1.get_make())
print(electric_car1.get_model())
electric_car1.set_make_model('Tesla-1', 'Model-2')
print(electric_car1.get_make())
print(electric_car1.get_model())
car1.drive()
electric_car1.drive()


# Polymorphism
class Car:
    """
    Represents a basic Car with methods like start, stop, and drive.
    
    Attributes:
    - _make (str): The make of the car.
    - _model (str): The model of the car.
    - _is_running (bool): Indicates whether the car is running or not.
    """
    def __init__(self, make, model):
        """
        Initializes a Car object with the provided make and model.
        
        Parameters:
        - make (str): The make of the car.
        - model (str): The model of the car.
        """
        self._make = make
        self._model = model
        self._is_running = False
    
    def start(self):
        """
        Starts the car if it is not already running.
        """
        if not self._is_running:
            self._is_running = True
            print(f"{self._make} {self._model} is started")
        else:
            print(f"{self._make} {self._model} is already running")
    
    def stop(self):
        """
        Stops the car if it is currently running.
        """
        if self._is_running:
            self._is_running = False
            print(f"{self._make} {self._model} is stopped")
        else:
            print(f"{self._make} {self._model} is already stopped")
    
    def drive(self):
        """
        Displays a generic message indicating driving action.
        """
        print(f"{self._make} {self._model} causes sound and wind pollution during the Drive")

class ElectricCar(Car):
    """
    Represents an Electric Car, inheriting from the Car class.
    
    Attributes:
    - _battery_state (int): The battery state of the electric car.
    """
    def __init__(self, make, model, battery_state):
        """
        Initializes an ElectricCar object with the provided make, model, and battery state.
        
        Parameters:
        - make (str): The make of the electric car.
        - model (str): The model of the electric car.
        - battery_state (int): The initial battery state of the electric car.
        """
        super().__init__(make, model)
        self._battery_state = battery_state
    
    def charge(self):
        """
        Checks and displays the charge status of the electric car.
        """
        if self._battery_state > 20:
            print(f"{self._make} {self._model}'s charge is {self._battery_state}")
        else:
            print("Please plug in charge")
    
    def drive(self):
        """
        Displays a message indicating driving action for an electric car.
        """
        print(f"{self._make} {self._model} with a battery limit {self._battery_state} doesn't cause sound and wind pollution during the Drive")

car1 = Car('Tata', 'Model-5')
electric_car1 = ElectricCar('Tesla', 'Model-1', 21)
electric_car1.stop()
electric_car1.start()
electric_car1.charge()
print(electric_car1.get_make())
print(electric_car1.get_model())
electric_car1.set_make_model('Tesla-1', 'Model-2')
print(electric_car1.get_make())
print(electric_car1.get_model())
car1.drive()
electric_car1.drive()


# Abstraction
from abc import ABC, abstractmethod

class EntertainMedia(ABC):
    """
    Abstract base class representing Entertainment Media.
    """
    @abstractmethod
    def play_media(self):
        """
        Abstract method to play media.
        """
        pass
    
    @abstractmethod
    def pause_media(self):
        """
        Abstract method to pause media.
        """
        pass

class MusicPlayer(EntertainMedia):
    """
    Represents a Music Player implementing the EntertainMedia abstract class.
    
    Attributes:
    - play_button (bool): Indicates whether the music player is in play state.
    """
    def __init__(self, play_button):
        """
        Initializes a MusicPlayer object with the provided play button state.
        
        Parameters:
        - play_button (bool): Indicates whether the music player is in play state.
        """
        self.play_button = play_button
    
    def play_media(self):
        """
        Plays music if the play button is ON.
        """
        if self.play_button:
            print("Music player playing your favorite music")
        else:
            print("Music player is off, please turn it ON")

    def pause_media(self):
        """
        Pauses music if the play button is ON.
        """
        if not self.play_button:
            print("Music player is already in pause state")
        else:
            print("Music player is playing your favorite song. If you want to stop, turn it off")

class VideoPlayer(EntertainMedia):
    """
    Represents a Video Player implementing the EntertainMedia abstract class.
    
    Attributes:
    - play_button (bool): Indicates whether the video player is in play state.
    """
    def __init__(self, play_button):
        """
        Initializes a VideoPlayer object with the provided play button state.
        
        Parameters:
        - play_button (bool): Indicates whether the video player is in play state.
        """
        self.play_button = play_button
    
    def play_media(self):
        """
        Plays video if the play button is ON.
        """
        if self.play_button:
            self.play_button = True
            print("Video player playing your favorite video")
        else:
            print("Video player is off, please turn it ON")

    def pause_media(self):
        """
        Pauses video if the play button is ON.
        """
        if not self.play_button:
            self.play_button = False
            print("Video player is already in pause state")
        else:
            print("Video player is playing your favorite video. If you want to stop, turn it off")

music = MusicPlayer(True)
video = VideoPlayer(False)
music.play_media()
music.pause_media()
video.play_media()
video.pause_media()


# Composition
class Screen:
    """
    Represents the screen of a phone.
    
    Attributes:
    - size (str): The size of the screen.
    """
    def __init__(self, size):
        """
        Initializes a Screen object with the provided size.
        
        Parameters:
        - size (str): The size of the screen.
        """
        self.size = size
    
    def display(self):
        """
        Displays information about the phone screen.
        """
        print(f"The phone screen is made up of AMOLED and the size is {self.size}")

class Camera:
    """
    Represents the camera of a phone.
    
    Attributes:
    - resolution (str): The resolution of the camera.
    """
    def __init__(self, resolution):
        """
        Initializes a Camera object with the provided resolution.
        
        Parameters:
        - resolution (str): The resolution of the camera.
        """
        self.resolution = resolution
    
    def photo(self):
        """
        Takes a photo with the phone camera.
        """
        print(f"The phone camera has {self.resolution} MP resolution")

class Battery:
    """
    Represents the battery of a phone.
    
    Attributes:
    - capacity (str): The capacity of the battery.
    """
    def __init__(self, capacity):
        """
        Initializes a Battery object with the provided capacity.
        
        Parameters:
        - capacity (str): The capacity of the battery.
        """
        self.capacity = capacity
    
    def battery_info(self):
        """
        Displays information about the phone battery.
        """
        print("The phone battery has a capacity of", self.capacity)

# other example
class UIComponent(ABC):
    """
    Represents a UI component interface.
    """
    @abstractmethod
    def deploy(self):
        """
        Abstract method to deploy the UI component.
        """
        pass

class DraggableMixin:
    """
    Represents a mixin for draggable UI components.
    """
    def drag(self):
        """
        Drags the UI component.
        """
        print("This component is draggable")

class ClickableMixin:
    """
    Represents a mixin for clickable UI components.
    """
    def click(self):
        """
        Clicks the UI component.
        """
        print("This component is clickable")

class Button(UIComponent, DraggableMixin):
    """
    Represents a concrete UI component - Button.
    """
    def deploy(self):
        """
        Deploys the button.
        """
        print("The button component is draggable")

class TextArea(UIComponent, DraggableMixin, ClickableMixin):
    """
    Represents a concrete UI component - TextArea.
    """
    def deploy(self):
        """
        Deploys the text area.
        """
        print("The text area components are both clickable and draggable")

class RadioButton(UIComponent, ClickableMixin):
    """
    Represents a concrete UI component - RadioButton.
    """
    def deploy(self):
        """
        Deploys the radio button.
        """
        print("The radio buttons are only clickable")

# Create instances for composition example
button_instance = Button()
text_area_instance = TextArea()
radio_button_instance = RadioButton()

# Use the composed UI components
button_instance.drag()
button_instance.deploy()

text_area_instance.drag()
text_area_instance.deploy()
text_area_instance.click()

radio_button_instance.click()
radio_button_instance.deploy()

def cold_coffee(func):
    """
    Decorator for adding cost to cold coffee.
    """
    def cost():
        return func() + 5
    return cost

def chocolate_coffee(func):
    """
    Decorator for adding cost to chocolate coffee.
    """
    def cost():
        return func() + 10
    return cost

def capichino(func):
    """
    Decorator for adding cost to capichino.
    """
    def cost():
        return func() + 20
    return cost

@cold_coffee
@capichino
@chocolate_coffee
def simple_coffee():
    """
    Simple function representing the cost of a basic coffee.
    """
    return 5

# Use decorated coffee function
print(simple_coffee())

class Logging:
    """
    Represents a Logging class following the Singleton pattern.
    """
    _instance = None

    def __new__(cls):
        """
        Overrides the __new__ method to implement the Singleton pattern.
        """
        if cls._instance is None:
            cls._instance = super(Logging, cls).__new__(cls)
            cls._instance.log_file = 'apps.log'
        return cls._instance

    def log(self, msg):
        """
        Logs a message to the log file.
        
        Parameters:
        - msg (str): The message to be logged.
        """
        with open(self.log_file, "a") as f:
            f.write(f'{msg}\n')

# Use the Logging singleton instance
logs = Logging()
logs.log('Hi')
logs.log('This is about singleton pattern')

# Create another instance to check if it logs to the same file
logs2 = Logging()
with open(logs2.log_file, "r") as file_content:
    content = file_content.read()

print(content)


