def new_entry(user_name, user_path):
    def entry_type():
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
|    New Entry         |        [ 1. Incomes ]         [ 2. Expenses ]                                  |
|_______________________________________________________________________________________________________|

            """)

        try:
            entry_type = int(input("""    Please choose your entry type by number: """))

        except ValueError:
            print("""    
    Please choose the type using numbers!""")
            loading_bar(loading_duration)
            new_entry(user_name, user_path)
        if entry_type == 1:
            entry_type = "Incomes"
        elif entry_type == 2:
            entry_type = "Expenses"
        else:
            print("Please choose the correct entry type!")
            new_entry(user_name, user_path)
        return entry_type

    entry_type_ = entry_type()

    def entry(user_name, entry_type_, user_path):
        description = str(input(f"""    Enter the {entry_type_} description: """))
        while len(description) > 15:
            print("""    The description should be within 15 characters. Try again!""")
            entry(user_name, entry_type_, user_path)

        while True:
            try:
                amount = float(input("""    Enter the amount: """))
                if amount.is_integer() or amount == round(amount, 2):
                    break
                else:
                    print("    Please enter a valid float or integer.")
            except ValueError:
                print("    Please enter a valid float or integer.")

        print("""
    [ 1. January ]   [ 2. February ]   [ 3. March ]       [ 4. April ]      [ 5. May ]         [ 6. June ]

    [ 7. July ]      [ 8. August ]     [ 9. September ]   [ 10. October ]   [ 11. November ]   [ 12. December ]
""")
        months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        month = int(input("""    Choose the month by number: """))
        month_num = [1, 2 ,3, 4, 5, 6, 7, 8, 9, 10 ,11, 12]
        while month not in month_num:
            print("""    Please enter a correct number to choose the month. Try again!""")
            month = int(input("""    Choose the month by number: """))
        month = months[month]

        entry_data = f"{month},{description},{amount}\n"

        with open(f"{user_path}/Finance Section/{user_name}/{entry_type_}.txt", "a") as f:
            f.write(entry_data)

        print("""    Entry successfully added!""")

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

        loading_bar(loading_duration)

        from Home_UI import home_ui
        home_ui(user_name, user_path)

    entry(user_name, entry_type_, user_path)

