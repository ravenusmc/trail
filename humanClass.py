class Human():

  def __init__(self, name, job):
    self.name = name 
    self.job = job 
    self.money = 0
    self.life = 30

  #This method will drain the life from each of the player objects a little bit each day. It's a tough 
  #journey. In order for the life to go back up, the wagon has got to stop. 
  def lifeDrop(self):
    self.life -= 3


    
