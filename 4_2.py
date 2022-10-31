my_list = [23, 14, 85, 10, 3, 100, 323, 8, 5]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num -1]]
print(more_then)