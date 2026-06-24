from game import generate_number, play_game
from database import init_db, save_record, get_top_records

MIN_VAL = -100
MAX_VAL = 100


def show_menu():
    print("\n=== Угадай число ===")
    print("1. Новая игра")
    print("2. Таблица лидеров")
    print("3. Выход")
    return input("Выберите действие: ").strip()


def show_leaderboard():
    records = get_top_records(10)
    if not records:
        print("\nТаблица лидеров пуста!")
        return
    print("\n=== ТОП-10 лучших результатов ===")
    print(f"{'#':<4} {'Ник':<15} {'Попытки':<8} {'Дата':<20}")
    print("-" * 50)
    for i, rec in enumerate(records, 1):
        nick = rec[1][:15] + "…" if len(rec[1]) > 15 else rec[1]
        print(f"{i:<4} {nick:<15} {rec[2]:<8} {rec[3]}")


def new_game():
    secret = generate_number(MIN_VAL, MAX_VAL)
    print(f"\nЯ загадал число от {MIN_VAL} до {MAX_VAL}. Угадай его!")
    attempts = play_game(secret, MIN_VAL, MAX_VAL)
    nickname = input("Введите ваш ник: ").strip()
    if not nickname:
        nickname = "Anonymous"
    save_record(nickname, attempts)
    print(f"Результат сохранён! {attempts} попыток.")


def main():
    init_db()
    while True:
        choice = show_menu()
        if choice == "1":
            new_game()
        elif choice == "2":
            show_leaderboard()
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
