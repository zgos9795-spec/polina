data_values = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
position = 0

while data_values[position] is not None:
    position += 1

total_sum = sum(data_values[:position]) + sum(data_values[position + 1:])
average_value = total_sum / len(data_values)
data_values[position] = average_value

print("Modified list:", data_values)