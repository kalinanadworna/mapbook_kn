def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user['name']}! z miejscowości {user['location']} opublikował {user['posts']} postów")


def add_users(users_data: list) -> None:
    users_name: str = input("podaj imię nowego użytkownika: ")
    users_location: str = input("podaj lokalizacje nowego znajomego: ")
    users_posts: str = (input("podaj liczbę postów: "))
    users_data.append({"name": users_name, "location": users_location, "posts": users_posts})


def remove_users(users_data: list) -> None:
    user_name: str = input("podaj imię użytkownika do usunięcia;")
    for user in users_data:
        if user["name"] == user_name:
            users_data.remove(user)


def update_user(users_data: list) -> None:
    user_name = input("podaj imię użytkownika którego dane chcesz zaktualizować")
    for user in users_data:
        if user["name"] == user_name:
            user["name"] = input("podaj nowe imię użytkownika: ")
            user["location"] = input("podaj nową lokalizacje użytkownika: ")
            user["posts"] = int(input("podaj nową liczbę postów użytkownika: "))
