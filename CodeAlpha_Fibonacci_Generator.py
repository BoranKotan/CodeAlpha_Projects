import customtkinter as ctk
from tkinter import messagebox

def fibonacci(n: int):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def generate_fibonacci():
    try:
        num = int(entry.get())
        if num < 0:
            raise ValueError("Number can't be negative.")
        sequence = fibonacci(num)
        result_label.configure(text=f"Fibonacci Sequence: {sequence}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Please enter a valid number.\nError: {e}")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Fibonacci Generator")
root.geometry("500x300")

label = ctk.CTkLabel(root, text="Enter Fibonacci Sequence Length:")
label.pack(padx=20, pady=20)

entry = ctk.CTkEntry(root, width=200)
entry.pack(padx=10, pady=10)

generate_button = ctk.CTkButton(root, text="Generate a Fibonacci Sequence", command=generate_fibonacci)
generate_button.pack(padx=10, pady=10)

result_label = ctk.CTkLabel(root, text="")
result_label.pack(padx=10, pady=20)

root.mainloop()
