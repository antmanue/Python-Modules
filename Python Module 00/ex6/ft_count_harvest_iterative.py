def ft_count_harvest_iterative() -> None:
    days_to = int(input("Days until harvest: ")) + 1
    i = 1
    while (i < days_to):
        print("Day ", i)
        i = i + 1
    print("Harvest time!")
