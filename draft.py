def testOne():
  name = "Mike"
  testTwo(name)

def testTwo(name):
  num = 3
  lastname = "Cuddy"
  testThree(name, lastname)
  testFour(name, lastname, num)

def testThree(name, lastname):
  print(name)
  print(lastname)
  testFour(name, lastname)

def testFour(name, lastname, num):
  print(num)
  print(name)
  print(lastname)

testOne()