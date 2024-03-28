def assignmentTwo():
  import math

  a = float(input("Enter side A: "))
  b = float(input("Enter side B: "))
  c = float(input("Enter side C: "))
  d = float(input("Enter side D: "))
  e = float(input("Enter side E: "))

  one = 1.0 * a * b
  two = (a - c) * (d - e - b)
  three = 0.5 * (a - c) * e

  print("Room Area: " + str(one + two + three))