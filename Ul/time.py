def hours_passed(time1, time2):

    if time1 == time2:
        return"no time passed"

    time1_clock, time1_period = time1.split()
    time2_clock, time2_period = time2.split()
    hours1, minutes1 = time1_clock.split(':')
    hours2, minutes2 = time2_clock.split(':')

    if time1_period == time2_period:
        return str(int(hours1) - int(hours2)) + " hours"
    else:
        return str(12 - int(hours1) - int(hours2)) + " hours"

print(hours_passed("1:00 AM", "3:00 PM"))
