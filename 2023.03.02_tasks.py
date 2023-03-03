# ----------- Task 1 --------

# age = int(input("Enter your age: "))
# licence = input("Do you have driver's licence (yes or no: ")
# licence = "yes"
# result = age >= 18 and licence == "yes"                                # why it is not working when age=true but licence=false ==> False?
# print("You are able to drive:"+ str(result))


# ----------- Task 2 --------
# password = input("Enter your password: ")
# result = len(password) >= 8
# print("Password accepted: " + str(result))


# ----------- Task 3 --------
# a=int(input("Enter number: "))
# b=int(input("Enter number once again: "))
# result= a%2==0 and b%2==0
# print("Both numbers are even: " + str(result))
# result = a%2==0 or b%2==0
# print("At least one number ir even: " + str(result))


# ----------- Task 4 --------
# year = int((input("Enter a year: ")))
# result = year%4 == 0 and not year%100==0 or year%400==0
# print("Leap year: " + str(result))


# ----------- Task 5 --------
import datetime as dt
current_date = dt.date.today()
Date = input("Enter yyyy-mm-dd: ")
result= Date==current_date                                        # I assume I have a mistake here
print("Date valid: " + str(result))
