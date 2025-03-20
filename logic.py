import random
from decouple import Config, RepositoryIni

# Загружаем настройки из settings.ini
config = Config(RepositoryIni("settings.ini"))
MIN_NUMBER = int(config.get("GAME", "MIN_NUMBER"))
MAX_NUMBER = int(config.get("GAME", "MAX_NUMBER"))
ATTEMPTS = int(config.get("GAME", "ATTEMPTS"))
STARTING_BALANCE = int(config.get("GAME", "STARTING_BALANCE"))

def play_game():
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    balance = STARTING_BALANCE

    print(f"Добро пожаловать в игру! У вас {ATTEMPTS} попыток и стартовый баланс {balance}.")

    for attempt in range(ATTEMPTS):
        try:
            bet = int(input("Введите вашу ставку: "))
            if bet > balance:
                print("Недостаточно средств! Введите меньшую ставку.")
                continue

            guess = int(input(f"Угадайте число ({MIN_NUMBER}-{MAX_NUMBER}): "))

            if guess == secret_number:
                balance += bet
                print(f"Поздравляю! Вы угадали число {secret_number}. Ваш баланс: {balance}")
                return
            else:
                balance -= bet
                print(f"Неверно! Осталось {ATTEMPTS - attempt - 1} попыток. Ваш баланс: {balance}")

            if balance <= 0:
                print("Вы проиграли все деньги!")
                return
        except ValueError:
            print("Ошибка ввода! Введите число.")

    print(f"Игра окончена! Загаданное число было {secret_number}. Ваш итоговый баланс: {balance}")
