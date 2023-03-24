#---------------TASK 1 ---------------------------
# Write a function that takes two parameters (a and b) and returns their sum.

# a=int(input("Enter the parameter one: "))
# b=int(input("Enter the parameter two: "))
# print(a + b)


#---------------TASK 2 ---------------------------
# Write a function that takes a string as a parameter and returns the number of vowels (aeiou) in the string. Hint: you can use given_character in "aeiou"

#def vowel_count(str):
    #count=0
    #vowel=set("aeiou")
    #for letter in str:
        #if letter in vowel:
            #count=count+1
    #print("Number of vewels: ", count)

#str = input("Write a sentence: ")
#vowel_count(str)

# Arturs question - while I didn't replace last two rowes at the end this didn't work, why? 
#I start with str = input("Write a sentence: ") and then only def vowel_count(str): => is this was the reason that programm didn't work?


#---------------TASK 3 ---------------------------
# Write a function that takes a string as a parameter and returns True if the string is a palindrome and False otherwise

#def isPalindrome(text):
    #return text == text[::-1]
#text = input("Write a word: ")
#ans = isPalindrome(text)
#if ans:
    #print("True")
#else:
    #print("False")


#---------------TASK 4 ---------------------------
# Write a function that takes a list of integers as a parameter and returns a list of only the even integers in the original list

#my_list = [1,0,2,-3,9,3,8,-5,4,7,4,6,5]
#def even_numbers(list):
    #even_list = []
    #for number in list:
        #if number % 2 ==0:
            #even_list.append(list[number])
    #return even_list
#print(even_numbers(my_list))


#---------------TASK 5 ---------------------------
# Write a function that takes a list of integers and a target sum as parameters and returns a list of two integers from the original list that add up to the target sum.

#my_list = [1,0,2,-3,9,3,8,-5,4,7,4,6,5]
#target_sum = 15
#def targeting_sum(list, target):
    #count = 0
    #for my_list in list:
        #count += 1
        #for i in range(count,len(list)):
            #if my_list + list[i] == target:
                #return [my_list,list[i]]
            #else:
                #continue

#print(targeting_sum(my_list,target_sum))


#---------------TASK 6 ---------------------------
# Write a function that takes a list of integers as a parameter and returns the product of all the integers in the list

#my_list = [1,0,2,-3,9,3,8,-5,4,7,4,6,5]
#def product(list):
    #product = 1
    #for i in list:
        #product = product*i
    #return product

#print(product(my_list))

#---------------TASK 8 ---------------------------
# Write a function that takes a dictionary as a parameter and returns a list of all the keys in the dictionary that have an even value

#def even_value(dict):
    #even_dict = []
    #for key in dict:
        #if dict[key] % 2 ==0:
            #even_dict.append(dict[key])
    #return even_dict

#my_dict = {"apple" : 1, "banana" : 2, "orange" : 3}
#print(even_value(my_dict))


#---------------TASK 9 ---------------------------
# Write a function that takes a list of dictionaries as a parameter and returns a new dictionary that contains the sum of the values for each key in the original dictionarie

#my_dict = [{"apple" : 1, "banana" : 2, "orange" : 3}, 
           #{"apple" : 3, "banana" : 1, "orange" : 2},]
#Sum_dict={}
#for i in my_dict:
    #for j in i.keys():
        #Sum_dict[j]=Sum_dict.get(j,0)+i[j]
#print(Sum_dict)


#---------------TASK 10 ---------------------------
# Write a function that takes a tuple as a parameter and returns a new tuple that has the first and last elements swapped

#my_tuple = ("apple", "banana", "orange") 
#print(my_tuple)
#list_my_tuple=list(my_tuple)
#list_my_tuple[0], list_my_tuple[2]=list_my_tuple[2], list_my_tuple[0]
#new_tuple=tuple(list_my_tuple)
#print(new_tuple)

#---------------TASK 11 ---------------------------
# Write a function that takes a set as a parameter and returns a new set that contains only the elements that are not divisible by 3

my_set = {1,0,2,-3,9,3,8,-5,4,7,4,6,5}

def not_divisible_3(sets):
    new_set = set()
    for i in sets:
        if i % 3 != 0:
            new_set.add(i)
    return new_set

print(not_divisible_3(my_set))
