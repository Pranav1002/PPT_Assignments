def canAttendMeetings(intervals):
        
    intervals.sort(key=lambda a: a.start)
    for i in range(len(intervals)-1):
        if intervals[i].end > intervals[i+1].start:
            return False
    return True