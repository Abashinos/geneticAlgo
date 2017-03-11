from crossover import CROSSOVER_TYPES


class ArgumentCleaner:

    MESSAGES = {
        "board_size": ("Размер доски",
                       "Введите размер доски",
                       "от 4 до 30"),
        "initial_population": ("Начальная популяция",
                               "Введите размер начальной популяции",
                               "не меньше размера доски"),
        "max_population": ("Максимальный размер популяции",
                           "Введите максимальный размер популяции",
                           "<= 0 - не ограничен"),
        "generation_limit": ("Максимальное количество поколений",
                             "Введите максимальное количество поколений",
                             "<= 0 - не ограничено"),
        "mutation_chance": ("Шанс каждого гена мутировать на каждой итерации",
                            "Введите шанс каждого гена мутировать на каждой итерации",
                            "от 0 до 1"),
        "crossover_type": ("Тип алгоритма скрещивания",
                           "Введите название типа алгоритма скрещивания",
                           ", ".join(CROSSOVER_TYPES.keys())),
        "crossover_percent": ("Доля особей, участвующих в скрещивании",
                              "Введите долю особей, участвующих в скрещивании",
                              "от 0 до 1"),
        "selection_percent": ("Доля особей, переходящих в следующее поколение",
                              "Введите долю особей, переходящих в следующее поколение",
                              "от 0.01 до 1"),
        "verbose": ("Режим вывода информации",
                    "Выберите режим вывода (0 - циклический, 1 - пошаговый)",
                    "0 или 1"),
    }

    @staticmethod
    def get_full_message(key):
        full_message = ArgumentCleaner.MESSAGES.get(key)
        return "{msg} ({hint})\n".format(msg=full_message[1], hint=full_message[2]) if full_message else ""

    @staticmethod
    def clean_arg(name, required_type, predicate, value):
        while True:
            try:
                value = required_type(value)
            except (TypeError, ValueError):
                print("Параметр '{0}' имеет некорректный тип '{1}'. Требуется: '{2}'".format(name, type(value), required_type))
            else:
                if not predicate(value):
                    print("Параметр '{0}' не удовлетворяет условию '{1}'.".format(name, ArgumentCleaner.MESSAGES[name][2]))
                else:
                    break

            value = input(ArgumentCleaner.get_full_message(name))
        return value

    @staticmethod
    def clean_board_size(value):
        return ArgumentCleaner.clean_arg("board_size",
                                         int, lambda n: 3 < n < 31,
                                         value)

    @staticmethod
    def clean_initial_population(value, board_size):
        return ArgumentCleaner.clean_arg("initial_population",
                                         int, lambda n: n >= board_size,
                                         value)

    @staticmethod
    def clean_max_population(value):
        return ArgumentCleaner.clean_arg("max_population",
                                         int, lambda _: True,
                                         value)

    @staticmethod
    def clean_generation_limit(value):
        return ArgumentCleaner.clean_arg("generation_limit",
                                         int, lambda _: True,
                                         value)

    @staticmethod
    def clean_mutation_chance(value):
        return ArgumentCleaner.clean_arg("mutation_chance",
                                         float, lambda n: 0.0 <= n <= 1.0,
                                         value)

    @staticmethod
    def clean_crossover_type(value):
        return ArgumentCleaner.clean_arg("crossover_type",
                                         str, lambda n: n in CROSSOVER_TYPES.keys(),
                                         value)

    @staticmethod
    def clean_crossover_percent(value):
        return ArgumentCleaner.clean_arg("crossover_percent",
                                         float, lambda n: 0.0 <= n <= 1.0,
                                         value)

    @staticmethod
    def clean_selection_percent(value):
        return ArgumentCleaner.clean_arg("selection_percent",
                                         float, lambda n: 0.01 <= n <= 1.0,
                                         value)

    @staticmethod
    def clean_verbose(value):
        return ArgumentCleaner.clean_arg("verbose",
                                         int, lambda n: n in (0, 1),
                                         value)