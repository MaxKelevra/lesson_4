from itertools import count, cycle

my_count = count(5)
my_cycle = cycle("ABC")

for _ in range(4):
    print("my_count, my_cycle) = ({}, {})".format(next(my_count), next(my_cycle)))