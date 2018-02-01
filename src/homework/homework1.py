def get_hours_since_midnight(seconds):
    hours = seconds // 3600
    return hours

hours = get_hours_since_midnight(seconds)
format(hours,'02d')

def get_minutes(seconds):
    minutes = ( seconds % 3600)
    minutes //= 60

    return minutes
minutes = get_minutes(seconds)
format(minutes, '02d')

def get_seconds(seconds, minutes):
    total_seconds = (seconds % 3600) % 60

    return seconds
total_seconds = get_seconds(seconds, minutes)

print('The time since midnight is %02d:%02d:%0d' %(hours,minutes,total_seconds))
