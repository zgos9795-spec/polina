participants_list = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

center_position = len(participants_list) // 2

team_a = participants_list[:center_position]
team_b = participants_list[center_position:]

print(team_a)
print(team_b)