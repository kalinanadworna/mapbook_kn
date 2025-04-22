users: list = [
    {"name":"Krzysztof","location":"Białobrzegi","posts":500},

]
print(users)


def add_user(users_data: list) ->None:
    user_name = input("podaj imie nowego użytkownika: ")
    user_location = input("podaj lokalizacje nowego znajomego: ")
    user_posts = int(input("podaj liczbe postów: "))
    users_data.append({"name": user_name, "location": user_location, "posts": user_posts})


add_user(users)

print(users)


print(users)