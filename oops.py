'''*********** Create a Class: ***********
Define a simple class,
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


'''********  Encapsulation:***********
 Implement encapsulation by making attributes private
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
	




'''  ******* Inheritance: *******

 Create a subclass of the Car class,
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

