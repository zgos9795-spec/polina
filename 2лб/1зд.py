months = 0
money_capital = 30000  # Подушка безопасности
salary = 7000  # Ежемесячная зарплата
spend = 8000  # Траты за первый месяц
increase = 0.03  # Ежемесячный рост цен

while money_capital + salary >= spend:
    spend += spend * increase
    money_capital -= spend - salary
    months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)