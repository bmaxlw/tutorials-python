from tkinter import *
import functions as f
import functools as ft

# widgets => GUI elements: buttons, textboxes, labels, images
# windows => containers to contain widgets


class Application:
    def __init__(self, auth=0):  # authentication status default 0 - not authenticated, 1 - authenticated
        self.auth = auth

    # [06.04.2022]: Creates a tkinter empty window with basic changeable configurations
    def set_window(self,
                   window_logo,                     # 'logo.png'
                   window_width_height='420x420',
                   window_title='New App',
                   window_background='white'):
        window = Tk()
        window.geometry(window_width_height)
        window.title(window_title)
        logo = PhotoImage(file=window_logo)
        window.iconphoto(True, logo)
        window.config(background=window_background)
        return window

    # [06.04.2022]: Creates a tkinter label inside a master window
    def set_label(self,
                  window,                            # window to put label on
                  label_text='Hello World!',         # displayed text of the label
                  label_font=('Arial', 10, 'bold'),  # a tuple as in the example
                  label_fg='black',                  # label foreground (a text color) default=black
                  label_bg='white',                  # label background (a background color) default=white
                  padding_x=0,
                  padding_y=0
                  ):
        label = Label(master=window,
                      text=label_text,
                      font=label_font,
                      fg=label_fg,
                      bg=label_bg,
                      padx=padding_x,
                      pady=padding_y)
        label.pack()                             # void

    # [07.04.2022]: Creates a tkinter button inside a master window
    def set_button(self,
                   window,
                   btn_text='Click me!',
                   btn_command=None,
                   btn_font=('Arial', 10, 'bold'),
                   btn_foreground='black',
                   btn_background='white',
                   btn_active_fg='white',
                   btn_active_bg='black',
                   padding_x=0,
                   padding_y=0,
                   btn_side=None):
        button = Button(master=window,
                        text=btn_text,
                        command=btn_command,
                        font=btn_font,
                        fg=btn_foreground,
                        bg=btn_background,
                        activeforeground=btn_active_fg,
                        activebackground=btn_active_bg,
                        padx=padding_x,
                        pady=padding_y
                        )
        button.pack(side=btn_side)

    # [07.04.2022]: Creates a tkinter entry inside a master window
    def set_entry(self,
                  window,
                  entry_font=('Arial', 10, 'bold')):
        entry = Entry(master=window,
                      font=entry_font)
        entry.pack()
        return entry

    # [07.04.2022]: Is used to insert data into Customers table
    def sql_ins_Customers(self, f_name, l_name, email, phone, db='CustomerApp'):
        f.sql_server_connect(db).execute(
            f"INSERT INTO Customers(FirstName, LastName, "
            f"                      EmailAddress, PhoneNumber)"
            f"VALUES('{f_name.get()}', '{l_name.get()}', "
            f"       '{email.get()}', '{phone.get()}');"
        ).commit()
        f_name.delete(0, END)  # clear entry field (0, END) == [0:]
        l_name.delete(0, END)
        email.delete(0, END)
        phone.delete(0, END)

    # [07.04.2022]: Is used to clear entries
    def clear_entries(self, f_name, l_name, email, phone):
        f_name.delete(0, END)  # clear entry field (0, END) == [0:]
        l_name.delete(0, END)
        email.delete(0, END)
        phone.delete(0, END)

    # [07.04.2022]: Is used to sign in as user (data taken from Users table)
    def sign_in(self, username, user_password, master, db='CustomerApp'):
        status = f.sql_server_connect(db).execute(
            f"SELECT ID FROM Users WHERE "
            f"Username = '{username.get()}' AND Password = '{user_password.get()}';"
        ).fetchall()
        if len(status) > 0:
            self.auth = 1
        else:
            self.auth = 0
        master.destroy()


app = Application()

# [07.04.2022]: Login window
login_window = app.set_window(window_logo='logo.png', window_title='CMS v1.0 Alpha', window_width_height='300x250',
                              window_background='whitesmoke')
app.set_label(login_window, label_text=f'Login:', padding_x=100, padding_y=10, label_font=('Arial', 15, 'bold'),
              label_bg='whitesmoke')
login = app.set_entry(login_window, entry_font=('Arial', 15))

app.set_label(login_window, label_text=f'Password:', padding_x=100, padding_y=10, label_font=('Arial', 15, 'bold'),
              label_bg='whitesmoke')
password = app.set_entry(login_window, entry_font=('Arial', 15))
app.set_button(login_window, btn_text='Sign in', btn_font=('Arial', 15, 'bold'),
               # ft.partial => to call args separately
               btn_command=ft.partial(app.sign_in, username=login, user_password=password, master=login_window),
               btn_background='white', btn_foreground='black', btn_active_bg='green',
               btn_active_fg='white')
login_window.mainloop()

# [07.04.2022]: Main window is accessible only if app.auth == 1
if app.auth == 1:
    main_window = app.set_window(window_logo='logo.png', window_title='CMS v1.0 Alpha', window_width_height='300x390',
                                 window_background='whitesmoke')
    app.set_label(main_window, label_text=f'First Name:', padding_x=100, padding_y=10, label_font=('Arial', 15, 'bold'),
                  label_bg='whitesmoke')
    first_name = app.set_entry(main_window, entry_font=('Arial', 15))
    app.set_label(main_window, label_text=f'Last Name:', padding_x=100, padding_y=10, label_font=('Arial', 15, 'bold'),
                  label_bg='whitesmoke')
    last_name = app.set_entry(main_window, entry_font=('Arial', 15))
    app.set_label(main_window, label_text=f'Email Address:', padding_x=100, padding_y=10, label_font=('Arial', 15, 'bold'),
                  label_bg='whitesmoke')
    email_address = app.set_entry(main_window, entry_font=('Arial', 15))
    app.set_label(main_window, label_text=f'Phone Number:', padding_x=100, padding_y=10, label_font=('Arial', 15, 'bold'),
                  label_bg='whitesmoke')
    phone_number = app.set_entry(main_window, entry_font=('Arial', 15))
    app.set_button(main_window, btn_text='Submit', btn_font=('Arial', 15, 'bold'),
                   # ft.partial => to call args separately
                   btn_command=ft.partial(app.sql_ins_Customers, first_name, last_name, email_address, phone_number),
                   btn_background='white', btn_foreground='black', btn_active_bg='green',
                   btn_active_fg='white')
    app.set_button(main_window, btn_text='Clear', btn_font=('Arial', 15, 'bold'),
                   # ft.partial => to call args separately
                   btn_command=ft.partial(app.clear_entries, first_name, last_name, email_address, phone_number),
                   btn_background='white', btn_foreground='black', btn_active_bg='green',
                   btn_active_fg='white')
    main_window.mainloop()
