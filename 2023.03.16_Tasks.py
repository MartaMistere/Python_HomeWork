#----------TASK 1----------------

#text = input("Enter the text: ")
#letter = input("Enter one letter: ")
#result = text.count(letter)
#print(result)

#----------TASK 1.1----------------

#countOfChars = dict()
#for element in text:
    #countOfChars[element] = 0
#for character in text:
    #countOfChars[character] += 1
#print(countOfChars)

#----------TASK 2----------------  # to get this result I searched in the net 
list=["A","G","V","D","B","C"]
sort_list=[]
while list:
    smallest = min(list)
    sort_list.append(smallest)
    list.pop(list.index(smallest))
print(sort_list)