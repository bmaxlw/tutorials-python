from tkinter import *
import functions as f


# [06.04.2022]: App Main
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
                  padding_y=0,
                  label_side=None):
        label = Label(master=window,
                      text=label_text,
                      font=label_font,
                      fg=label_fg,
                      bg=label_bg,
                      padx=padding_x,
                      pady=padding_y)
        label.pack(side=label_side)                           # void

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
                   btn_side=None,
                   btn_bd=None):
        button = Button(master=window,
                        text=btn_text,
                        command=btn_command,
                        font=btn_font,
                        fg=btn_foreground,
                        bg=btn_background,
                        activeforeground=btn_active_fg,
                        activebackground=btn_active_bg,
                        padx=padding_x,
                        pady=padding_y,
                        bd=btn_bd
                        )
        button.pack(side=btn_side)

    # [07.04.2022]: Creates a tkinter entry inside a master window
    def set_entry(self,
                  window,
                  entry_font=('Arial', 10, 'bold'),
                  entry_bg_color='white',
                  entry_fg_color='black',
                  show_sign='',
                  entry_side=None,
                  entry_width=None,
                  entry_bd=None):
        entry = Entry(master=window,
                      font=entry_font,
                      bg=entry_bg_color,
                      fg=entry_fg_color,
                      show=show_sign,
                      width=entry_width,
                      bd=entry_bd)
        entry.pack(side=entry_side)
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

    # [11.04.2022]: (RepExp) Is used to clear entries
    def clear_entries_RepExp(self, order_id, customer, customer_phone, customer_email, prod_qt_from,
                             prod_qt_to, prod_name, customer_country, customer_city,
                             shipping_address, order_price_from, order_price_to, supplier, path):
        order_id.delete(0, END)
        customer.delete(0, END)
        customer_phone.delete(0, END)
        customer_email.delete(0, END)
        prod_qt_from.delete(0, END)
        prod_qt_to.delete(0, END)
        prod_name.delete(0, END)
        customer_country.delete(0, END)
        customer_city.delete(0, END)
        shipping_address.delete(0, END)
        order_price_from.delete(0, END)
        order_price_to.delete(0, END)
        supplier.delete(0, END)
        path.delete(0, END)
        path.delete(0, END)

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

    # [08.04.2022]: (RepExp) Extracts data filtered by conditions from db to .CSV
    def get_csv_from_db(self,
                        db,
                        path,
                        par_order_id='NULL',
                        par_customer='NULL',
                        par_customer_phone='NULL',
                        par_customer_email='NULL',
                        par_prod_qt='NULL',
                        par_prod_qt2='NULL',
                        par_prod_name='NULL',
                        par_customer_country='NULL',
                        par_customer_city='NULL',
                        par_shipping_address='NULL',
                        par_order_price='NULL',
                        par_order_price2='NULL',
                        par_supplier='NULL'):
        coalesce = lambda x: x if x == 'NULL' else f'{x}'
        crs = f.sql_server_connect(db).execute(
            f"EXEC sp_Rpt_RunCSV_export "
            f"@OrderID={coalesce(par_order_id)}, "
            f"@Customer={coalesce(par_customer)}, "
            f"@CustomerPhone={coalesce(par_customer_phone)}, "
            f"@CustomerEmail={coalesce(par_customer_email)}, "
            f"@ProdQT={coalesce(par_prod_qt)}, "
            f"@ProdQT2={coalesce(par_prod_qt2)}, "
            f"@ProdName={coalesce(par_prod_name)}, "
            f"@CustomerCountry={coalesce(par_customer_country)}, "
            f"@CustomerCity={coalesce(par_customer_city)}, "
            f"@ShippingAddress={coalesce(par_shipping_address)}, "
            f"@OrderPrice={coalesce(par_order_price)}, "
            f"@OrderPrice2={coalesce(par_order_price2)}, "
            f"@Supplier={coalesce(par_supplier)};").fetchall()
        with open(path, 'w') as file:
            for i in crs:
                for j in i:
                    file.write(f'{j}|')
                file.write('\n')

    # [08.04.2022]: (RepExp) Convert attributes
    def convert_attributes_RepExp(self, *attributes):
        converted = []
        for attr in attributes:
            if attr.get() == '':
                attr = 'NULL'
                converted.append(attr)
            else:
                converted.append(str(attr.get()))
        self.clear_entries_RepExp(attributes[0], attributes[1], attributes[2], attributes[3],
                                  attributes[4], attributes[5], attributes[6], attributes[7],
                                  attributes[8], attributes[9], attributes[10], attributes[11],
                                  attributes[12], attributes[13])
        self.get_csv_from_db(
            db='MainDB',
            path=converted[13],
            par_order_id=converted[0],
            par_customer=converted[1],
            par_customer_phone=converted[2],
            par_customer_email=converted[3],
            par_prod_qt=converted[4],
            par_prod_qt2=converted[5],
            par_prod_name=converted[6],
            par_customer_country=converted[7],
            par_customer_city=converted[8],
            par_shipping_address=converted[9],
            par_order_price=converted[10],
            par_order_price2=converted[11],
            par_supplier=converted[12],
        )


# app = Application()
# app.get_csv_from_db('MainDB', par_prod_qt='9', par_prod_qt2='100')

# (order_id.get(), customer.get(), customer_phone.get(), customer_email.get(),
#                       prod_qt_from.get(), prod_qt_to.get(), prod_name.get(), shipping_address.get(),
#                       order_price_from.get(), order_price_to.get(), supplier.get())





