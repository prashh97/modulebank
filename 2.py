#2a
def convert_to_list_and_tuple():
    numbers = input("Enter comma-separated numbers: ")
    num_list = numbers.split(",")
    num_tuple = tuple(num_list)  

    print("List:", num_list)
    print("Tuple:", num_tuple)

convert_to_list_and_tuple()


# 2b: Separate even and odd numbers
def separate_numbers():
    numbers = input("Enter numbers: ") 
    numbers = numbers.split(",")
    
    pos_list = []  
    neg_list = []  

    for num in numbers:  
        num = int(num) 
        if num >= 0:  
            pos_list.append(num) 
        else:
            neg_list.append(num)

    print("Positive List:", pos_list)
    print("Negative List:", neg_list)
    print("Positive Tuple:", tuple(pos_list))
    print("Negative Tuple:", tuple(neg_list))

separate_numbers()


# 2c: Calculate the sum and average
def sum_and_average():
    numbers = input("Enter numbers: ")
    numbers = numbers.split(",") 

    num_list = []
    for num in numbers:
        num_list.append(int(num))  
    total_sum = 0 
    count = 0 

    for num in num_list:
        total_sum += num
        count += 1  
    average = total_sum / count  

    print("List:", num_list)
    print("Tuple:", tuple(num_list))
    print("Sum:", total_sum)
    print("Average:", average)

sum_and_average()


# 2d: Count sum of even and odd numbers
def even_odd_separation():
    numbers = input("Enter numbers: ")
    numbers = numbers.split(",")

    even_list = []
    odd_list = []

    for num in numbers:
        num = int(num)
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)  

    even_sum = 0 
    odd_sum = 0  

    for num in even_list:
        even_sum += num  

    for num in odd_list:
        odd_sum += num 

    print("Even List:", even_list)
    print("Odd List:", odd_list)
    print("Even Tuple:", tuple(even_list))
    print("Odd Tuple:", tuple(odd_list))
    print("Sum of Even Numbers:", even_sum)
    print("Sum of Odd Numbers:", odd_sum)

even_odd_separation()
