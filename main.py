from utils.model import users
from utils.controller import get_user_info, add_users , remove_users, get_map, up

def main():
    while True:

        print("=================MENU===================")
        print("0 - zakończ program")
        print("1 - pokaż co u znajomych")
        print("2 - dodaj nowego znajomego")
        print("3 - usuń znajomego")
        print("4 - zaktualizuj dane znajomego")
        print("==========================================")
        print("5 - wygeneruj mapę znajomych")
        choice = input("wybierz opcje menu: ")
        if choice == "0": break
        if choice == "1": get_user_info(users)
        if choice == "2": add_users(users)
        if choice == "3": remove_users(users)
        if choice == "4": update_user(users)
        if choice == "5": get_map(users)


if __name__ == "__main__":
    main()
