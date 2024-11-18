current_users = ['jack', 'DASHA', 'Max', 'Olga', 'admin']
new_users = ["pat", "pawat", "Jack", "MAX", "Adil"]

current_users_lower = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}, you will need to enter a new username")
    else:
        print(f'The username {new_user} is available.')