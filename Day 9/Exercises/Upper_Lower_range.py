Lower_range = 2
Upper_range = 10

for number in range(Lower_range , Upper_range):
    if number > 1:
        for i in range(2, number):
            if (number%i == 0):
                
                break
            else:
                print(number)