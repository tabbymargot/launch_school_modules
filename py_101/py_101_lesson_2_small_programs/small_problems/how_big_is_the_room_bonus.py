"""  
Ask user if they want to use meters or feet and save to a variable.
Get the input and calculate the area
If in feet, convert to meters and output string accordingly.
If in meters, convert to feet and output string accordingly.

"""

# Note that this solution assumes the user is inputting valid data.

def prompt(message):
    print(f'==> {message}')

def calculate_area(length, width):
    room_area = length * width
    return room_area

def convert_to_meters(room_area):
    room_area_in_square_meters = room_area / 10.7639
    return room_area_in_square_meters

def convert_to_feet(room_area):
    room_area_in_square_feet = room_area * 10.7639
    return room_area_in_square_feet

prompt('Would you like to use feet or meters? Input "f" for feet and "m" for meters')
measurement_type = input()

prompt("Enter the length")
length = float(input())
prompt("Enter the width in meters")
width = float(input())

room_area = calculate_area(length, width)

if measurement_type == 'f':
    room_area_in_square_meters = convert_to_meters(room_area)
    print(f'The area in square feet is {room_area}, and the area in square meters is {room_area_in_square_meters:.2f}.')
elif measurement_type == 'm':
    room_area_in_square_feet = convert_to_feet(room_area)
    print(f'The area in square meters is {room_area}, and the area in square feet is {room_area_in_square_feet:.2f}.')