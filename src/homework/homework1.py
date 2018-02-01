def get_hours_since_midnight(total_seconds):
    hours = total_seconds // 3600
    return hours

total_seconds = int(input('Enter a number of seconds: '))
hours = get_hours_since_midnight(total_seconds)
format(hours,'02d')

def get_minutes(total_seconds):
    minutes = ( total_seconds % 3600)
    minutes //= 60

    return minutes
minutes = get_minutes(total_seconds)
format(minutes, '02d')

def get_seconds(total_seconds, minutes):
    seconds = (total_seconds % 3600) % 60

    return seconds
seconds = get_seconds(total_seconds, minutes)

print('The time since midnight is %02d:%02d:%0d' %(hours,minutes,seconds))
