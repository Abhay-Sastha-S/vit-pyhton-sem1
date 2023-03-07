import tkinter as tk
from tkinter import messagebox
from selenium import webdriver

# create the main window
root = tk.Tk()
root.title("Order Status")
root.configure(bg="#f9f2ea")
root.geometry("500x500")


# define a function to prompt the user for their phone number
def get_phone_number(button_number):
    phone_number = tk.StringVar()
    prompt_window = tk.Toplevel(root)
    prompt_window.title("Phone Number")
    prompt_window.configure(bg='#f9f2ea')  # set background color
    prompt_window.geometry('250x150')  # set window size
    prompt_label = tk.Label(prompt_window, text=f"{button_number} for Phone Number:", font=("Arial", 14), bg='#f9f2ea')  # increase font size and set background color
    prompt_entry = tk.Entry(prompt_window, textvariable=phone_number, font=("Arial", 12))
    prompt_button = tk.Button(prompt_window, text="OK", font=("Arial", 12), command=lambda: prompt_window.destroy())
    prompt_label.pack(pady=10)
    prompt_entry.pack(pady=10)
    prompt_button.pack(pady=10)
    prompt_window.grab_set()
    prompt_window.wait_window()
    if len(phone_number.get()) != 10 or not phone_number.get().isdigit():
        messagebox.showerror("Phone Number", "Invalid phone number!")
        return get_phone_number()  # call function recursively to prompt user again
    else:
        return phone_number.get()


# define a function to create the message to be displayed in the message box
def text(phone_number, button_number):

    link_final = "http://bulkmessaging.in:1111/mspProducerM/sendSMS?user=Boltz_TreeV&pwd=Trees2018&sender=TREEST&mobile="

    # order ready
    link1 = "&msg=Dear Customer, Your order is ready and you can pick up at your convenience. Thanks keep supporting dc. TREES&mt=0"
    # order accepted
    link2 = "&msg=Dear Customer, Thanks for placing orders with dc. Your order has been accepted and will be ready on time. TREES.&mt=0"
    # in stock
    link3 = "&msg=Dear Customer, We are ready now, you can place your orders now.Trees&mt=0"
    # out of stock
    link4 = "&msg=Dear Customer, Sorry we cannot process your order at present. We shall get back to you once we are ready. TREES&mt=0"

    link_select = ""

    if button_number == 1:
        link_select = link2
    elif button_number == 2:
        link_select = link4
    elif button_number == 3:
        link_select = link3
    elif button_number == 4:
        link_select = link1

    link_final += phone_number + link_select

    driver = webdriver.Chrome()
    driver.get(link_final)
    driver.close()

# define a function to save the phone number and button clicked as variables and display the message box
def save_phone_number(button_number):
    phone_number = get_phone_number(button_number)
    if phone_number:
        message = text(phone_number, button_number)
        messagebox.showinfo("Order Status", message)
        # here you can save the phone number and button clicked as variables or use them for further processing
        print(f"Order status: {button_number}")
        print(f"Phone number: {phone_number}")

    else:
        messagebox.showwarning("Phone Number", "You did not enter a phone number.")

# create the buttons with assigned numbers
accept_button = tk.Button(root, text="1. ACCEPT", height=2, width=20, activebackground='#808080', background="white", command=lambda: save_phone_number(1))
accept_button.place(x=650, y=550)
cancel_button = tk.Button(root, text="2. CANCEL", height=2, width=20, activebackground='#808080', background="white", command=lambda: save_phone_number(2))
cancel_button.place(x=700, y=620)
in_stock_button = tk.Button(root, text="3. IN STOCK", height=2, width=20, activebackground='#808080', background="white", command=lambda: save_phone_number(3))
in_stock_button.place(x=750, y=690)
order_ready_button = tk.Button(root, text="4. ORDER READY", height=2, width=20, activebackground='#808080', background="white", command=lambda: save_phone_number(4))
order_ready_button.place(x=800, y=760)
# place the buttons in the window
accept_button.pack()
cancel_button.pack()
in_stock_button.pack()
order_ready_button.pack()

# start the main event loop
root.mainloop()
