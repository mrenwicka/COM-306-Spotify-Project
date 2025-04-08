def createacct():
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Append new account to the file
    with open("account.txt", "a") as file:
        file.write(username + " " + password + "\n")
    print("Account created successfully.\n")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("account.txt", "r") as file:
        for line in file:
            stored_username, stored_password = line.strip().split()
            if username == stored_username and password == stored_password:
                print("Login successful!\n")
                user_session(username)
                return
    print("Login failed.\n")


def logout(username):
    print(f"User '{username}' has been logged out.\n")


def user_session(username):
    while True:
        print(f"Welcome, {username}!")
        print("1. Log out")
        choice = input("Choose an option: ")

        if choice == "1":
            logout(username)
            break
        else:
            print("Invalid option.\n")


# Basic menu to use the system
def main():
    while True:
        print("==== MENU ====")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            createacct()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    main()
