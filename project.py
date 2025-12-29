# # assignment 1

# # create a list  of color 
# color = ["red","green","blue"]

# #access  the second element  of list 
# second_element= color[1]
# print(second_element)

# #update the first element to "yellow"
# color[0]= "yellow"
# print(color)

# #slice the list  to get  the  last two elements
# last_two= color[1:]
# print(last_two)

# # get the lenght of the list 
# print(len(color))

# assignment2
# flatten the tuple
data = ((2, 3), (4, 3), (1, 5))
# flat = sum(data, ())
# print(flat)
i=()
t=()
result= tuple( i for t in data for i in t)
print(result)

# remove the duplicate
numbers=(1,2,2,3,3,4,4,4,5)
remove=set(numbers)
print(remove)
