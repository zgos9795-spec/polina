def count_letters(input_text):  # TODO  Напишите функцию count_letters
    letter_counts = {}
    for character in input_text.lower():
        if character.isalpha():
            letter_counts[character] = 0
    for letter_key in letter_counts:
        for character in input_text.lower():
            if character.isalpha() and letter_key == character:
                letter_counts[letter_key] += 1
    return letter_counts


def calculate_frequency(letter_statistics):  # TODO Напишите функцию calculate_frequency
    sum_of_letters = 0
    for count_value in letter_statistics.values():
        sum_of_letters += count_value
    for letter_key, count_value in letter_statistics.items():
        letter_statistics.update({letter_key: count_value / sum_of_letters})
    return letter_statistics


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


for letter, frequency in calculate_frequency(count_letters(main_str)).items():  # TODO Распечатайте в столбик букву и её частоту в тексте
    print(f'{letter}: {frequency:.2f}')