from cardHolder import cardHolder as ch
import tkinter as tk
from tkinter import messagebox, simpledialog


class Atmm:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM System")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.list_card_holders = [
            ch("100001", "1001", "Ram","G", 20000),
            ch("100002", "1002", "Venkat","K", 26000),
            ch("100003", "1003", "Prem","L", 6000),
            ch("100004", "1004", "Krish","J", 12000),
            ch("100005", "1005", "Datta","G", 45000),
            ch("100006", "1006", "Ravan","L", 500),
    
        ]
      
        self.current_user = None

        self.login_screen()
    
    def login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Enter Card Number", font=("Arial", 14)).pack(pady=10)
        self.card_var = tk.StringVar()
        self.card_entry = tk.Entry(self.root, textvariable=self.card_var, font=("Arial", 14))
        self.card_entry.pack(pady=5)

        tk.Label(self.root, text="Enter PIN", font=("Arial", 14)).pack(pady=10)
        self.pin_var = tk.StringVar()
        self.pin_entry = tk.Entry(self.root, textvariable=self.pin_var, font=("Arial", 14), show="*")
        self.pin_entry.pack(pady=5)

        

        tk.Button(self.root, text="Login", command=self.authenticate, font=("Arial", 12), width=10).pack(pady=10)
        
    
 

    def authenticate(self):
        cardnum = self.card_var.get()
        pin = self.pin_var.get()

        user_found = None
        for user in self.list_card_holders:
            if user.get_cardNumb() == cardnum:
                user_found = user
                break

        if user_found and user_found.get_pin() == pin:
            self.current_user = user_found
            self.main_menu()
        else:
            messagebox.showerror("Error", "Invalid Card Number or PIN!")

    def main_menu(self):
        self.clear_screen()

        tk.Label(self.root, text="ATM Menu", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text = "Hello: {}".format(self.current_user.get_firstname()),font=("Arial", 12),fg="green", width=20).pack(pady=5)
        tk.Button(self.root, text="Check Balance", command=self.check_balance, font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(self.root, text="Deposit Money", command=self.deposit, font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(self.root, text="Withdraw Money", command=self.withdraw, font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(self.root, text="Change PIN", command=self.change_pin, font=("Arial", 12), width=20).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.logout, font=("Arial", 12), width=20, fg="red").pack(pady=10)

    def deposit(self):
        try:
            deposit = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
            self.current_user.set_balance(self.current_user.get_balance() + deposit)
            messagebox.showinfo("Thank You, Your new balnce", str(self.current_user.get_balance()))
        except:
            messagebox.showerror("Invalid Input")

    def withdraw(self):
        try:
            withdraw = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
            if(withdraw <= self.current_user.get_balance()):
                self.current_user.set_balance(self.current_user.get_balance() - withdraw)
                messagebox.showinfo("Succes, Thank you")
            else:
                messagebox.showinfo("Insufficient Balance")
        except:
            messagebox.showerror("Invalid Input")

   
   
    def check_balance(self):
        messagebox.showinfo("Your Balance", self.current_user.get_balance())

    
    
    def change_pin(self):
        try:
            newpin = simpledialog.askstring("Change PIN", "Enter new 4-digit PIN:")
            self.current_user.set_pin(newpin)
            messagebox.showinfo("Succesfully changed your PIN")
        except:
            messagebox.showerror("invalid PIN")
    
    
    def logout(self):
        self.current_user = None
        messagebox.showinfo("Logout", "Logged out successfully!")
        self.login_screen()

    
    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    atm_app = Atmm(root)
    root.mainloop()



            