from argcleaner import ArgumentCleaner
from solver import Solver


class MainMenu:

    def __init__(self):
        self.sim_params = {}

    def get_choice(self, choice):
        return ({
            1: self.set_parameters,
            2: self.run_sim,
            0: exit
        }).get(choice, self.error)

    def set_parameters(self):
        print("Введите параметры симуляции:")

        self.sim_params["board_size"] = ArgumentCleaner.clean_board_size(
            input(ArgumentCleaner.get_full_message("board_size"))
        )
        self.sim_params["initial_population"] = ArgumentCleaner.clean_initial_population(
            input(ArgumentCleaner.get_full_message("initial_population")),
            self.sim_params["board_size"]
        )
        self.sim_params["generation_limit"] = max(0, ArgumentCleaner.clean_generation_limit(
            input(ArgumentCleaner.get_full_message("generation_limit"))
        ))
        self.sim_params["mutation_chance"] = ArgumentCleaner.clean_mutation_chance(
            input(ArgumentCleaner.get_full_message("mutation_chance"))
        )
        self.sim_params["crossover_type"] = ArgumentCleaner.clean_crossover_type(
            input(ArgumentCleaner.get_full_message("crossover_type"))
        )
        self.sim_params["crossover_percent"] = ArgumentCleaner.clean_crossover_percent(
            input(ArgumentCleaner.get_full_message("crossover_percent"))
        )
        while True:
            choice = input("Введите 'm' для задания максимальной популяции или "
                           "'s' для задания доли особей, переходящих в следующее поколение:\n")
            if choice == 'm':
                self.sim_params["max_population"] = max(0, ArgumentCleaner.clean_max_population(
                    input(ArgumentCleaner.get_full_message("max_population"))
                ))
                break
            elif choice == 's':
                self.sim_params["selection_percent"] = ArgumentCleaner.clean_crossover_percent(
                    input(ArgumentCleaner.get_full_message("selection_percent"))
                )
                break
            else:
                print('Неверный ввод\n')

        self.sim_params["verbose"] = bool(ArgumentCleaner.clean_crossover_percent(
            input(ArgumentCleaner.get_full_message("verbose"))
        ))

        print(self.sim_params)

    def run_sim(self):
        if not self.sim_params:
            raise TypeError("Параметры симуляции не инициализированы")
        solver = Solver(self.sim_params)
        solver.run()

    def error(self):
        print("Неверный выбор")

    def show(self):
        while True:
            try:
                self.get_choice(int(input("Добрый вечер\n"
                                          "Введите выбор:\n"
                                          "1 - Задать параметры симуляции\n"
                                          "2 - Запустить симуляцию\n"
                                          "0 - Выйти\n")))()
            except (TypeError, ValueError) as e:
                print("Неверный выбор. Ошибка: \n{}".format(e))


if __name__ == "__main__":
    MainMenu().show()
