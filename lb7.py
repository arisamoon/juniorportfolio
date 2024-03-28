def ageLimits():
  age = int(input("Hello! Enter your age please: "))

  if age < 16:
    print("You're too young to drive!")
  elif age >= 16 and age <= 17: 
    print("You are allowed to get a permit and drive under adult supervision!")
  elif age >= 18: 
    print("You can get your licsence and drive on your own!")
  elif age >= 85: 
    print("Take it easy on the road..")
  else: 
   print("please enter a valid age.")

  if age < 18: 
    print("You cannot vote!")
  elif age >= 18:
    print("You can vote!")

  if age < 13:
    print("You can only watch G-rated and PG-rated movies!")
  elif age >= 13 and age <= 15: 
    print("You can watch G and PG rated movies on your own, and PG-13 rated movies with an adult!")
  elif age >=16 and age<= 17:
    print("You can watch G, PG, PG-13, and R-rated movies!")
  elif age >= 18:
    print("You can watch all rated movies!!")