#Validations for the main file. 
def mainValid(choice):
  if choice == 1 or choice == 2 or choice == 3:
    return True
  else:
    return False 

def characterValid(choice):
  if choice == 1 or choice == 2 or choice == 3 or choice == 4:
    return True 
  else: 
    return False

def monthValid(choice):
  if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
    return True 
  else: 
    return False 

## Validations for the store file. 
def storemainValid(choice):
  if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6:
    return True
  else: 
    return False 

def oxenValid(yokeNumber):
  if yokeNumber < 0 or yokeNumber > 5:
    return False
  else:
    return True

def foodValid(foodNumber):
  if foodNumber < 0:
    return False
  else:
    return True

def clothValid(clothNumber):
  if clothNumber < 0:
    return False
  else: 
    return True 

def wheelValid(wheel):
  if wheel < 0:
    return False 
  else: 
    return True 

def axleValid(axle):
  if axle < 0:
    return False
  else: 
    return True

def tongueValid(tongue):
  if tongue < 0:
    return False
  else: 
    return True

def bulletValid(bulletNumber):
  if bulletNumber < 0:
    return False
  else:
    return True 

## Validations for the trail file.

def travellingTrailValid(choice):
  if choice == 1 or choice == 2 or choice == 3:
    return True
  else: 
    return False 

def trailMenuValid(choice):
  if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6:
    return True
  else:
    return False 

def increaseValid(speedUp, wagon):
  if (speedUp * 5) + wagon.speed > wagon.speed:
    return False
  else: 
    return True

def decreaseValid(speedDown, wagon):
  if wagon.speed - (speedDown * 5) < 0:
    return False
  else: 
    return True

def changeFoodValid(choice):
  if choice == 1 or choice == 2 or choice == 3:
    return True
  else: 
    return False

def riverAheadValid(option):
  if option == 1 or option == 2:
    return True 
  else:
    return False

## Validations for the merchant class. 

def merchantClassValid(choice):
  if choice == 1 or choice == 2 or choice == 3:
    return True 
  else: 
    return False 

def merchantPriceValid(amount):
  if amount < 0:
    return False
  else:
    return True 
































  