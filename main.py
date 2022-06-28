from timerange import TimeRange
from member import Member
from time_list import TimeList
import helper as helper
import time as time

def main():
    try: # Try and except to catch int casting error if user input is not an int
        no_of_members = input("How many members are in the meeting: ", ) # Save user input of number of members

        if int(no_of_members) in range(0, 10): # Check if input is digit 0-9

            i = 0 # Initialise iterator for while loop
            while i < int(no_of_members): # Iterate through number of members inputted
                name = input(f"Please enter member {i + 1}'s name: ", ) # Save user input of members name
                no_of_busy_intervals = input(f"Please enter the number of time intervals '{name}' is busy: ", ) # Save input of number of busy time intervals

                try: # Try and except to catch int casting error if user input is not an int

                    if int(no_of_busy_intervals) in range(0, 10): # Check if input is digit 0-9
                        member = Member(name) # Instantiate new member object 
                        
                        j = 0 # Initialise iterator for while loop
                        while j < int(no_of_busy_intervals): # Iterate through number of busy intervals inputted
                            start = input(f"Please enter the start time for busy interval {j + 1}: ", ) # Save start time for each interval
                            end = input(f"Please enter the end time for busy interval {j + 1}: ", ) # Save end time for each interval

                            try: # Try and except to catch if user input is not in the correct format
                                if (time.strptime(start, '%H:%M') or time.strptime(end, '%H:%M')): # Check for input format
                                    member.add_busy_range(TimeRange(start, end)) # Add new time range object for member for each busy time interval
                                else:
                                    print("Please enter valid times in the format HH:MM") # Return message for correct format
                                    j -= 1 # Decrement iterator to ask for incorrect intervals again
                            except ValueError:
                                print("Please enter valid times in the format HH:MM") # Return message for correct format
                                j -= 1 # Decrement iterator to ask for incorrect intervals again
                            j += 1 # Increment iterator 
                    else:
                        i -= 1 # Decrement iterator to ask for number of intervals again
                except:
                    print("Please enter a single valid digit 0-9") # Return message of incorrect input
                    i -= 1 # Decrement iterator to ask for number of intervals again
                i += 1 # Increment iterator
                    
            available_times_minutes = TimeList(range(1440)) # List to store available times, initialised with all minutes in the day

            for m in available_times_minutes[:]:
                # Looping through copy of all minutes in the day and removing busy minutes from list
                for r in Member.all_busy_minutes:
                    # Check all busy times for all members
                    if m in r:
                        available_times_minutes.remove_if_exists(m)

            for tr in helper.available_time_ranges(available_times_minutes):
                print(f"Available time at {tr}")
        
        else:
            print("Please enter a digit from 0-9")
            main()
    except ValueError:
        print("Please enter a digit from 0-9")
        main()


if __name__ == "__main__":
    main()