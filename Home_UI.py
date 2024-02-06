def home_ui(user_name,user_path):
    from replit import clear

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

    clear()
    print(f""" _______________________________________________________________________________________________________
|                                                                                                       |
|    Personal Finance Management System | Warmly Welcome {user_name}                                            |
|_______________________________________________________________________________________________________|      
|                                                                                                       |
|   [ 1. New Entry ]     [ 2. Incomes ]    [ 3. Expenses ]    [ 4. Summery ]    [ 5. Logout ]           |
|                                                                                                       |
|_______________________________________________________________________________________________________|

        """)
    
    try:
        choice = int(input("    Enter your choice using number: "))
        print("""
    """)

        if choice == 1:
            from New_Entry import new_entry
            new_entry(user_name, user_path)

        elif choice == 2:
            from Incomes import incomes
            incomes(user_name, user_path)

        elif choice == 3:
            from Expenses import expenses
            expenses(user_name, user_path)

        elif choice == 4:
            from Summary import summary
            summary(user_name, user_path)
            
        elif choice == 5:
            print("""    Your user has been successfully logged out!""")
            loading_bar(loading_duration)
            from Home import home
            home(user_path)

        else:
            print("""   Your number is not in the choice. Please try again...""")
            from Home_UI import home_ui
            home_ui(user_name, user_path)

    except ValueError:
        print("""   Please enter a number to choose an option. Please try again...""")
        from Home_UI import home_ui
        home_ui(user_name, user_path)