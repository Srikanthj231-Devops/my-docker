# store_user_info.py

def store_user_info():
    name = input("Enter your name: ").strip()
    if name:
        with open("userinfo.txt", "a") as file:
            file.write(name + "\n")
        print(f"Name '{name}' has been saved.")
    else:
        print("No name entered. Nothing was saved.")

def display_users():
    try:
        with open("userinfo.txt", "r") as file:
            users = file.readlines()
            if users:
                print("\nUsers in the file:")
                for idx, user in enumerate(users, 1):
                    print(f"{idx}. {user.strip()}")
            else:
                print("No users found in the file.")
    except FileNotFoundError:
        print("No user info file found.")

if __name__ == "__main__":
    store_user_info()

    show = input("Do you want to display all users? (yes/no): ").strip().lower()
    if show in ["yes", "y"]:
        display_users()
    else:
        print("Okay, not displaying the users.")
