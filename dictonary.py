

# dict1 = {'name':'abcd','age':36}
# dict2={'age':26 , "name":"egft"}
# print(id(dict1))
# print(dict1==dict2)
# print(dict1 is dict2)
# print(id(dict1==dict2))
# print(id(dict1 is dict2))

# merging  the dict
# 1. union merge
# return_dict = dict2 | dict1
# print(return_dict)

# 2. update merge
# dict1.update(dict2)
# print(id(dict1))
#
# 3. keyword argument merge
# result_dict ={**dict1,**dict2}
# print(result_dict)

# 4.removing key value

dict3 ={"name":"sudip", "age":"20"}
value = dict3.pop("name")
print(value)
print(dict3)

# 
# value= dict3.popitem()
# print(value)
# print(dict3)