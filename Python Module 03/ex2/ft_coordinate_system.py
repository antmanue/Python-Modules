import math


def get_players_pos() -> tuple[float, float, float]:
    while True:
        string = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            x_str, y_str, z_str = string.split(',')
        except ValueError:
            print("Invalid syntax")
            continue

        try:
            clean_p = x_str.strip()
            x = float(clean_p)

            clean_p = y_str.strip()
            y = float(clean_p)

            clean_p = z_str.strip()
            z = float(clean_p)

            return (x, y, z)
        except ValueError as err:
            print(f"Error on parameter '{clean_p}': {err}")


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    my_tuple1 = get_players_pos()
    x1, y1, z1 = my_tuple1
    print(f"Got a first tuple: {my_tuple1}")
    coord_total1 = ((x1**2) + (y1**2) + (z1**2))
    dist = math.sqrt(coord_total1)
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance to center: {dist:.4f}")
    print()
    print("Get a second set of coordinates")
    my_tuple2 = get_players_pos()
    x2, y2, z2 = my_tuple2
    dist2p = math.sqrt(((x2-x1)**2) + ((y2-y1)**2) + ((z2-z1)**2))
    print(f"Distance between the 2 sets of coordinates: {dist2p:.4f}")


if __name__ == "__main__":
    main()
