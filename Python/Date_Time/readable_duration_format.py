def format_duration(seconds):
    if seconds == 0:
        return "now"
    years, seconds = divmod(seconds, 365 * 24 * 60 * 60)
    days, seconds = divmod(seconds, 24 * 60 * 60)
    hours, seconds = divmod(seconds, 60 * 60)
    minutes, seconds = divmod(seconds, 60)
    time_units = []
    if years > 0:
        time_units.append(f"{years} year"if years == 1 else f"{years} years")
    if days > 0:
        time_units.append(f"{days} day"if days == 1 else f"{days} days")
    if hours > 0:
        time_units.append(f"{hours} hour"if hours == 1 else f"{hours} hours")
    if minutes > 0:
        time_units.append(f"{minutes} minute" if minutes ==
                          1 else f"{minutes} minutes")
    if seconds > 0:
        time_units.append(f"{seconds} second" if seconds ==
                          1 else f"{seconds} seconds")

    if len(time_units) > 1:
        return ", ".join(time_units[:-1]) + " and " + time_units[-1]
    else:
        return time_units[0]


print(format_duration(0))
print(format_duration(15731080))
print(format_duration(3500))

"""
    Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
    
    
    
Link:https://www.codewars.com/kata/52742f58faf5485cae000b9a/python
"""
