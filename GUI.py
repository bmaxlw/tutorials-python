from tkinter import *
import functions as f

# widgets => GUI elements: buttons, textboxes, labels, images
# windows => containers to contain widgets

class Application:

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
                  padding_y=0,
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
                   padding_y=0):
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
        button.pack()

    def set_entry(self,
                  window,
                  entry_font=('Arial', 10, 'bold')):
        entry = Entry(master=window,
                      font=entry_font)
        entry.pack()
        return entry

    def sql_insert_customer_data(self):
        f.sql_server_connect('CustomerApp').execute(
            f"INSERT INTO Customers(FirstName, LastName, EmailAddress, PhoneNumber)"
            f"VALUES('{first_name.get()}', '{last_name.get()}', "
            f"       '{email_address.get()}', '{phone_number.get()}');"
        ).commit()



app = Application()
main_window = app.set_window(window_logo='logo.png', window_title='Customer v1.0 Alpha', window_width_height='300x360')
app.set_label(main_window, label_text=f'First Name:', padding_x=100, padding_y=10, label_font=('Arial', 15, 'bold'))
first_name = app.set_entry(main_window, entry_font=('Arial', 15))
app.set_label(main_window, label_text=f'Last Name:', padding_x=100, padding_y=10, label_font=('Arial', 15, 'bold'))
last_name = app.set_entry(main_window, entry_font=('Arial', 15))
app.set_label(main_window, label_text=f'Email Address:', padding_x=100, padding_y=10, label_font=('Arial', 15, 'bold'))
email_address = app.set_entry(main_window, entry_font=('Arial', 15))
app.set_label(main_window, label_text=f'Phone Number:', padding_x=100, padding_y=10, label_font=('Arial', 15, 'bold'))
phone_number = app.set_entry(main_window, entry_font=('Arial', 15))
app.set_button(main_window, btn_text='Submit', btn_font=('Arial', 15, 'bold'),
               btn_command=app.sql_insert_customer_data)
main_window.mainloop()
