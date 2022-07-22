import tkinter as tk
from tkinter import Entry, ttk
from tkinter import messagebox

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(True, True)
root.title('Am4Helper')

label = tk.Label(text="AM4 Helper")
label.pack()

entry = Entry(root)
entry.pack()
valor = entry.get()

def showValor():
    messagebox.showinfo("hello",str(valor))

print_button = ttk.Button(
    root,
    text='Print',
    command=showValor
)

print_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

# exit button
exit_button = ttk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()