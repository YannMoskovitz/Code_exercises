def timeConversion(s):
    time_characters_list = [char for char in s]
    minutes_seconds_list = time_characters_list[2:8]
    minutes_seconds = '' # sliced and concatenated ":mm:ss" so it will be concatenated with the correct "hour" variable 
    hour = s[:2]
    for t in minutes_seconds_list:
        minutes_seconds += t
    if "P" in time_characters_list:
        
        if hour == '12':
            return hour + minutes_seconds
        else:
            hour = int(hour) + 12
            return str(hour) + minutes_seconds
    else:
        if hour == '12':
            hour = '00'
            return hour + minutes_seconds
        else:
            return hour + minutes_seconds
    
s = '09:15:24PM'
x = '09:15:24AM'
z = '12:05:39AM'
a = '12:45:54PM'
b = '12:40:22AM'
print(timeConversion(s))
print(timeConversion(x))
print(timeConversion(z))
print(timeConversion(a))
print(timeConversion(b))

