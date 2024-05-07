# Pinnacle Lab
# Task 3 - Password Analyzer

import tkinter as tk
from tkinter import messagebox
import re

class PasswordStrengthEvaluator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Evaluator")

        self.create_widgets()

    def create_widgets(self):
        self.password_label = tk.Label(self.root, text="Enter Password:")
        self.password_label.grid(row=0, column=0, padx=10, pady=10)

        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=0, column=1, padx=10, pady=10)  # Grid password_entry here

        self.evaluate_button = tk.Button(self.root, text="Evaluate", command=self.evaluate_password)
        self.evaluate_button.grid(row=1, columnspan=2, padx=10, pady=10)  # Then grid evaluate_button

        self.result_text = tk.Text(self.root, height=4, width=40, wrap="word")
        self.result_text.grid(row=2, columnspan=2, padx=10, pady=10)
    
    def evaluate_password(self):
        password = self.password_entry.get()
        result = self.evaluate_strength(password)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

    def evaluate_strength(self, password):
        if len(password) < 8:
            return "Password is too short. Please use at least 8 characters."
        elif not re.search(r'\d', password):
            return "Password should contain at least one digit."
        elif not re.search(r'[a-zA-Z]', password):
            return "Password should contain at least one letter."
        elif not re.search(r'[!@#%^&(),.?":{}|<>]', password):
            return "Password should contain at least one special character."
        else:
            return "Password strength is good!"

def main():
    root = tk.Tk()
    app = PasswordStrengthEvaluator(root)
    root.mainloop()

if __name__ == "__main__":
    main()                        