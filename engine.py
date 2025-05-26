MAX_ROUNDS = 3


def run_game(game):
    """
    Общая логика запуска игры:
    - Здоровается с игроком
    - Запускает раунды
    - Проверяет ответы
    - Поздравляет или завершает игру при ошибке
    """
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(game.GAME_RULES)

    for _ in range(MAX_ROUNDS):
        question, correct_answer = game.generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
