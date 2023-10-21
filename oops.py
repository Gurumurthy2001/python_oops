'''Create a Class: Define a simple class,
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
