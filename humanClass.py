class Human():

  def __init__(self, name):
    self.name = name 

class Banker(Human):

  def __init__(self, name):
    self.name = name
    self.money = 2000

class Carpenter(Human):

  def __init__(self, name):
    self.name = name
    self.money = 1500

class Farmer(Human):

  def __init__(self, name):
    self.name = name
    self.money = 1000