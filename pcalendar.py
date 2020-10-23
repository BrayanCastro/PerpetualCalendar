# Author: Brayan Castro Lugo
# Class: COMP 141
# Program 3: Perpetual Calendar
# Pledge: I have neither given nor received unauthorized aid on this program. 
# Description: In this program I have designed a perpetual calendar by writing a number of functions that will work together to Compute and print the day of the year for this month/day/year , Compute and print the day of the week for this month/day/year, Compute and print the day of the week for user's month and day, but for the year 2020, and Compute and print the day of the week for New Year's Day on the user's year..


#This function takes a parameter called year, which will be an integer. Then this function will return True if the year is a leap year, and False if it is not.
def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False
           
      
      
#This function takes a parameter called month to return the number of days that have gone by in a year on the first of any month (assuming it's not a leap year).
def magic_month(month):
  if month == 1:
    month = 0
    return (month)
  elif month == 2:
    month = 31
    return (month)
  elif month == 3:
    month = 59
    return (month)
  elif month == 4:
    month = 90
    return (month)
  elif month == 5:
    month = 120
    return (month)
  elif month == 6:
    month = 151
    return (month)
  elif month == 7:
    month = 181
    return (month)
  elif month == 8:
    month = 212
    return (month)
  elif month == 9:
    month = 243
    return (month)
  elif month == 10:
    month = 273
    return (month)
  elif month == 11:
    month = 304
    return (month)
  elif month == 12:
    month = 334
    return (month)
  else:
    return ("Please enter a valid month")
  
  
  
#This function is called day_of_year and takes three integer parameters: a month (1-12), a day (1-31), and a year (any year is possible). This function then returns the day of year (1-366) that the given date occurs on.
def day_of_year(month, day, year):
  if is_leap(year) == False:
     return magic_month(month) + day
  elif is_leap(year) == True:
    if month >=3:
      return (magic_month(month) + day )+1
    elif month <=3:
      return magic_month(month) + day
    
    

#This function will calculate the day of the week number (from the table below) for any January 1 in history. It is called new_years_day, and takes an integer parameter called year, and returns an integer interpreted as a day of the week.
def new_years_day(year):
  Sunday = 0
  Monday =1
  Tuesday = 2
  Wednesday = 3
  Thursday = 4
  Friday = 5
  Saturday = 6
  
  if is_leap(year) == False:
    return (((year+(year//4)) - (year//100))+(year//400))%7
  elif is_leap(year) == True:
    return ((((year+(year//4)) - (year//100))+(year//400))-1)%7
    
  
  
#This function takes three parameters: the month (1-12), the day of the month (1-31), and the year. This function will then compute the day of the week for any day of any year by returning this as an integer value.   
def day_of_week(month, day, year):
  return (((day_of_year(month, day, year)) + (new_years_day(year)))-1)%7
  
  
  
#This function is called day_of_week_str, and does the same operation as day_of_week, except the answer is returned as a string. It takes three parameters: the month (1-12), the day of the month (1-31), and the year. 
def day_of_week_str(month, day, year):
  dayz = day_of_week(month, day, year)
  if dayz == 0:
    dayz = "Sunday"
    return (dayz)
  elif dayz == 1:
    dayz = "Monday"
    return (dayz)
  elif dayz == 2:
    dayz = "Tuesday"
    return (dayz)
  elif dayz == 3:
    dayz = "Wednesday"
    return (dayz)
  elif dayz == 4:
    dayz = "Thursday"
    return (dayz)
  elif dayz == 5:
    dayz = "Friday"
    return (dayz)
  elif dayz == 6:
    dayz = "Saturday"
    return (dayz)
 
 
  
#This is the main function which asks the user for three integers and prints varios statements also asking the user if he wants to loop the function. 
def main():
  print("Pick a date, any date (such as your birthday!) ")
  month = int(input("What is the month?(1-12) "))
  day = int(input("What is the day of the month? "))
  year= int(input("What is the year? "))
  print("This is day number", day_of_year(month, day, year) ,"of the year.")
  print("This date falls on a", day_of_week_str(month, day, year) + "." )
  print("In", 2020 ,",this date falls on a", day_of_week_str(month, day, 2020) + ".")
  print("In", year ,"New Year's Day falls on a", day_of_week_str(1, 1, year) + ".")
  
  keep_going = 'yes'
  while keep_going != 'no':
    keep_going = input("Would you like to pick another date? (yes or no)") 
    print("")
    if keep_going == "yes":
      return main()
    else:
      print("Thank You")
  
main() 
  