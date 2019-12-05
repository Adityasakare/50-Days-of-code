
#Traditional Method

# def addme (num1 , num2):
#     total = num1 + num2

#     return total

# to = addme(2,3)
# print(to)


#Multi_args

# def addme (*num1):
#     total = 0
#     for i in num1:
#         total = total + i

#     return total

# to = addme(2,3, 5 , 8 ,9 )
# print(to)


#Assignment

def sub(num1 , num2):
    total = 100
    for i in num1:
        total= total - i
    for k in num2:
        total= total - k

    return total

print(sub(2 , 3)) 