import math


def format_duration(seconds):
    if seconds == 0:
        return "now"

    time_dict = {}
    time_unit_dict = {'second': 60, 'minute': 60*60, 'hour': 24*60*60, 'day': 365*24*60*60}

    minutes, time_dict['second'] = divmod(seconds, 60)
    hours, time_dict['minute'] = divmod(minutes, 60)
    days, time_dict['hour'] = divmod(hours, 24)
    years, time_dict['day'] = divmod(days, 365)
    time_dict['year'] = years

    final_string_list = []
    value_counter = 0
    for time_unit, value in time_dict.items():
        if value > 0:
            value_counter += 1
            final_string_list.insert(0, f"{value} {time_unit}{'s' if value > 1 else ''}")

            if seconds > time_unit_dict.get(time_unit, math.inf):
                if value_counter == 1:
                    final_string_list.insert(0, " and ")
                else:
                    final_string_list.insert(0, ", ")

    return ''.join(final_string_list)


if __name__ == "__main__":
    print(format_duration(5))
    print(format_duration(65))
    print(format_duration(3660))
    print(format_duration(666666665))