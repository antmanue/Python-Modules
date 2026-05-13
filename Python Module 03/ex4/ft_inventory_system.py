import sys

def dict_build() -> None:
    inventory = {}

    for i in range(1, len(sys.argv)): 
        param = sys.argv[i]
        try
            if ':' not in param:
                raise ValueError("syntax")
            item, str_quantity = param.split(':')
            if item in inventory:
                print(f"Redundant item '{item}' discarding")
                continue
        except ValueError as e:
            if str(e) == "syntax":
                print(f"Error invalid parameter '{param}'")
            else
                print(f"Quantity error for '{item}: {e}'")

        quantity = int(str_quantity)
        inventory[item] = "quantity"