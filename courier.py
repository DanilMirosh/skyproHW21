from abstract_storage import Storage
from request import Request


class Courier:

    def __init__(self, request: Request, storages: dict[str, Storage]):
        self.__request = request

        if self.__request.departure in storages:
            self.__from = storages[self.__request.departure]

        if self.__request.destination in storages:
            self.__to = storages[self.__request.destination]

    def move(self):
        self.__from.remove(title=self.__request.product, quantity=self.__request.quantity)
        print(f'Курьер забрал {self.__request.quantity} {self.__request.product} из {self.__request.departure}')
        self.__to.add(title=self.__request.product, quantity=self.__request.quantity)
        print(f'Курьер доставил {self.__request.quantity} {self.__request.product} в {self.__request.destination}')


