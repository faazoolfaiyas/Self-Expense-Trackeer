import os
from replit import clear
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def get_file_path(user_name, category, user_path):
    base_path = f"{user_path}/Finance Section/"
    return os.path.join(base_path, user_name, f"{category}.txt")

def calculate_data(data, selected_month):
    final_records = []
    total = 0

    for each in data:
        each_temp = each.split(",")
        temp_list = []

        if len(each_temp) >= 3 and each_temp[0] == selected_month:
            for temp_index in range(3):
                temp_list.append(each_temp[temp_index])

            total += float(each_temp[2])

            # Rearrange the order to print description first and then amount
            temp_list_f = [each_temp[1] + "     ->      " + each_temp[2]]
            temp_list = "".join(temp_list_f)
            final_records.append(temp_list)

    return final_records, total

def generate_pdf(content, filename, user_path, user_name):
    file_saving = f"{user_path}/Finance Section/{user_name}/{filename}"
    pdf_canvas = canvas.Canvas(file_saving, pagesize=letter)    
    pdf_canvas.setFont("Helvetica", 10)

    y_position = 750
    for line in content.split('\n'):
        pdf_canvas.drawString(100, y_position, line)
        y_position -= 8

    pdf_canvas.save()

def summary(user_name, user_path):
    clear()

    income_file_path = get_file_path(user_name, "incomes", user_path)
    expense_file_path = get_file_path(user_name, "expenses", user_path)

    try:
        with open(income_file_path, "r") as f:
            income_data = f.read().split("\n")

        with open(expense_file_path, "r") as f:
            expense_data = f.read().split("\n")
    except FileNotFoundError:
        print(f"Error: Files not found for user: {user_name}")
        from Home_UI import home_ui
        home_ui(user_name, user_path)

    print("""
    [ 1. January ]   [ 2. February ]   [ 3. March ]       [ 4. April ]      [ 5. May ]         [ 6. June ]

    [ 7. July ]      [ 8. August ]     [ 9. September ]   [ 10. October ]   [ 11. November ]   [ 12. December ]
""")

    months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    try:
        month = int(input("""    Which month summary do you want? (choose the month by number) : """))
        while month not in range(1, 13):
            print("""    Please enter a correct number to choose month. Try again!""")
            month = int(input("""    Choose the month by number: """))
    except ValueError:
        print("Invalid input. Please enter a number.")
        from Home_UI import home_ui
        home_ui(user_name, user_path)

    selected_month = months[month]
    clear()

    income = calculate_data(income_data, selected_month)
    expense = calculate_data(expense_data, selected_month)

    balance = income[1] - expense[1]
    final = []

    final.append(f""" _______________________________________________________________________________________________________
                                                                                                        
     Personal Finance Management System   |   Summary  -->  {user_name}                                    
 _______________________________________________________________________________________________________    
                                                                                                        
     Number        Description        Amount                                               
 _______________________________________________________________________________________________________
""")
    
    final.append(f"""
                    Incomes of the {selected_month}
 _______________________________________________________________________________________________________        
""")
    
    number = 1
    for i in income[0]:
        final.append(f"""
       {number}.            {i}
 _______________________________________________________________________________________________________
 """)
        number += 1

    final.append(f"""
                           Total      +{income[1]}
""")

    final.append(f""" _______________________________________________________________________________________________________        

                    Expenses of the {selected_month}
 _______________________________________________________________________________________________________        
""")

    number = 1
    for i in expense[0]:
        final.append(f"""
       {number}.            {i}
 _______________________________________________________________________________________________________
 """)
        number += 1

    final.append(f"""
                           Total      -{expense[1]}
""")
    
    final.append(f""" _______________________________________________________________________________________________________        

     Balancing of the {selected_month} -->    {balance}           
 _______________________________________________________________________________________________________        
""")
    
    final = "".join(final)
    clear()
    print(final)
    
    generate_pdf_input = input("Do you need a PDF file of the summary?  [ 1. Yes ] [ (any key). No ] : ")
    if generate_pdf_input == "1":
        file_name = user_name + f" summary of the {selected_month}.pdf"
        generate_pdf(final, file_name, user_path, user_name)
        print(f"PDF generated successfully: {file_name}")

    from Home_UI import home_ui
    home_ui(user_name, user_path)