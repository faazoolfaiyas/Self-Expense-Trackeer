import hashlib
from replit import clear
import getpass

def load_users_and_hashes(user_path):
    users_file_path = f"{user_path}/User Section/users.txt"
    passes_file_path = f"{user_path}/User Section/passes.txt"

    with open(users_file_path, "r") as users_file:
        users = users_file.read().split(",")

    with open(passes_file_path, "r") as passes_file:
        hashes = passes_file.read().split(",")

    return users, hashes

def login(user_path):
    clear()

    print(""" _______________________________________________________________________________________________________
|                                                                                                       |
|    Personal Finance Management System | Login User                                                    |
|_______________________________________________________________________________________________________|      


    """)

    users, hashes = load_users_and_hashes(user_path)

    def loading_bar(duration):
        import time
        iterations = 3  # Number of loading stages
        for _ in range(iterations):
            for i in range(3):
                print("""\r   Loading""" + "." * i, end="", flush=True)
                time.sleep(duration / (3 * iterations))
        print("""\r    Loading...""", "Loading complete!", flush=True)

    # Set the duration for the loading bar in seconds (3 seconds in this example)
    loading_duration = 1.4

    exit_login = False
    while not exit_login:
        try:
            user_name = str(input("""    Enter your user name: """))
            user_index = 0

            if user_name == "":
                print("""    You haven't entered anything!""")
                loading_bar(loading_duration)
                from Home import home
                home(user_path)

            if user_name in users:
                user_index = users.index(user_name)
                entered_password = getpass.getpass("""    Enter your user password(It will be invisible): """)

                # Hash the entered password using SHA-256
                entered_password_hash = hashlib.sha256(entered_password.encode()).hexdigest()

                if entered_password_hash == hashes[user_index]:
                    print("""    Logged in successfully!
                        """)

                    loading_bar(loading_duration)

                    from Home_UI import home_ui
                    home_ui(user_name, user_path)

                    # Exit the login loop
                    exit_login = True

                else:
                    print("""    Wrong password! Try again or forget password!""")

            else:
                print("""    Can't find the user! If you'd like to create a user, go to home... and try again!""")

        except IndexError:
            print("   Something went wrong. Try again!")

        loading_bar(loading_duration)

        from Home import home
        home(user_path)
