def find_common_participants(group1_members, group2_members, separator=","):  # TODO Напишите функцию find_common_participants
    members_list1 = group1_members.split(separator)
    members_list2 = group2_members.split(separator)
    common_names = []
    for _, participant1 in enumerate(members_list1):
        for _, participant2 in enumerate(members_list2):
            if participant1 == participant2:
                common_names.append(participant1)
    return sorted(common_names)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))# TODO Провеьте работу функции с разделителем отличным от запятой