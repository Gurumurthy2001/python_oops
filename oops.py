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
	
