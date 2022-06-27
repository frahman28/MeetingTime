def timerange_convert_minutes(timeString):
    # Taking string input of time in format HH:MM return amount of minutes
    
    hours = int(timeString.split(":")[0])
    minutes = int(timeString.split(":")[1])

    # Convert hours to minutes 
    hours_as_minutes = hours * 60

    return hours_as_minutes + minutes

def timerange_convert_string(mins):
    # Taking minutes and return formatted string in HH:MM

    hour = mins // 60 # Get floor division of minutes for hours
    hour_string = f"{hour:02d}" # Convert hours value to string in 00 format

    minutes = int(mins) % 60 # Remainder will be MM of HH:MM
    minutes_string = f"{minutes:02d}" # Convert minutes value to string in 00 format

    return f"{hour_string}:{minutes_string}"

def available_time_ranges(times: list):
    ranges = [] # List to store evaluated time ranges of availability

    group = [] # List to store a range which will be added to ranges and reset for each subsequent range

    for time in times:
        # Loop through each time in minutes grouping congruent times
        if group == []: # Add first time in group
            group.append(time)
            continue
        if group[-1] + 1 == time: # Add time if increment of previous element
            group.append(time)
        else: # If not an increment reset group list
            ranges.append(group[:])
            group.clear()
            group.append(time)
    
    ranges.append(group) # Add group to ranges

    times = [] # List to store time ranges formatted 

    for r in ranges:
        startTime = timerange_convert_string(r[0])
        endTime = timerange_convert_string(r[-1])

        range_string = f"{startTime} - {endTime}"

        times.append(range_string)
    
    return times


