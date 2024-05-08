# Python

# This will calculate the shapes area.

def calculate_rectangle_area(width, height):
    area = width * height
    return area

def calc_tri_area(h, b):
    area = 1 / 2 * h * b
    return area

def main():
    print('This is our shapes program')

    rectangle_area = calculate_rectangle_area(10, 20)
    print(f'The area of the rectangle is: {rectangle_area}')

    tri_area = calc_tri_area(20, 79)
    print(f'The area of the triangle is: {tri_area}')

main()