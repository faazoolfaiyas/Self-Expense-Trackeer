import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def expenses(user_name, user_path):
    expenses_file_path = f"{user_path}/Finance Section/{user_name}/expenses.txt"

    if not os.path.exists(expenses_file_path):
        print(f"Expenses file not found for user: {user_name}")
        from Home_UI import home_ui
        home_ui(user_name, user_path)

    with open(expenses_file_path, "r") as f:
        expense = f.read().split("\n")

    final_records = []
    total_expense = 0

    for each in expense:
        expense_temp = each.split(",")

        if len(expense_temp) >= 3:
            temp_list = [expense_temp[temp_index] for temp_index in range(3)]
            temp_list_f = [temp + "    ->     " if temp_num < 2 else temp for temp_num, temp in enumerate(temp_list)]
            temp_list = "".join(temp_list_f)
            final_records.append(temp_list)

            total_expense += float(expense_temp[2])

    final = []
    final.append(f""" _______________________________________________________________________________________________________
                                                                                                        
     Personal Finance Management System   |   Expenses  -->  {user_name}                                    
 _______________________________________________________________________________________________________    
                                                                                                        
     Number        Month        Description        Amount                                               
 _______________________________________________________________________________________________________        
""")
    number = 1
    for i in final_records:
        final.append(f"""
       {number}.         {i}
 _______________________________________________________________________________________________________
 """)
        number += 1

    final.append(f"""
                                        Total      {total_expense}""")
    final = "".join(final)
    print(final)

    generate_pdf_input = input("Do you need a PDF file of the expenses?  [ 1. Yes ] [ (any key). No ] : ")
    if generate_pdf_input == "1":
        file_name = user_name + " expenses.pdf"
        generate_pdf(final, file_name, user_path, user_name)
        print(f"PDF generated successfully: {file_name}")

    from Home_UI import home_ui
    home_ui(user_name, user_path)

def generate_pdf(content, filename, user_path, user_name):
    file_saving = f"{user_path}/Finance Section/{user_name}/{filename}"
    pdf_canvas = canvas.Canvas(file_saving, pagesize=letter)    
    pdf_canvas.setFont("Helvetica", 10)

    y_position = 750
    for line in content.split('\n'):
        pdf_canvas.drawString(100, y_position, line)
        y_position -= 8

    pdf_canvas.save()
