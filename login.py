import tkinter as tk

root = tk.Tk()
root.geometry('350x500')
root.title('Login to the System')

show_face = '🔓'
hide_face = '🔒'

def show_hide_password():
    if password_entry['show'] == '*':
        password_entry.configure(show='')
        show_hide_btn.configure(text=show_face)
    else:
        password_entry.configure(show='*')
        show_hide_btn.configure(text=hide_face)
def login():
    user = user_name_lb.pack




page_frame = tk.Frame(root)

user_name_lb = tk.Label(page_frame, text='User Name', font=('Bold', 15))
user_name_lb.pack(pady=10)

hr_user_line = tk.Label(page_frame, text="-------------------------------", font=('Bold', 15),
                        fg='#d6d6d6')
hr_user_line.place(x=12, y=68)

user_name_entry = tk.Entry(page_frame, font=('Bold', 15), bd=0)
user_name_entry.pack(pady=10)

user_name_entry.bind('<FocusIn>', lambda e: hr_user_line.configure(fg='#158aff'))
user_name_entry.bind('<FocusOut>', lambda e: hr_user_line.configure(fg='#d6d6d6'))
password_lb = tk.Label(page_frame, text='Password', font=('Bold', 15))
password_lb.pack(pady=10)

show_hide_btn = tk.Button(root, text=hide_face, font=('Bold', 15), bd=0,
                          command=show_hide_password)
show_hide_btn.place(x=290, y=166)

hr_password_line = tk.Label(page_frame, text="-------------------------------", font=('Bold', 15),
                        fg='#d6d6d6')
hr_password_line.place(x=12, y=163)

password_entry = tk.Entry(page_frame, font=('Bold', 15), bd=0, show='*')
password_entry.pack(pady=10)

password_entry.bind('<FocusIn>', lambda e: hr_password_line.configure(fg='#158aff'))
password_entry.bind('<FocusOut>', lambda e: hr_password_line.configure(fg='#d6d6d6'))

login_btn = tk.Button(page_frame, text='Login', font=('Bold', 15), bd=0,
                      bg='#158aff', fg='white', width=20)
login_btn.pack(pady=20)


page_frame.pack(pady=20)
page_frame.pack_propagate(False)
page_frame.configure(width=250, height=500)

root.mainloop()
