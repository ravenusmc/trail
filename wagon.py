#This is where the wagon class will be. 
class Wagon():

  def __init__(self):
    self.oxen = 0
    self.food = 0
    self.cloth = 0
    self.wheel = 0
    self.axle = 0
    self.tongue = 0
    self.speed = 0

  #I may need to think about placing the human objects into here?
  def move(self):
    self.speed = 1
    self.speed = 2.5 * self.oxen
    print(self.speed)
  
wagon = Wagon()
wagon.move()

#Trail was 2000 miles long
#covered about 15 miles per day 
#Took 4-6 months to make the journey. 
#10 oxen is the max I allow someone to buy 
# 2 is per yoke. 20 Miles per day is max speed with 10 oxen. 8 oxen miles per day is 16
# 10 oxen is 25 MPH , 8 oxen is 20 mph, number of oxen * 2.5 is speed. 

