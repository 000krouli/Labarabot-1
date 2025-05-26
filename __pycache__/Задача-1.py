import random
import math

def lcm(a, b):
    """Функция для вычисления наименьшего общего кратного (НОК)"""
    return abs(a * b) // math.gcd(a, b)

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")

    for _ in range(3):  # Задаем 3 вопроса
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        correct_answer = lcm(num1, num2)

        print(f"Question: {num1} {num2}")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Завершаем игру при неправильном ответе

    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()