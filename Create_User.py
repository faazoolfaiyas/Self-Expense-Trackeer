import os
import getpass
import hashlib
from replit import clear

def create_user(user_path):
    clear()

    print(""" _______________________________________________________________________________________________________
|                                                                                                       |
|    Personal Finance Management System | Create User                                                   |
|_______________________________________________________________________________________________________|      


    """)

    # Check if the users file exists; create it if not
    users_file_path = f"{user_path}/User Section/users.txt"
    if not os.path.exists(users_file_path):
        open(users_file_path, 'a').close()

    with open(users_file_path, "r") as users_file:
        users = users_file.read().split(",")

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

    user_name = str(input("""    Enter your user name: """))

    if user_name == "":
        print("""    You haven't entered anything!""")
        loading_bar(loading_duration)
        from Home import home
        home(user_path)

    if user_name in users:
        print(f"""   Your user name {user_name} is already exist! try to log-in.""")

    else:
        password = getpass.getpass("""    Enter your user password(It will be invisible): """)

        # Hash the password using SHA-256
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        with open(users_file_path, "a") as users_file:
            users_file.write(user_name + ",")

        passes_file_path = f"{user_path}/User Section/passes.txt"
        with open(passes_file_path, "a") as passes_file:
            passes_file.write(hashed_password + ",")

        characters = 0
        while characters != 6:
            verify = getpass.getpass("""    Enter a six characters text for the verification! (Don't forget this, then you can't recover your account)(Invisibled!): """)
            characters = len(verify)

        # Hash the verification code using SHA-256
        hashed_verify = hashlib.sha256(verify.encode()).hexdigest()

        verify_file_path = f"{user_path}/User Section/verify.txt"
        with open(verify_file_path, "a") as verify_file:
            verify_file.write(hashed_verify + ",")

        finance_section_path = f"{user_path}/Finance Section/{user_name}"
        os.mkdir(finance_section_path)

        income_file_path = f"{finance_section_path}/incomes.txt"
        open(income_file_path, 'w').close()

        expense_file_path = f"{finance_section_path}/expenses.txt"
        open(expense_file_path, 'w').close()

        print(f"""    Your user {user_name} is successfully created!""")

    loading_bar(loading_duration)

    from Login import login
    login(user_path)