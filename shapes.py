# Python

# This will calculate the shapes area.

def calculate_rectangle_area(width, height):
    area = width * height
    return area

def main():
    print('This is our shapes program')

    rectangle_area = calculate_rectangle_area(10, 20)
    print(f'The area of the rectangle is: {rectangle_area}')

main()