import random
from decouple import Config, RepositoryIni

config = Config(RepositoryIni("settings.ini"))
MIN_NUMBER = int(config.get("GAME", "MIN_NUMBER"))
MAX_NUMBER = int(config.get("GAME", "MAX_NUMBER"))
ATTEMPTS = int(config.get("GAME", "ATTEMPTS"))
STARTING_BALANCE = int(config.get("GAME", "STARTING_BALANCE"))

def play_game():
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    balance = STARTING_BALANCE

    print(f"у вас {ATTEMPTS} попыток и стартовый баланс {balance}.")

    for attempt in range(ATTEMPTS):
        try:
            bet = int(input("введите вашу ставку: "))
            if bet > balance:
                print("недостаточно средств!")
                continue

            guess = int(input(f"угадайте число ({MIN_NUMBER}-{MAX_NUMBER}): "))

            if guess == secret_number:
                balance += bet
                print(f"вы угадали число {secret_number}. ваш баланс: {balance}")
                return
            else:
                balance -= bet
                print(f"осталось {ATTEMPTS - attempt - 1} попыток. ваш баланс: {balance}")

            if balance <= 0:
                print("вы проиграли все деньги!")
                return
        except ValueError:
            print("введите число.")

    print(f"игра окончена! загаданное число было {secret_number}. ваш итоговый баланс: {balance}")
