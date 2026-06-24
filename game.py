import random


def generate_number(min_val=-100, max_val=100):
    return random.randint(min_val, max_val)


def check_guess(secret, guess):
    if guess == secret:
        return "correct"
    elif guess > secret:
        return "too high"
    else:
        return "too low"


def play_game(secret, min_val, max_val, input_func=input, output_func=print):
    attempts = 0
    while True:
        raw = input_func().strip()
        try:
            guess = int(raw)
        except ValueError:
            output_func(f"Ошибка: введите целое число.")
            continue
        if guess < min_val or guess > max_val:
            output_func(f"Число должно быть от {min_val} до {max_val}.")
            continue
        attempts += 1
        output_func(f"Попытка №{attempts}")
        result = check_guess(secret, guess)
        if result == "correct":
            output_func(f"Поздравляем! Вы угадали число {secret} за {attempts} попыток!")
            return attempts
        elif result == "too high":
            output_func("Слишком много!")
        else:
            output_func("Слишком мало!")
