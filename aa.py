    #DAY = 2

# name1=" sudip "
# print(name1)

# name2= "shrestha"
# print(name2)

# #built  in methods of string
# value=name1.upper()  # upper case 
# print(value)

# second_value=name1.lower() # lower case
# print(second_value)

# third_value=name1.title() first word capital
# print(third_value)

# fourth_value=name1.startswith('s')  #true or false check
# print(fourth_value)

# fifth_value=name1.endswith('p')  #true or false
# print(fifth_value)

# print(name1)
# sixth_value=name1.strip()  #leading or laging space cut
# print(sixth_value)

# message= "hello world"
# print(message.split('  '))

#       # iterators and iterables
# message="hello"
# iterator=iter(message)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#  print (message[5]) 






# print("\ n== 4. string length ===")
# text3= 'hello world'
# print("leng

# th of text3 =", len (text3))

# print("\n===5. loop through a srting ===")
# for char in "CAT":
#     print(char)


                                 #LIST DATA TYPE  D3

# frist_list=[1,2,3]
# print(type(frist_list))

# #get the middle element 
# # get the last element 
# #get the first element 
# # reverse the element 

# print(frist_list[1])
# print(frist_list[-1])
# print(frist_list[::-1])


# my_list=[1,2,3,4]
# print(id(my_list))
# adding element

# my_list.append("ent_item")
# print(my_list)
# print(id(my_list))

# my_list.insert(1, "new_item_at_1")
# print(my_list)
# print(len(my_list))

#task1 use insert method as  append method
# my_list.insert(5, "new_item_at_-1")
# print(my_list)
# print(id(my_list))

# inner_list =[5,6,7]
# print(my_list+inner_list)

# # marge_list=my_list+inner_list
# # print(id(marge_list))

# my_list.extend(inner_list)
# print(my_list)
# print(id(my_list))

# my_list = [4,1,9,2,6]

# my_list.sort()
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)

# my_list=[4,1,3,4,5,4,3,4]
# print(my_list.index(4))

# my_list.remove(4)
# print(my_list)

# value = my_list.pop(my_list.index(4))
# print(my_list)

#remove duplicate
# set_value =set(my_list)
# print(list(set_value))
 
                         #   D3 tuples


# t1=(1,2,3)
# t2=("python",3.12,True)
# print(t1)
# print(t2)

# # empty tuple
# empty=()
# print(empty)
# print(type(empty))

# # single element tuple (comma is mandatory)
# single =(10,)
# print(single)
# print(type(single))

# # without comma NOTR a tuple
# not_tuple= (10)
# print(not_tuple)
# print(type(not_tuple))

# create a tuple of 10 element
# my_tuple=(1,"two",3.0,"four",5,"six",7,8,9,10)
# print(my_tuple)

# # print element at multiple of 2
# print(my_tuple[2:10:2])


# multiply each element by 2 and print the result 
#  range 

# s=(1,2,3,4,5,6,7,8)
# result=tuple(i*2 for i in s)
# print(result)

# # a tuple is immutable 

# t = (1, 2, 3,4,5)
# print(id(t))
# t = + t(1,)
# print(id(t))





# t = (1,2,3,4,[5,6,7],8)
# t[5]= 66    
# print(t)

# t = (1, 2, [3,4,5],7)
# t[2][0]= 67
# print(t)

# # access the depest value 2 and print it 
# data=((1,2),(3,4),(5,(1,2)))
# print(data[2][1][1])

# 1. Create the dictionary
student_scores = {
    "Alex": [75, 82, 58],
    "Jordan": [45, 55, 62],
    "Taylor": [90, 88, 94]
}

# 2. Select one student (e.g., Alex)
selected_student = "Alex"
marks = student_scores[selected_student]

# 3. Calculate the average
# Sum the marks and divide by the number of exams
average = sum(marks) / len(marks)

# 4. Compare the average to the goal (60)
is_passing = average >= 60

# Output the result
print(is_passing)

