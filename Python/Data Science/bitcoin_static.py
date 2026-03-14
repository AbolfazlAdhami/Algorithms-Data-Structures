def get_min_avg_max(discard, data):
    result = []
    total_values = []

    for array in data:
        filtered_array = array[discard:-
                               discard] if len(array) > 2 * discard else []

        if filtered_array:
            array_min = min(filtered_array)
            array_avg = sum(filtered_array) / len(filtered_array)
            array_max = max(filtered_array)

            result.append((array_min, array_avg, array_max))

            total_values.extend(filtered_array)
        else:

            result.append((None, None, None))

    if total_values:
        total_min = min(total_values)
        total_avg = sum(total_values) / len(total_values)
        total_max = max(total_values)
        result.append((total_min, total_avg, total_max))
    else:
        result.append((None, None, None))

    return result


data = [[800, 1200, 2100, 4100, 1300, 700], [
    1000, 1500, 4500, 5000, 5800, 2000, 1500]]

print(get_min_avg_max(len(data), data))
