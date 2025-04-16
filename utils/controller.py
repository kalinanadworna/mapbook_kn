def remove_user(users_data: list) -> None:
    user_name = input("podaj imie użytkownika do usunięcia: ")
    for user in users_data:
        if user["name"] == user_name:
            users_data.remove(user)
