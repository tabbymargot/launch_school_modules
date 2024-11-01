"""  
Ask for the length and store it
Ask for the width and store it
Convert the values to feet and store them.
Create a function that calculates the room area.
Get the area in both meters and feet by passing in the vars for both.
Output the values using string interpolation.
"""

def prompt(message):
    print(f'==> {message}')

def calculate_area(length_in_meters, width_in_meters):
    room_area_in_square_meters = length_in_meters * width_in_meters
    return room_area_in_square_meters


def convert_to_feet(room_area_in_square_meters):
    room_area_in_square_feet = room_area_in_square_meters * 10.7639
    return room_area_in_square_feet

prompt("Enter the length in meters")
length_in_meters = float(input())
prompt("Enter the width in meters")
width_in_meters = float(input())

room_area_in_square_meters = calculate_area(length_in_meters, width_in_meters)
room_area_in_square_feet = convert_to_feet(room_area_in_square_meters)

print(f'The area in square meters is {room_area_in_square_meters}, and the area in square feet is {room_area_in_square_feet}.')