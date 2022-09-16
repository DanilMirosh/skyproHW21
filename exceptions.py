class BaseError(Exception):
    message = 'Неожиданная ошибка'


class NotEnoughSpace(BaseError):
    message = 'Недостаточно места на складе'


class NotEnoughProduct(BaseError):
    message = 'Недостаточно товара на складе'


class TooManyDifferentProducts(BaseError):
    message = 'Слишком много товаров'


class InvalidRequest(BaseError):
    message = 'Неправильный запрос. Попробуйте снова'


class InvalidStorageName(BaseError):
    message = 'Введен не существующий склад'
