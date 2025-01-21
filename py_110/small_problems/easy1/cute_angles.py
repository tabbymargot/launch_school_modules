DEGREE = "\u00B0"

# Minutes per degree and seconds per minute are both 60.
MULTIPLIER = 60

def calculate_minutes_and_seconds(number, integer):
    return (number - integer) * MULTIPLIER

def append_zero(integer):
    if len(str(integer)) == 1:
        return f'0{str(integer)}'
    else:
        return f'{str(integer)}'
    
def dms(degrees):
    minutes = calculate_minutes_and_seconds(degrees, int(degrees))
    seconds = calculate_minutes_and_seconds(minutes, int(minutes))

    degrees_string = str(int(degrees))
    minutes_string = append_zero(int(minutes))
    seconds_string = append_zero(int(seconds))

    return (f"{degrees_string}{DEGREE}"
            f"{minutes_string}'"
            f'{seconds_string}"')

print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"")
      
    #   or dms(360) == "0°00'00\"")