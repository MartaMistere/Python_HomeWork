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

# ----------- Task 3 --------

#number=int(input("Enter number: "))
#factors=1
#for i in range (1,number+1):
    #factors *=i
#print("This is factors of your nubmer: ", factors)

# ----------- Task 4 --------

a=int(input("Enter first number: "))
b=int(Input("Enter second number: "))
c=input("Enter one of these operation (*,/,+,- or %): ")
    if c=="*":
        print(a*b)

    elif c=="/":
        print(a/b)

    elif c=="+":
        print(a+b)

    elif c== "-":
        print(a-b)

    elif c=="%":
        print(a%b)

    else: print("Operation provided isn't valid, please try again: ", c)

