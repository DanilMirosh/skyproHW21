from courier import Courier
from exceptions import BaseError
from request import Request
from shop import Shop
from store import Store

store = Store(items={
    "печенька": 25,
    "собачка": 25,
    "ёлка": 25
})

shop = Shop(items={
    "печенька": 2,
    "собачка": 2,
    "ёлка": 2
})

storages = {
    "магазин": shop,
    "склад": store
}


def main():
    print('\nДобрый день\n')

    while True:

        # Вывести все товары во всех хранилищах
        for storage_title in storages:
            print(f"В {storage_title} храниться: \n "
                  f"({storages[storage_title].get_items()})")




        # забрать у пользователя строку с запросом
        user_input = input(
            'Ввидите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
            'Ввидите "стоп" или "stop", если хотите закончить:\n'
        )
        if user_input in ('stop', 'стоп'):
            break

        # собрать класс запросов
        try:
            request = Request(request=user_input, storages=storages)
        except BaseError as e:
            print(e.message)
            continue

        # обработать доставку если запрос валиден
        courier = Courier(
            request=request,
            storages=storages
        )

        try:
            courier.move()
        except BaseError as e:
            print(e.message)


if __name__ == '__main__':
    main()
