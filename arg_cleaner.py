

class ArgumentCleaner:

    @staticmethod
    def clean_arg(name, message, required_type, predicate, value):
        while True:
            if not issubclass(type(value), required_type):
                print("Параметр '{0}' имеет некорректный тип '{1}'. Требуется: '{2}'".format(name, type(value), required_type))
            elif not predicate(value):
                print("Параметр '{0}' не удовлетворяет условию '{1}'.".format(name, predicate))
            else:
                break

            value = input(message)
        return value

    @staticmethod
    def clean_board_size(value):
        return ArgumentCleaner.clean_arg("Размер доски", "Введите размер доски (от 4 до 30)",
                                         int, lambda n: 3 < n < 31,
                                         value)
