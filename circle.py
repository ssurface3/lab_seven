import math
import sys

def compute_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2

def main():
    try:
        print("Enter the radius of the circle: ", end='')
        sys.stdout.flush()
        radius = float(input())
        if radius < 0:
            print("Radius cannot be negative.")
            return
        area = compute_area(radius)
        print(f"The area of the circle with radius {radius} is {area:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
