# Python

# This will calculate the shapes area.

def calculate_rectangle_area(width, height):
    area = width * height
    return area

def calculate_triangle_area(height, base):
    area = 1/2 * base * height
    return area

def main():
    print('This is our shapes program')

    rectangle_area = calculate_rectangle_area(10, 20)
    print(f'The area of the rectangle is: {rectangle_area}')

    triangle_area = calculate_triangle_area(20, 40)
    print(f'The area of the triangle is: {triangle_area}')

main()