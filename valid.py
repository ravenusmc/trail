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
  if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
    return True
  else: 
    return False 

def oxenValid(yokeNumber):
  if yokeNumber < 0 or yokeNumber > 10:
    return False
  else:
    return True

  