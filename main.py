from timerange import TimeRange
from member import Member
from time_list import TimeList
import helper as helper

def main():
    available_times_minutes = TimeList(range(1440)) # List to store available times, initialised with all minutes in the day
    m1 = Member("Jim")
    m1.add_busy_range(TimeRange("08:00", "10:00"))
    m2 = Member("Chris")
    m2.add_busy_range(TimeRange("12:00", "14:00"))

    for m in available_times_minutes[:]:
        # Looping through copy of all minutes in the day and removing busy minutes from list
        for r in Member.all_busy_minutes:
            # Check all busy times for all members
            if m in r:
                available_times_minutes.remove_if_exists(m)

    for tr in helper.available_time_ranges(available_times_minutes):
        print(f"Available time at {tr}")


if __name__ == "__main__":
    main()

