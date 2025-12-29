# def greet_student(name):
#     print(f"Hello {name}! welcome to python class")

# name="sudip"
# greet_student(name)

# def greet_name(name):
#     return (f"my name is {name})"

# print(greet_name(10))

# task 1
# related positional argument and keyword arguments
# create a small function to calculate the volume of cuboid 
# def volume_cuboid(length,width,hight):
#     volume=length*width*hight
#     return volume

# l=2
# w=3
# h=7
# print(volume_cuboid(l,w,h))


# reverse the list using function call 
# my_list=[1,2,3,4]
# my_list.reverse()
# print(my_list)


# def reverse_list(listing):
#     listing=[1,2,3,4]
#     return listing
# print(reverse_list())

# repeat same message multiple n time using function 
# def repeat_same_message(message,n):
#     for  i in range(9):
#         print(message)

# repeat_same_message("hello world,",9)
    
# recursive functions
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(7))



# sum of natural number usinf recursive function 
# def natural_number(n):
#     if n==1:
#         return n
#     else:
#         return n + natural_number(n-1)
# print(natural_number(10))


# from the list find the smallest number using recursive function

# def smallest_number(li1):
#     if len(li1) == 1:
#         return li1[0]
#     else:
#         return  li1 [0]if li1[0] < smallest_number else li1


# (smallest_number(li1=[1,2,3,4,5,6,7]))
    
# def find_min(arr):
#     # Base case: if the list has only one element
#     if len(arr) == 1:
#         return arr[0]
    
#     # Recursive step: find the minimum of the rest of the list
#     rest_min = find_min(arr[1:])
    
#     # Return the smaller of the first element and the rest_min
#     return arr[0] if arr[0] < rest_min else rest_min

# # Example usage:
# numbers = [34, 12, 5, 89, 67]
# print(f"The smallest number is: {find_min(numbers)}")

    
# def greet(a,b):
#     print(f"hello {a} {b}")
#     print("welcome to python class")


# greet("sudip","shrestha")