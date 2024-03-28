

portfolio=True
while portfolio==True:
  print("Hello! Welcome To My Portfolio Portal ᓚᘏᗢ")
  print("* > -------------------------------------- < *")
  print("* > -------------------------------------- < *")
  print("   ")
  print("LABS ⑅˚₊")
  print("1. lab one - Emoji Face")
  print("2. lab two - Exact Change")
  print("3. lab three - Play!")
  print("4. lab four - Password Generator")
  print("5. lab five - Input Check")
  print("6. lab six - Leap Year")
  print("7. lab seven - Age Limits")
  print("8. lab eight - Height")
  print("9. lab nine - It's Odd Power")
  print("                    ")
  print("GAMES ⋆⑅˚₊")
  print("- Ping Pong ")
  print("      ")
  print("PROJECT STEM ⋆⑅˚₊")
  print("- Assignment One")
  print("- Assignment Two")
  print("- Assignment Three")
  print("- Assignment Four")
  print("     ")
  x=(input("What lab number would you like to view? (1/2/3/4/5/6/7/8/9/pingpong/one/two/three/four) !Please keep capitilization, spelling, and spacing in mind while responding, thank you /ᐠ. .ᐟ\ฅ:"))

#IF STATEMENTS
  if x =="2":
    exactChange()
  elif x =="1":
    print("      ")
    print("This task got lost in another demension, it's currently unavaiable!")
    print("     ")
  elif x == "3":
    print("      ")
    print("This task got lost in another demension, it's currently unavaiable!")
    print("     ")
  elif x =="4":
    passwordGenrtor()
  elif x =="5":
    inputCheck()


  y =(input("Do you want to see another?! ฅ^._.^ฅ "))
  if y != "yes":
    portfolio= False
    print("Thats alright, have a good day ᓚᘏᗢ")
