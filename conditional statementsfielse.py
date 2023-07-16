# # conditional oprators:
# #     < , <= , >= , > , ==, !=
# a=10
# print(a<10)
# print(a>10)
# print(a==10)
# print(a!=10)
# print(a>=10)
# print(a<=10)

# if-else
age=18
print("\nif-else Statments")
if (age<18):
    print("you cannot Vote")
    print("you cannot Drive")
else:
    print("You can't Vote and Drive")
    
# if-else_elif
age=18
print("\nif-else_elif Statments")
if (age<18):
    print("you cannot Vote")
    print("you cannot Drive")
elif(age>=18):
    print("You can't Vote and Drive")
else:
    print("You cannot Vote ")
    
# Nested if-else_elif
age=18
print("\nNested if-else_elif Statments")
if (age<18):
    if(age>0):
        print("you cannot Vote")
        print("you cannot Drive")  
    else:
        print("You Enter Wrong Age Please check this Again")       
else:
    if(age<85):
        print("You can't Vote")
    else:
        print("You cannot Vote")
