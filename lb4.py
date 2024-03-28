
import random
def passwordGenrtor ():
    listofAnimals = ["cat", "dog", "unicorn", "dragon"] # list of Animal to
    ani=random.choice(listofAnimals) # this line make the compter pick a animal from the list randomy
    beginingNum=random.randint(7,21098487) # this line pick a number between 7 and 21098487
    lastNum=random.randint(1-500) # this line pick a number between 1 and 500
    listofChar=["!","#","@","?"] # this line hold a list of characters
    char=random.choice(listofChar) 
    newPassword=str(beginingNum)+ani+str(lastNum)+char
    #this line put all the List in a password
    print(newPassword)
  #import random
  #def rollingDice():
  #    dice1=random.randint(1,6)
  #    dice2=random.randint(1,6)
  #    twodices=(dice1 , dice2)
  #    print(twodices)

#rollingDice()