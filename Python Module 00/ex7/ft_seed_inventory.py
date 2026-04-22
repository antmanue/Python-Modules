def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        unit = "packets available."
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit}")
    elif unit == "grams":
        unit = "grams total"
        print(f"{seed_type.capitalize()} seeds: {quantity} {unit}")
    elif unit == "area":
        unit = "square meters"
        print(f"{seed_type.capitalize()} seeds: covers {quantity} {unit}")
    else:
        print("Unknown unit type")
