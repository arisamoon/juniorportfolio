def assignmentThree():

  name= input("Hi! What is your full name? ")
  food= input("What is your favorite food? ")
  store= input("What is your favorite store? ")
  sport= input("What is your favorite sport (Ex: basketball, soccer, baseball, etc. ")
  top= input("Any favorite type of toppings on pizza ")
  additional= input("Anything else you want to say? ")
  import random
  age= (input("What's your favorite number? "))
  print("My favorite number is "+ str(random.randint(1,100)))

  if not name =="ok":
      print("Hi,", name)

  if food =="pizza":
      print("so yummy")

  elif food== "burgers":
      print("That's delicious")

  else: print("Nice one!")

  if store == "Forever 21":
      print("Me too!")

  elif store == "H&M":
      print("I love their clothing!")

  elif store == "Garage":
      print("Their tops are so cute")

  else:
      print("Amazing")

  if sport =="soccer":
      print("My favorite sport.")
  elif sport== "basketball":
      print("You are very tall")

  else:
      print("Very athletic")