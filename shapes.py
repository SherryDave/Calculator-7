import math
#python code that acts as a calculator for the geometrical shapes
# Global unit variable
unit = ""

def square():
    side = float(input(f"Enter the side of the square ({unit}): "))
    print("\nWhat do you want to calculate?")
    print("1. Area")
    print("2. Perimeter")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        area = side ** 2
        print(f"Formula: Area = side × side")
        print(f"Area = {side} × {side} = {area} {unit}²\n")
    elif choice == '2':
        perimeter = 4 * side
        print(f"Formula: Perimeter = 4 × side")
        print(f"Perimeter = 4 × {side} = {perimeter} {unit}\n")
    else:
        print("Invalid choice.\n")

def rectangle():
    length = float(input(f"Enter the length ({unit}): "))
    width = float(input(f"Enter the width ({unit}): "))

    print("\nWhat do you want to calculate?")
    print("1. Area")
    print("2. Perimeter")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        area = length * width
        print(f"Formula: Area = length × width")
        print(f"Area = {length} × {width} = {area} {unit}²\n")
    elif choice == '2':
        perimeter = 2 * (length + width)
        print(f"Formula: Perimeter = 2 × (length + width)")
        print(f"Perimeter = 2 × ({length} + {width}) = {perimeter} {unit}\n")
    else:
        print("Invalid choice.\n")

def circle():
    radius = float(input(f"Enter the radius of the circle ({unit}): "))

    print("\nWhat do you want to calculate?")
    print("1. Area")
    print("2. Circumference")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        area = math.pi * radius ** 2
        print("Formula: Area = π × radius²")
        print(f"Area = π × {radius}² = {area:.2f} {unit}²\n")
    elif choice == '2':
        circumference = 2 * math.pi * radius
        print("Formula: Circumference = 2 × π × radius")
        print(f"Circumference = 2 × π × {radius} = {circumference:.2f} {unit}\n")
    else:
        print("Invalid choice.\n")


def triangle():
    base = float(input(f"Enter the base ({unit}): "))
    height = float(input(f"Enter the height ({unit}): "))

    area = 0.5 * base * height
    print("Formula: Area = 0.5 × base × height")
    print(f"Area = 0.5 × {base} × {height} = {area} {unit}²\n")


def cube():
    side = float(input(f"Enter the side of the cube ({unit}): "))
    print("\nWhat do you want to calculate?")
    print("1. Surface Area")
    print("2. Volume")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        surface_area = 6 * side ** 2
        print("Formula: Surface Area = 6 × side²")
        print(f"Surface Area = 6 × {side}² = {surface_area} {unit}²\n")
    elif choice == '2':
        volume = side ** 3
        print("Formula: Volume = side³")
        print(f"Volume = {side}³ = {volume} {unit}³\n")
    else:
        print("Invalid choice.\n")


def cuboid():
    length = float(input(f"Enter the length ({unit}): "))
    width = float(input(f"Enter the width ({unit}): "))
    height = float(input(f"Enter the height ({unit}): "))

    print("\nWhat do you want to calculate?")
    print("1. Surface Area")
    print("2. Volume")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        surface_area = 2 * (length * width + width * height + height * length)
        print("Formula: Surface Area = 2 × (lw + wh + hl)")
        print(f"Surface Area = 2 × ({length}×{width} + {width}×{height} + {height}×{length}) = {surface_area} {unit}²\n")
    elif choice == '2':
        volume = length * width * height
        print("Formula: Volume = length × width × height")
        print(f"Volume = {length} × {width} × {height} = {volume} {unit}³\n")
    else:
        print("Invalid choice.\n")


def triangular_prism():
    base = float(input(f"Enter the base of the triangle ({unit}): "))
    height_triangle = float(input(f"Enter the height of the triangle ({unit}): "))
    length = float(input(f"Enter the length of the prism ({unit}): "))
    side1 = float(input(f"Enter side 1 of the triangle ({unit}): "))
    side2 = float(input(f"Enter side 2 of the triangle ({unit}): "))

    print("\nWhat do you want to calculate?")
    print("1. Surface Area")
    print("2. Volume")
    choice = input("Enter 1 or 2: ")

    triangle_area = 0.5 * base * height_triangle
    perimeter_base = base + side1 + side2

    if choice == '1':
        surface_area = 2 * triangle_area + perimeter_base * length
        print("Formula: Surface Area = 2 × Triangle Area + Perimeter × Length")
        print(f"Surface Area = 2 × (0.5 × {base} × {height_triangle}) + ({base} + {side1} + {side2}) × {length}")
        print(f"Surface Area = {surface_area} {unit}²\n")
    elif choice == '2':
        volume = triangle_area * length
        print("Formula: Volume = Triangle Area × Length")
        print(f"Volume = (0.5 × {base} × {height_triangle}) × {length} = {volume} {unit}³\n")
    else:
        print("Invalid choice.\n")


def triangular_pyramid():
    base = float(input(f"Enter the base of the triangle ({unit}): "))
    height_triangle = float(input(f"Enter the height of the triangle ({unit}): "))
    slant_height = float(input(f"Enter the slant height of the pyramid ({unit}): "))
    height_pyramid = float(input(f"Enter the vertical height of the pyramid ({unit}): "))

    print("\nWhat do you want to calculate?")
    print("1. Surface Area")
    print("2. Volume")
    choice = input("Enter 1 or 2: ")

    base_area = 0.5 * base * height_triangle
    lateral_area = 3 * (0.5 * base * slant_height)

    if choice == '1':
        surface_area = base_area + lateral_area
        print("Formula: Surface Area = Base Area + Lateral Area")
        print(f"Surface Area = (0.5 × {base} × {height_triangle}) + 3 × (0.5 × {base} × {slant_height})")
        print(f"Surface Area = {surface_area} {unit}²\n")
    elif choice == '2':
        volume = (1/3) * base_area * height_pyramid
        print("Formula: Volume = (1/3) × Base Area × Height")
        print(f"Volume = (1/3) × (0.5 × {base} × {height_triangle}) × {height_pyramid} = {volume} {unit}³\n")
    else:
        print("Invalid choice.\n")


def sphere():
    radius = float(input(f"Enter the radius ({unit}): "))

    print("\nWhat do you want to calculate?")
    print("1. Surface Area")
    print("2. Volume")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        surface_area = 4 * math.pi * radius ** 2
        print("Formula: Surface Area = 4 × π × radius²")
        print(f"Surface Area = 4 × π × {radius}² = {surface_area:.2f} {unit}²\n")
    elif choice == '2':
        volume = (4/3) * math.pi * radius ** 3
        print("Formula: Volume = (4/3) × π × radius³")
        print(f"Volume = (4/3) × π × {radius}³ = {volume:.2f} {unit}³\n")
    else:
        print("Invalid choice.\n")


def cylinder():
    radius = float(input(f"Enter the radius ({unit}): "))
    height = float(input(f"Enter the height ({unit}): "))

    print("\nWhat do you want to calculate?")
    print("1. Surface Area")
    print("2. Volume")
    choice = input("Enter 1 or 2: ")

    if choice == '1':
        surface_area = 2 * math.pi * radius ** 2 + 2 * math.pi * radius * height
        print("Formula: Surface Area = 2πr² + 2πrh")
        print(f"Surface Area = 2π × {radius}² + 2π × {radius} × {height} = {surface_area:.2f} {unit}²\n")
    elif choice == '2':
        volume = math.pi * radius ** 2 * height
        print("Formula: Volume = π × r² × h")
        print(f"Volume = π × {radius}² × {height} = {volume:.2f} {unit}³\n")
    else:
        print("Invalid choice.\n")

# Ask if user wants to continue
def ask_continue():
    again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    return again in ['yes', 'y']

# Main menu
def main():
    global unit
    print("Welcome to the Geometry Calculator!")
    unit = input("Enter the unit(e.g., cm, m, in): ").strip()

    while True:
        print("\nChoose a shape:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Triangle")
        print("5. Cube")
        print("6. Cuboid")
        print("7. Triangular Prism")
        print("8. Triangular Pyramid")
        print("9. Sphere")
        print("10. Cylinder")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ").strip()

        if choice == '1':
            square()
        elif choice == '2':
            rectangle()
        elif choice == '3':
            circle()
        elif choice == '4':
            triangle()
        elif choice == '5':
            cube()
        elif choice == '6':
            cuboid()
        elif choice == '7':
            triangular_prism()
        elif choice == '8':
            triangular_pyramid()
        elif choice == '9':
            sphere()
        elif choice == '10':
            cylinder()
        elif choice == '11':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        if not ask_continue():
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
