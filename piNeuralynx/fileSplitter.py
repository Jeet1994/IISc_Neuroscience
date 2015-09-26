""" this works because the ncs timestamps are sorted array on basis of time"""
def nextGreaterElement(timestamps, eventStartTimestamp):
	for index,ts in enumerate(timestamps):
		if ts > eventStartTimestamp:
			return ts
	raise ValueError("Nothing Found")

def nextSmallerElement(timestamps, eventStopTimestamp):
	try: return max(ts for ts in timestamps if ts< eventStopTimestamp)
	except ValueError: return "Nothing Found"

def fileSplitterUsingEvents(ncsData, eventStartTimestamp, eventStartName, eventStopTimestamp, eventStopName):
	"""Splits the ncs data on the basis of event start time and event stop time.
        Keyword arguments:
        ncsData -- refers to the data collected over a channel
        eventStartTimestamp --  start time for the event
        eventStartName --  event name for the starting timestamp
        eventStopTimestamp --  stop time for the event
        eventStopName -- event name for the stopping timesamp
        Returns (in order):
        - frequency data in the range between event start time and event stop time
        """
	
	#store all the timestamps in one single list
	ncsTimestamp = []
	for ts in ncsData[1]:
		ncsTimestamp.append(ts[0])

	#get time stamp next to start time
	eventStartTime = nextGreaterElement(ncsTimestamp, eventStartTimestamp)
	#get time stamp just before stop time
	eventStopTime = nextSmallerElement(ncsTimestamp, eventStopTimestamp)

	dataPoints = []
	for ts in ncsData[1]:
		if ts[0]>= eventStartTime and ts[0]<=eventStopTime:
                 for t in ts[4]:
                     dataPoints.append(t)
	return dataPoints