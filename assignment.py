# # task 1
# student_scores={
#     "sudip":[78,50,67],
#     "samir":[30,34,20],  }


# selected_student="sudip"
# average=sum(student_scores["sudip"]) / len(student_scores["sudip"])

# if average >=60:
#     print("true")
# else:
#     print("false")


# task 2
stock = {"apples": 10, "bananas": 2, "oranges": 0}
if "pears" in stock :
    print("pears in stock")
else:
    print("not in stock")

if "bananas" in stock  and stock["bananas"] < 5:
    print("Time to restock bananas")


# task 3
users = {"admin": "1234"}

users["teacher"] = "password789"

input_user="admin"
input_pass="1234"

if (input_user in users and users [input_user] ==input_pass):
    print("access granted")
# else:
#     print("access denied")