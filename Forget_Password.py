import os
from replit import clear
import getpass
import hashlib

def load_user_data(user_path):
    users_file_path = f"{user_path}/User Section/users.txt"
    passes_file_path = f"{user_path}/User Section/passes.txt"
    verify_file_path = f"{user_path}/User Section/verify.txt"

    # Check if the files exist
    for file_path in [users_file_path, passes_file_path, verify_file_path]:
        if not os.path.exists(file_path):
            open(file_path, 'a').close()

    with open(users_file_path, "r") as users_file:
        users = users_file.read().split(",")

    with open(passes_file_path, "r") as passes_file:
        passes = passes_file.read().split(",")

    with open(verify_file_path, "r") as verify_file:
        verify = verify_file.read().split(",")

    return users, passes, verify

def encrypt_password(password):
    # Hash the password using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

def encrypt_verification(verification):
    # Hash the verification code using SHA-256
    return hashlib.sha256(verification.encode()).hexdigest()

def loading_bar(duration):
    import time
    iterations = 3  # Number of loading stages
    for _ in range(iterations):
        for i in range(3):
            print("""\r   Loading""" + "." * i, end="", flush=True)
            time.sleep(duration / (3 * iterations))
    print("""\r    Loading...""", "Loading complete!", flush=True)

def forget_password(user_path):
    clear()

    print(""" _______________________________________________________________________________________________________
|                                                                                                       |
|    Personal Finance Management System | Forget Password                                               |
|_______________________________________________________________________________________________________|      


""")

    users, passes, verify = load_user_data(user_path)

    loading_duration = 1.4

    try:
        user_name = str(input("""    Enter your user name: """))
        user_index = 0

        if user_name == "":
            print("""   You haven't entered anything!""")
            loading_bar(loading_duration)
            from Home import home
            home(user_path)

        if user_name in users:
            user_index = users.index(user_name)
            verification = getpass.getpass("""    Enter your verification text (It will be invisible): """)

            # Encrypt the verification code
            encrypted_verification = encrypt_verification(verification)

            if verify[user_index] == encrypted_verification:
                new_password = getpass.getpass("""    Enter your new user password (It will be invisible): """)
                encrypted_password = encrypt_password(new_password)
                passes[user_index] = encrypted_password

                # Write the encrypted passwords back to the file
                with open(f"{user_path}/User Section/passes.txt", "w") as passes_file:
                    passes_file.write(','.join(passes))

                print("""    Your password is successfully changed!""")

            else:
                print("""    Incorrect verification code! Please try again.""")
        else:
            print("""    Can't find the user! If you'd like to create a user, go to home... and try again!""")
            
    except IndexError:
        print("Something went wrong. Try again!")

    loading_bar(loading_duration)

    from Home import home
    home(user_path)

