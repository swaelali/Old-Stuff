def clock_angle(clock):
	hours = int(clock[0:2])
	if hours >= 12:
		hours = hours -12
	
	minutes = int(clock[3:5])
	
	hours_angle = 0.5*((60*hours) + minutes)
	minutes_angle = 6 * minutes
	
	angle = abs(hours_angle - minutes_angle)
	if angle > 180:
		angle = 360- angle
	return angle
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"
