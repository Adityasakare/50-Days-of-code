#PRIME NUMBER

# num = 3
num = int(input("Enter a prime number: "))

if num >1:
    for i in range(2 , num):
        if (num % i == 0 ):
            print(num , "This is not PRime Number")
            break
    else:
        print(" a prime number")