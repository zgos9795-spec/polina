def find_product_index(product_catalog, target_product):  # TODO Напишите функцию для поиска индекса товара
    for position, product in enumerate(product_catalog):
        if product == target_product:
            return position
    return None

product_catalog = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for target_product in ['банан', 'груша', 'персик']:
    product_position = find_product_index(product_catalog, target_product)  # TODO Вызовите функцию, что получить индекс товара
    if product_position is not None:
        print(f"Первое вхождение товара '{target_product}' имеет индекс {product_position}.")
    else:
        print(f"Товар '{target_product}' не найден в списке.")