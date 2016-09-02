
#This is where the wagon class will be. 
class Wagon():

  def __init__(self, ration):
    self.oxen = 0
    self.food = 100
    self.ration = ration
    self.cloth = 0
    self.wheel = 0
    self.axle = 0
    self.tongue = 0
    self.speed = 0
    self.distance = 2000

  #This method will keep track of the speed and subtract that number from the distance each day. 
  def move(self):
    self.speed = 2.5 * self.oxen
    self.distance -= self.speed 
    if self.distance == 0:
        print("You have reached Oregon!")

  #This will affect the amount of food eating by the ration level. I decided to place this method here 
  #and not in the human class becuase one cannot change the individual ration levels-as of now. Thus, 
  #since ration and food are properties of wagon I figured it would be easier to keep them here. 
  def eat(self):
    if self.ration == "Meager":
      self.food -= .25
    elif self.ration == "Normal":
      self.food -= .5
    elif self.ration == "Tons":
      self.food -= 1

  
# wagon = Wagon("Meager")
# wagon.eat()
# print(wagon.food)
# wagon.eat()
# print(wagon.food)
# wagon.eat()
# print(wagon.food)

#Trail was 2000 miles long
#covered about 15 miles per day 
#Took 4-6 months to make the journey. 
#10 oxen is the max I allow someone to buy 
# 2 is per yoke. 20 Miles per day is max speed with 10 oxen. 8 oxen miles per day is 16
# 10 oxen is 25 MPH , 8 oxen is 20 mph, number of oxen * 2.5 is speed. 

# Need to have method that decreases food supplies based on what the ration level is set at. 
# Need a method that decreases distance based on the speed. 

