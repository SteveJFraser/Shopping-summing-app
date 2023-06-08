import tkinter as tk
from database import add_num, get_num, delete_data


def get_items(*args):
    try:
        number = float(item_input.get())
        add_num(number)
        x = []
        new_num = get_num()
        for data in new_num:
            for y in data:
                x.append(float(y))
        output_display.set(f"Total Bill ${sum(x):.2f}")
        item_input.set('')
    except ValueError:
        output_display.set('No Data')


def clear_data():
    delete_data()
    output_display.set('Data Cleared')


root = tk.Tk()
root.config(background="#171e2e")
root.geometry("300x300")
root.title("Shopping Calculator")
# item price label and entry ----------------------------------------------------
item_price_label = tk.Label(root, text="Item Price Entry: ",
                            width=21, font=("Arial", 18), background="purple")
item_price_label.pack()
# item input -----------------
item_input = tk.StringVar()
item_price = tk.Entry(root, width=20, background="#255e2e", 
                      font=("Arial", 15), textvariable=item_input)
item_price.pack(ipady=10)
item_price.focus()
# item display ---------------
output_display = tk.StringVar()
view_items = tk.Label(root, textvariable=output_display,
                      font=("Arial", 15), background="black", 
                      foreground="chartreuse", width=20, height=4)
view_items.pack()
# delete button --------------
delete_btn = tk.Button(root, text="Clear All", width=20,
                       height=1, font=("Arial", 14), 
                       command=clear_data, background="purple")
delete_btn.pack()
quit_btn = tk.Button(root, text="QUIT", width=20, height=1,
                                font=("Arial", 14), 
                                command=root.destroy, background="purple")
quit_btn.pack()
root.bind("<Return>", get_items)
root.mainloop()
