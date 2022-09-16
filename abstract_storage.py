from abc import ABC


class Storage(ABC):
    def __init__(self, items, capacity):
        self.items = items  # dict
        self.capacity = capacity  # int

    def add(self, title, quantity) -> None:
        # увеличивает запас items
        pass

    def remove(self, title, quantity) -> None:
        # уменьшает запас items
        pass

    def get_free_space(self) -> int:
        # вернуть количество свободных мест
        pass

    def get_items(self):
        # возвращает содержимое склада в словаре {товар: количество}
        pass

    def unique_items_count(self):
        # возвращает количество уникальных товаров.
        pass
