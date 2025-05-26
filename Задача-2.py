import random

def generate_geometric_progression(length):
    """Генерирует геометрическую прогрессию заданной длины."""
    start = random.randint(1, 10)  # Начальное значение
    ratio = random.randint(2, 5)    # Знаменатель (рацион)
    progression = [start * (ratio ** i) for i in range(length)]
    return progression

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    for _ in range(3):  # Задаем 3 вопроса
        length = random.randint(5, 10)  # Длина прогрессии от 5 до 10
        progression = generate_geometric_progression(length)

        missing_index = random.randint(0, length - 1)  # Случайная позиция для пропуска
        missing_value = progression[missing_index]
        progression[missing_index] = '..'  # Заменяем число на '..'

        print("Question:", ' '.join(map(str, progression)))
        user_answer = int(input("Your answer: "))

        if user_answer == missing_value:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{missing_value}'.")
            print(f"Let's try again, {name}!")
            return  # Завершаем игру при неправильном ответе

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()
