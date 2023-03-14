# ----------- Task 1 --------

#number = int(input("Enter number: "))
#if number > 0:
    #print("positive")
#elif number < 0:
    #print("negative")
#elif number==0:
    #print("zero")

# ----------- Task 2 --------

#for i in range(1, 101):
    #if i%3==0 and not i%5==0:
        #print("Fizz")
    #elif i%5==0 and not i%3==0:
        #print("Buzz")
    #elif i%3==0 and i%5==0:
        #print("FizzBuzz")
#else: print(i)

#-----------second version of TASK2-----------
#for i in range(1, 101):
#printnumber = True
#if i%3==0:
        #print("Fizz",end="")
        #printnumber = False
    #elif i%5==0:
        #print("Buzz", end=""")
        #printnumber = False
#if printnumber:
    #print(i)
#else:  #go to the next line
    #print()

# ----------- Task 3 --------

#number=int(input("Enter number: "))
#factors=1
#for i in range (1,number+1):
    #factors *=i
#print("This is factors of your nubmer: ", factors)

#-----------second version of TASK3-----------
#number=int(input("Enter number: "))
#for i in range (1,number):
#    if(number % 1 ==0)
# print(number)

#-----------3ed version of TASK3-----------
#number=int(input("Enter number: "))
#if number < 0:
#.....

# ----------- Task 4 --------

#a=int(input("Enter first number: "))
#b=int(Input("Enter second number: "))
#c=input("Enter one of these operation (*,/,+,- or %): ")
    #if c=="*":
     #   print(a*b)
    #elif c=="/":
     #   print(a/b)
    #elif c=="+":
     #   print(a+b)
    #elif c== "-":
     #   print(a-b)
    #elif c=="%":
     #   print(a%b)
    #else: print("Operation provided isn't valid, please try again: ", c)

# ---- second version / corect -----

#number1=float(input("Enter first number: "))
#number2=float(Input("Enter second number: "))

#while True:
    #operation = input("Enter one of these operation (*,/,+,- or %): "
    #if operation == "*":
        #result = number1 * number2
     #elif operation=="/":
        #result = number1 / number2
    #elif operation=="+":
        #result = number1 + number2
    #elif operation=="-":
        #result = number1 - number2
    #elif operation=="%":
        #result = number1 % number2
    #else:
        #print("Operation is not correct: ")
        #continue   # go to the next iteration
    #print("Result is " + str(result))
    #break       # go out of the loop


# ----------- Task 5 -------- (similar to task 3)
#number = int(input("Enter the number\n"))

#prime = True

#for i in range(2,number):     # 1 is not prime from math defin
    #if(number % i == 0):
        #prime = False

#if number > 1 and prime:
    #print("Number is prime")
#else:
    #print("Number is not prime")°

# ---- TASK 5 add task print all the number upto-----

numberUp = int(input("Enter the number\n"))

for number in range(2,numberUp + 1):
    prime = True

    for i in range(2,number):
        if(number % i == 0):
            prime = False

    if number > 1 and prime:
        print(number)