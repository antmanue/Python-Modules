import sys

def dict_build() -> dict:
    inventory = {}

    for i in range(1, len(sys.argv)): 
        param = sys.argv[i]
        try:
            if ':' not in param:
                raise ValueError("syntax")
            item, str_quantity = param.split(':')
            quantity = int(str_quantity)
            if item in inventory:
                print(f"Redundant item '{item}' - discarding")
                continue
            inventory[item] = quantity


        except ValueError as e:
            if str(e) == "syntax":
                print(f"Error - invalid parameter '{param}'")
            else:
                print(f"Quantity error for '{item}': {e}")
    return inventory

def main() -> None:
    print(f"=== Inventory System Analysis ===")
    my_inventory = dict_build()
    if not my_inventory:
        return
    total_qty = sum(my_inventory.values())
    most_item = ""
    least_item = ""
    max_qty = -1
    min_qty = -1
    print(f"Got inventory: {my_inventory}")
    print(f"Item list: {list(my_inventory.keys())}")
    print(f"Total quantity of the {len(my_inventory)} items: {total_qty}")
    for item, quantity in my_inventory.items():
        percent_qty = (quantity*100)/total_qty
        print(f"Item {item} represents {round(percent_qty, 1)}%")
        if max_qty == -1 or quantity > max_qty:
            max_qty = quantity
            most_item = item
        if min_qty == -1 or quantity < min_qty:
            min_qty = quantity
            least_item = item
    print(f"Item most abundant: {most_item} with quantity {max_qty}")
    print(f"Item least abundant: {least_item} with quantity {min_qty}")
    my_inventory.update({'magic_item': 1})
    print(f"Updated inventory: {my_inventory}")

if __name__ == "__main__":
    main()