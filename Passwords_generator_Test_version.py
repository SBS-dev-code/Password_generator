import customtkinter as ctk
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title('Generator of the passwords')
root.geometry('350x250')
root.resizable(width=False, height=False)

ch = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+",
    "=", "[", "]", "{", "}", ";", ":", ",", ".", "<", ">", "/", "?"
]

def randomize():
    try:
        length = int(e.get())
        
        if length <= 0:
            result.configure(text="Length should be more than zero", text_color="red")
            btn_copy.configure(state="disabled")
            return
        if length > 100:
            result.configure(text="Too more length! Limit: 100 chars", text_color="orange")
            btn_copy.configure(state="disabled")
            return
            
        password = "".join(random.choice(ch) for _ in range(length))
        result.configure(text=password, text_color="white")
        btn_copy.configure(state="normal")
        btn_copy.configure(fg_color="purple")
        
    except ValueError:
        result.configure(text="Please enter number!", text_color="red")
        btn_copy.configure(state="disabled")

def copy_to_clipboard():
    password_text = result.cget("text")
    if password_text and "!" not in password_text and "—" not in password_text:
        root.clipboard_clear()
        root.clipboard_append(password_text)
        root.update()
        result.configure(text="Copyied!", text_color="green")


label = ctk.CTkLabel(root, text='Please enter the length of the password:', font=('Arial', 13))
label.place(relx=0.5, y=20, anchor=ctk.CENTER)

e = ctk.CTkEntry(root, font=('Arial', 13), width=100, justify=ctk.CENTER, border_color='orange')
e.place(relx=0.5, y=55, anchor=ctk.CENTER)

btn = ctk.CTkButton(root, text='Generate', font=('Helvetica', 14, 'bold'), command=randomize)
btn.place(relx=0.5, y=105, anchor=ctk.CENTER)

result = ctk.CTkLabel(root, text='', font=('Arial', 12, 'bold'), wraplength=300)
result.place(relx=0.5, y=155, anchor=ctk.CENTER)

btn_copy = ctk.CTkButton(root, text='Copy', font=('Helvetica', 12), width=100, fg_color="gray", state="disabled", command=copy_to_clipboard)
btn_copy.place(relx=0.5, y=205, anchor=ctk.CENTER)

root.mainloop()