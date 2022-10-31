from random import randint
num_list = [randint(-10, 10) for _ in range (20)]
my_list = [el for el in num_list if num_list.count(el) == 1]
print(f"Исходный список\n{num_list}\nСписок без повторов\n{my_list}")
