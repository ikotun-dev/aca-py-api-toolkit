def linear_search(list, target):
    flag = 0
    for index in range(len(list)):
        if list[index] == target:
            flag = 1
            print("element found at"  + " " + str(index))  
    if flag == 1:
        pass
    else :
        print("element was not found")
    
numbers = [3, 9, 2, 7, 1, 5]
target_number = 7

linear_search(numbers, target_number)
