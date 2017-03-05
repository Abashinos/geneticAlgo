from arg_cleaner import ArgumentCleaner


class MainMenu:

    def __init__(self):
        self.sim_params = {}

    def get_choice(self, choice):
        return ({
            1: self.set_parameters,
            0: exit
        }).get(choice, self.error)

    def set_parameters(self):
        print("Введите параметры симуляции:")
        self.sim_params["board_size"] = ArgumentCleaner.clean_board_size(input("Введите размер доски (от 4 до 30)\n"))

    def error(self):
        print("Неверный выбор")

    def show(self):
        while True:
            try:
                self.get_choice(int(input("Добрый вечер\n")))()
            except TypeError:
                print("Неверный выбор")


if __name__ == "__main__":
    MainMenu().show()
