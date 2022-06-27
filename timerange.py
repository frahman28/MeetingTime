import helper as helper
from dataclasses import dataclass, field

class TimeRange:
    def __init__(self, startTime, endTime, startMinutes = None, endMinutes = None, minutesRange = None):
        self.start_time = startTime
        self.end_time = endTime

        self.start_minutes = helper.timerange_convert_minutes(self.start_time)
        self.end_minutes = helper.timerange_convert_minutes(self.end_time)
        self.minutesRange = range(self.start_minutes, self.end_minutes, 1)
        

#@dataclass
#class TimeRange:
#    startTime : str
#    endTime : str
#
#    startMinutes : int = field(init=False, repr=False)
#    endMinutes : int = field(init=False, repr=False)
#
#    minutesRange : range = field(init=False, repr=False)
#

#    def __post_init__(self):
#        self.startMinutes = helper.timerange_convert_minutes(self.startTime)
#        self.endMinutes = helper.timerange_convert_minutes(self.endTime)
#        self.minutesRange = range(self.startMinutes, self.endMinutes, 1)
        
