import os
import shutil
from replit import clear
import getpass
import hashlib

def load_user_data(user_path):
    base_path = f"{user_path}/User Section/"
    users_file_path = os.path.join(base_path, "users.txt")
    passes_file_path = os.path.join(base_path, "passes.txt")
    verify_file_path = os.path.join(base_path, "verify.txt")

    with open(users_file_path, "r") as users_file:
        users = users_file.read().split(",")

    with open(passes_file_path, "r") as passes_file:
        passes = passes_file.read().split(",")

    with open(verify_file_path, "r") as verify_file:
        verify = verify_file.read().split(",")

    return users, passes, verify

def encrypt_password(verification):
    # Verification before hashing using SHA-256
    return hashlib.sha256(verification.encode()).hexdigest()

def loading_bar(duration):
    import time
    iterations = 3  # Number of loading stages
    for _ in range(iterations):
        for i in range(3):
            print("""\r   Loading""" + "." * i, end="", flush=True)
            time.sleep(duration / (3 * iterations))
    print("""\r    Loading...""", "Loading complete!", flush=True)

def remove_user(user_path):
    clear()

    print(""" _______________________________________________________________________________________________________
|                                                                                                       |
|    Personal Finance Management System | Remove User                                                   |
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

            # Add encryption to the verification code
            encrypted_verification = encrypt_password(verification)

            if verify[user_index] == encrypted_verification:
                del users[user_index]
                del passes[user_index]
                del verify[user_index]

                user = ','.join(users)
                password = ','.join(passes)
                verification_join = ','.join(verify)

                base_path = f"{user_path}/User Section/"
                with open(os.path.join(base_path, "users.txt"), "w") as f:
                    f.write(user)

                with open(os.path.join(base_path, "passes.txt"), "w") as f:
                    f.write(password)

                with open(os.path.join(base_path, "verify.txt"), "w") as f:
                    f.write(verification_join)

                base_path = user_path
                user_dir_path = os.path.join(base_path, f"Finance Section/{user_name}")

                try:
                    # Use shutil.rmtree to force remove the non-empty directory
                    shutil.rmtree(user_dir_path)
                except OSError as e:
                    print(f"Failed to remove user directory: {e}")

                print(f"""    Your user {user_name} is successfully removed!""")

            else:
                print("""    Your verification text is wrong. Please try again!""")

        else:
            print("""    Can't find the user! If you'd like to create a user, go to home... and try again!""")

    except IndexError:
        print("Something went wrong. Try again!")

    loading_bar(loading_duration)

    from Home import home
    home(user_path)
