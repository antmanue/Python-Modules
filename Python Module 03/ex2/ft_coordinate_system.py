import math
def input_str() -> tuple:
    while True:
        string = input("Enter new coordinates as floats in format 'x,y,z': ")
        split_string = string.split(',')
        if len(split_string) != 3:
            print("Invalid syntax")
            continue
        try:
            current_coord = []
            for p in split_string:
                clean_p = p.strip()
                coordinates = float(clean_p)
                current_coord.append(coordinates)
            if len(current_coord) == 3:
                return tuple(current_coord)
            print("Invalid syntax")
        except ValueError as e:
            print(f"Error on parameter '{clean_p}': {e}")

def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print(f"Get a first set of coordinates")
    my_tuple1 = input_str()
    x1, y1, z1 = my_tuple1
    print(f"Got a first tuple: {my_tuple1}")
    coord_total1 = ((x1**2) + (y1**2) + (z1**2))
    dist = math.sqrt(coord_total1)
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance to center: {dist:.4f}")
    print()
    print(f"Get a second set of coordinates")
    my_tuple2 = input_str()
    x2, y2, z2 = my_tuple2
    dist2p = math.sqrt(((x2-x1)**2) + ((y2-y1)**2) + ((z2-z1)**2))
    print(f"Distance between the 2 sets of coordinates: {dist2p:.4f}")


if __name__ == "__main__":
    main()