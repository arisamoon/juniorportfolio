def inputCheck(): 
input_1 = (input("Enter a 4-digit whole number: "))
if len(input_1)==4 and (input_1).isdecimal() and input_1[0]!= "0": 
    print("Thanks!")
else:
    print("That is not a 4-digit whole number :<")
input_2 = int(input("Enter an integer less than 50: ")) 

if input_2 < 50:
    print("Thanks!")
else: 
    print("That is not an integer less than 50:<")

input_3 = input("Enter a string that begins with a vowel: ")
if input_3.startswitch('a') and input_3.startswitch ('i') and input_3.startswitch ('e') and input_3.startswitch ('o') and input_3.startswitch('u'):
    print("Thanks!")
else:
    print("That doesn't start with a vowel :<")
ninput_4 = input("Enter a string that ends with a consonant: ")
