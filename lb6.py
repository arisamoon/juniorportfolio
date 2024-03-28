def leapYear():
  year = int(input("Enter a year: "))
  #leap year is a year that has an extra day in feburary.
  #If you were born on feburary 29th , then you can only celebrate your birthday every four years on that date 
  #every year feburary ends on the 28th 
  #every four years we have a leap year that makes feburary longer by a day 
  if(year<=1752): #start of the gregorian calendar 
    print("Leap years didn't exist back then!")
  #every four years make it leap is the julian calender 
  #if the year is multiple of 100 it is not a leap year 
  #if the year is multiple of 400 it is a leap year

  #if the year is more of 10000 or multiple of 10000+28000 it is not a leap year 
  elif year > 10000 and (year - 2800)%10000 == 0 and (year%100)==0:
    print(year, " is NOT a leap year")
  #if the year ends in 2800, 5600, 0r 8400 that is NOT a leap year
  #tropical year is 365 days, 5 hours, 48 minutes, 45 seconds, and 138 milliseconds 
  elif year < 10000 and (year-2800)%10000 == 0 :
    print(year, " is NOT a leap year")
  elif year < 10000 and (year-5600)%10000 == 0:
    print(year, " is NOT  a leap year")
  elif year < 10000 and (year-8400)%10000 == 0:
    print(year, " is NOT a leap year")
  else: #to tell what is a leap year
    if year % 400 == 0:
      print(year, " is a leap year!")
    elif year%100!=0 and year%4==0:
      print(year, " is a leap year!")
    else: 
      print(year, "is NOT a leap year")