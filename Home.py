def home(user_path):
    from replit import clear
    import time

    clear()
    print(""" _______________________________________________________________________________________________________
|                                                                                                       |
|    Personal Finance Management System | Warmly Welcome...                                             |
|_______________________________________________________________________________________________________|      
|                                                                                                       |
|   [ 1. Login User ]     [ 2. Create User ]    [ 3. Forget Password ]    [ 4. Remove User ]            |
|                                                                                                       |
|_______________________________________________________________________________________________________|

        """)

    def loading_bar(duration):
        iterations = 3  # Number of loading stages
        for _ in range(iterations):
            for i in range(3):
                print("""\r    Loading""" + "." * i, end="", flush=True)
                time.sleep(duration / (3 * iterations))
        print("""\r    Loading...""", "Loading complete!", flush=True)

    # Set the duration for the loading bar in seconds (3 seconds in this example)
    loading_duration = 1.4

    try:
        choice = int(input("    Enter your choice using number: "))
        print("""
    """)

        if choice == 1:
            # Call the loading_bar function with the specified duration
            loading_bar(loading_duration)
            from Login import login
            login(user_path)

        elif choice == 2:
            # Call the loading_bar function with the specified duration
            loading_bar(loading_duration)
            from Create_User import create_user
            create_user(user_path)

        elif choice == 3:
            # Call the loading_bar function with the specified duration
            loading_bar(loading_duration)
            from Forget_Password import forget_password
            forget_password(user_path)

        elif choice == 4:
            # Call the loading_bar function with the specified duration
            loading_bar(loading_duration)
            from Remove_User import remove_user
            remove_user(user_path)
            
        else:
            print("""   Your number is not in the choice. Please try again...""")

    except ValueError:
        print("""   Please enter a number to choose an option. Please try again...""")

# Introduce a mechanism to exit the loop
exit = False
from Path import user_path
while not exit:
    home(user_path)
    exit_choice = input("Do you want to exit? (yes/no): ").lower()
    if exit_choice == "yes":
        exit = True
