#NOTE: I'am not following the NAMING RULES OF Class
# I provide the Naming rules inthe Readme file follw that for better practice


#  *********** Create a Class: ***********
'''Define a simple class,
 like a Car, with attributes such as make, model,
 and methods like start and stop.
Instance Creation:
 Instantiate objects of the Car class with different
 attributes.'''

class car:
	
	def __init__(self,make,model):
		self.make=make
		self.model=model
		self.car_running=False
		
	def start(self):
		if not self.car_running:
			self.car_running=True
			print(f"{self.make} {self.model}is started".format())
		else:
			print("The car is already running.")
				
	def stop(self):
		if self.car_running:
			self.car_running=False
			print(f"{self.make}"+" "+"{self.model}is started".format())
		else:
			print("The car is already stopped.")
			
car1=car('toyota','lexus')
car2=car('tata','thor')
car1.start()
car2.stop()


#    ********  Encapsulation:***********
''' Implement encapsulation by making attributes private
 (e.g., _make) and using getter and setter methods to 
access and modify them.'''


class car:
	#setting the class constructor
	def __init__(self,make,model):
		self._make=make
		self._model=model
		self._car_running=False
	# setting the getter methods (here we use private access modifier)
	def get_make(self):
		return self._make
		
	def get_model(self):
		return self._model
		
	def car_running(self):
		return self._car_running
		
    #setting the setter metthods
	def start(self):
		if not self._car_running:
			self._car_running=True
			print(f"{self._make} {self._model}is started".format())
		else:
			print("The car is already running.")
				
	def stop(self):
		if self._car_running:
			self._car_running=False
			print(f"{self._make}{self._model}is started".format())
		else:
			print("The car is already stopped.")
			
car1=car('toyota','lexus')
car2=car('tata','thor')
car1.start()
car2.stop()
print(car1.get_make())

print(car2.get_make())

'''In Python,
 even though an attribute is designated as private with 
a single underscore (e.g., _make), it is still technically
 accessible outside the class.
 However, it is considered a best practice to use getter 
and setter methods to access and modify such attributes 
rather than directly accessing them, 
to maintain encapsulation.

So, while you can access _make with car1._make,
 it's recommended to use car1.get_make() to access the
 attribute for better encapsulation and to follow 
good coding practices.'''

#here is an another example of car class that demonstrate you about getter and setter methods  and using those methods we can acces and modify the attributes


class car:
	#class constructor
	def __init__(self,make,model):
		self._make=make
		self._model=model
		
	#getter methode
	def get_make(self):
		return self._make
		
	def get_model(self):
		return self._model
		
	#setter methode to modify
	def set_make(self,new_make):
		self._make=new_make
		return new_make
		
	#instatiation
car3=car('benz','recent')
	
	# Access _make using the getter
print(car3.get_make())

#modifying using setter method
new_make=car3.set_make('lamborgini')
print(f'{new_make}')
	




#  ******* Inheritance: *******

''' Create a subclass of the Car class,
 e.g., ElectricCar, inheriting attributes and methods,
 and add specific characteristics for electric cars.'''

'''The provided code defines a Python class called "car"
 which serves as the parent class for other car-related
 classes.
The "car" class has a constructor (__init__) that takes
 two parameters: 'make' and 'model', and it initializes
 the instance variables '_make' and '_model'.
The class also has getter methods, get_make and get_model, to access the 'make' and 'model' attributes, respectively.
There's a setter method, set_make_model, to change the 'make' and 'model' attributes.The class contains methods for starting and stopping the car. It uses the '_is_running' attribute to track the car's running state.
An "electric_car" class is defined as a child class of "car," inheriting its properties and methods.
The child class "electric_car" has its constructor, which also takes 'make' and 'model' parameters, and an additional 'battery_state' parameter.The child class has a method 'charge' to check and print the battery charge status. It uses the '__battery_state' attribute to do so.
An object 'electric_car1' is created from the child class 'electric_car' with the make 'tesla,' model 'model-1,' and a battery state of 21.
The code demonstrates the use of various methods, including starting and stopping the electric car, checking the battery charge, and modifying the 'make' and 'model' attributes using getter and setter methods.
'''

#creating a car class
class car:
	#constructor for car class
	def __init__(self,make,model):
		self._make=make
		self._model=model
		self._is_running=False
	
	#getter methode for 'make''
	def get_make(self):
		return self._make
	
	#getter methode for 'model'
	def get_model(self):
		return self._model
	
		#setter methode for 'make and model' 	
	def set_make_model(self,new_make,new_model):
		self._make=new_make
		self._model=new_model
		
	def start(self):
		if not self._is_running:
			self._is_running=True
			print(f"{self._make} {self._model} is started")
			
		else:
			print(f"{self._make} {self._model} is already running")
			
	def stop(self):
		if self._is_running:
			self._is_running=False
			print(f"{self._make} {self._model} is stoppd")
			
		else:
			print(f"{self._make} {self._model} is already stopped")

#inherited class from parent class(car-->parent, and electric_car-->child)
class electric_car(car):
		#constructor for child class
		def __init__(self,make,model,battary_state):
			
			#super() methode to inherit the properties from the parent
			super().__init__(make,model)
			self._battary_state=battary_state
			
		def charge(self):
			if self._battary_state >20:
				print(f"{self._make} {self._model}\'s charge is {self._battary_state}")
				
			else:
				print("please plug in charge")
				
#creating the object for child class(electric_car)				
electric_car1=electric_car('tesla','model-1',21)

#accessing the parental properties				
electric_car1.stop()
electric_car1.start()

#accessing the child methode
electric_car1.charge()

#getter method usage using child class
print(electric_car1.get_make())
print(electric_car1.get_model())

#setter methode useage using childe class

electric_car1.set_make_model('telsa-1','model-2')
print(electric_car1.get_make())
print(electric_car1.get_model())




#  ****** Polymorphism:  ********
''' Implement a method in both the Car and ElectricCar classes, e.g., drive, with different behaviors.
 Demonstrate polymorphism by calling the same method on objects of both classes.
When we call the drive method on objects of both classes, we demonstrate polymorphism,
 as the same method name is used on different classes, 
and it exhibits different behaviors based on the object's actual class.
'''

#creating a car class
class car:
	#constructor for car class
	def __init__(self,make,model):
		self._make=make
		self._model=model
		self._is_running=False
	
	#getter methode for 'make''
	def get_make(self):
		return self._make
	
	#getter methode for 'model'
	def get_model(self):
		return self._model
	
		#setter methode for 'make and model' 	
	def set_make_model(self,new_make,new_model):
		self._make=new_make
		self._model=new_model
		
	def start(self):
		if not self._is_running:
			self._is_running=True
			print(f"{self._make} {self._model} is started")
			
		else:
			print(f"{self._make} {self._model} is already running")
			
	def stop(self):
		if self._is_running:
			self._is_running=False
			print(f"{self._make} {self._model} is stoppd")
			
		else:
			print(f"{self._make} {self._model} is already stopped")
			
	def drive(self):
		print(f"{self._make} {self._model} causes sound and wind pollution during the Drive")

#inherited class from parent class(car-->parent, and electric_car-->child)
class electric_car(car):
		#constructor for child class
		def __init__(self,make,model,battary_state):
			
			#super() methode to inherit the properties from the parent
			super().__init__(make,model)
			self._battary_state=battary_state
			
		def charge(self):
			if self._battary_state >20:
				print(f"{self._make} {self._model}\'s charge is {self._battary_state}")
				
			else:
				print("please plug in charge")
				
		def drive(self):
			print(f"{self._make} {self._model} with a battary limit {self._battary_state} dont causes sound and wind pollution during the Drive")
				
#creating the object for child class(electric_car)	
car1=car('tata','model-5')		
electric_car1=electric_car('tesla','model-1',21)

#accessing the parental properties				
electric_car1.stop()
electric_car1.start()

#accessing the child methode
electric_car1.charge()

#getter method usage using child class
print(electric_car1.get_make())
print(electric_car1.get_model())

#setter methode useage using childe class

electric_car1.set_make_model('telsa-1','model-2')
print(electric_car1.get_make())
print(electric_car1.get_model())

#polymorphism
car1.drive()
electric_car1.drive()




#   *********   Abstraction   ***********

'''Abstraction in programming hides the complex implementation details of a class or object and provides a simplified interface for the user to interact with. 
It allows you to focus on what an object does rather than how it does it. 
Abstraction is often achieved through abstract classes and interfaces, as demonstrated in the following example.
Let's consider a simple example using a multimedia player as a real-world analogy
'''

# importing "abstract base class" and abstractmethod
from abc import ABC,abstractmethod

#creating class with base class ABC
class entertain_media(ABC):
	#creating abstract method which will must be implement in child class
	@abstractmethod
	def play_media(self):
		pass
		
	@abstractmethod
	def pause_media(self):
		pass
		
#class for music player
class music_play(entertain_media):
	def __init__(self,play_button):
		self.play_button=play_button
	
	#method for playing media	
	def play_media(self):
		if self.play_button:
			print("music player playing your favrate music")
		else:
			print("music player is off please turn it ON")

	#method for pausing media		
	def pause_media(self):
		if not self.play_button:
			print("music player is already in pause state")
		else:
			print("music player is playing your favrate song if you want to stop then you turn it off")
			
#similarly for the vidio player

class vedio_play(entertain_media):
	def __init__(self,play_button):
		self.play_button=play_button
		
	def play_media(self):
		if self.play_button:
			self.play_button=True
			print("vedio player playing your favrate vedio")
		else:
			print("vedio player is off please turn it ON")
			
	def pause_media(self):
		if not self.play_button:
			self.play_button=False
			print("vedio player is already in pause state")
		else:
			print("vedio player is playing your favrate vedio song if you want to stop then you turn it off")
			

#object creation		
music=music_play(True)
vedio=vedio_play(False)

#method calling
music.play_media()
music.pause_media()

vedio.play_media()
vedio.pause_media()
			
'''This Python code defines an abstract class entertain_media with two abstract methods play_media and pause_media. It represents a media player interface. It also includes two concrete subclasses, music_play and video_play, which implement the media player functionality.music_play and video_play have a play_button parameter to determine if the player is turned on.
They implement the abstract methods play_media and pause_media, providing different messages based on the state of the play button.
Two instances, music and video, are created and their play_media and pause_media, providing different messages based on the state of the play button.
Two instances, music and video, are created and their play_media and pause_media methods are called, simulating the behavior of a music player and a video player.'''





#  ********* Multiple Inheritance  ***********

''' Multiple Inheritance is simply means that
 a single child class can inherits the properties of multiple parent classes.
 Here is an easy and effective example which gives the concept of Multiple inheritance'''


#parent class ----1
class car:
	#constructor
	def __init__(self,make,model):
		self.make=make
		self.model=model
	
	#methods	
	def start(self):
		print(f"{self.make} {self.model} is started")
	
	def stop(self):
		print(f"{self.make} {self.model} is stopped")
	
#parent class -----2
class helicopter_car:
	#constructor
	def __init__(self,builder,model_type):
		self.builder=builder
		self.model=model_type
	
	#methods	
	def taking_off(self):
		print(f"{self.builder} {self.model_type} taking-off")
		
	def landing(self):
		print(f"{self.builder} {self.model_type} landing-off")
	
	
#child class which inherits the properties from 2 parent class
class flying_car(car,helicopter_car):
	#constructor for child class
	def __init__(self,car_make,car_model,helicopter_builder,helicopter_model_type):
		#inheriting the parent---1
		car.__init__(self,car_make,car_model)
		
		#inheriting the parent---2
		helicopter_car.__init__(self,helicopter_builder,helicopter_model_type)
	
	#child class method	
	def fly(self):
		print(f"The flying car is the combination of {self.make} {self.model} and {self.builder} {self.model_type} is  succusessfully flying now")
	
#creating the object of child class
fly_car=flying_car('tata','model-A','tata_airlines inc.','fly_india-A')

#accessing the methods of diffrent parent class using the child class object
fly_car.start()
fly_car.taking_off()
fly_car.fly()
fly_car.landing()
fly_car.stop()






#         ********* Composition **********


'''In object-oriented programming, composition is a basic idea where a class is built by assembling other classes as components. 
In the example given, composition is exemplified by building a class called Smartphone that combines the Screen, Battery, and Camera classes to create a more complicated object.

The code consists of four classes representing different components of a smartphone: screen, camera, battary, and smartphone. Each class has a constructor method to initialize specific attributes, such as screen size, camera resolution, and battery capacity. The smartphone class employs composition by creating instances of the screen, camera, and battary classes as its attributes. These attributes correspond to the smartphone's components.

The smartphone class features various methods for interacting with the smartphone. The make_call method allows the smartphone to make calls and displays the phone's name. The pic_info method provides information about the camera by calling the photo method within the camera class. Similarly, the charge_info method displays battery capacity through the battary_info method in the battary class. The screen_info method presents details about the phone's screen using the display method in the screen class.

An instance of the smartphone class is created with the name "realme," a 14-inch screen, a 52MP camera, and a 4000mAh battery. The code demonstrates how to access and utilize the smartphone's features by calling its methods. This showcases the concept of composition as the smartphone class encapsulates its various components, allowing for a structured representation of a smartphone's functionality and characteristics.'''


class screen:
	def __init__(self,size):
	    self.size=size
	    
	def display(self):
	    print(f"The phone screen is made up of AMOLED and the size is {self.size}")
	    
	
class camera:
	def __init__(self, resolution):
	    self.resolution=resolution
	    
	def photo(self):
	    print(f"The phone camera has {self.resolution} MP  resolution")
	
class battary:
	def __init__(self,capacity):
	    self.capacity = capacity
	   
	def battary_info(self):
	    print(f"The phone maximum charge capacity is {self.capacity}")
	
class smartphone:
	def __init__(self,name,screen_size, photo_quality, battary_status):
	    self.name=name
	    self.screens=screen(screen_size)
	    self.photos=camera(photo_quality)
	    self.battaries=battary(battary_status)
	    
	def make_call(self):
	    print(f"using the {self.name} phone we can make a call")
	    
	def pic_info(self):
	    self.photos.photo()
	
	def charge_info(self):
	    self.battaries.battary_info()
	    
	def screen_info(self):
	    self.screens.display()
	    
phone=smartphone("realme","14-inch",52,"4000mh")
phone.make_call()
phone.pic_info()
phone.charge_info()
phone.screen_info()
