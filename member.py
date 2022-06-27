import helper as helper
from timerange import TimeRange
from dataclasses import dataclass, field
from typing import ClassVar

class Member:
    busy_times = []
    all_busy_minutes = []

    def __init__(self, name = None):
        self.name = name
    
    def add_busy_range(self, tr:TimeRange):
        # Initialise time range object values for members busy times
        self.busy_times.append(tr)
        Member.all_busy_minutes.append(tr.minutesRange)
        
#@dataclass
#class Member:
#    all_busy_minutes: ClassVar[list] = []
#    name : str
#    busy_times : list[TimeRange] = field(default_factory=list, repr=False)

#    def add_busy_range(self, tr:TimeRange):
#        # Initialise time range object values for members busy times
#        self.busy_times.append(tr)
#        Member.all_busy_minutes.append(tr.minutesRange)

