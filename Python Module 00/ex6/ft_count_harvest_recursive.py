def ft_count_harvest_recursive() -> None:
    days_to = int(input("Days until harvest: "))

    def counter(i: int):
        if i <= days_to:
            print("Day ", i)
            counter(i + 1)
        else:
            print("Harvest time! ")
    counter(1)
