def ft_plant_age() -> None:
    age_days = int(input("Enter plant age in days:"))
    if age_days < 60:
        print("Plant needs more time to grow.")
    if (age_days >= 60):
        print("Plant is ready to harvest!")
