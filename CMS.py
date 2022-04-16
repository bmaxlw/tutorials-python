import functools as ft
import GUI as gf

# widgets => GUI elements: buttons, entries, labels, images
# windows => containers to contain widgets

app = gf.Application()

# [07.04.2022]: Login window
login_window = app.set_window(window_logo='logo.png', window_title='CMS v1.0 Alpha', window_width_height='300x250',
                              window_background='whitesmoke')
app.set_label(login_window, label_text=f'Login:', padding_x=100, padding_y=10, label_font=('Arial', 15, 'bold'),
              label_bg='whitesmoke')
login = app.set_entry(login_window, entry_font=('Arial', 15))

app.set_label(login_window, label_text=f'Password:', padding_x=100, padding_y=10, label_font=('Arial', 15, 'bold'),
              label_bg='whitesmoke')
password = app.set_entry(login_window, entry_font=('Arial', 15), show_sign='*')
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
