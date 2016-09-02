from wagon import *

class Human():

  def __init__(self, name, job):
    self.name = name 
    self.job = job 
    self.money = 0
    self.life = 30

  #This method will drain the life from each of the player objects a little bit each day. It's a tough 
  #journey. In order for the life to go back up, the wagon has got to stop. 
  def lifeDrop(self, wagon):
    print(wagon.ration)
    if wagon.ration == "Meager":
      self.life -= 5
    elif wagon.ration == "Normal":
      self.life -= 4
    elif wagon.ration == "Tons":
      self.life -= 3

leader = Human("Mike", "Banker")
print(leader.life)
leader.lifeDrop(wagon)
print(leader.life)
leader.lifeDrop(wagon)
print(leader.life)

    
