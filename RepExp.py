import GUI as gf
import functools as ft


app = gf.Application()

main_window = app.set_window('loader_logo.png', window_title='RepExp v1.0. Alpha',
                             window_width_height='310x675', window_background='#1B1A17')

app.set_label(main_window, label_text='Order ID:', label_font=('Roboto', 11, 'bold'), label_bg='#1B1A17',
              label_fg='white')
order_id = app.set_entry(main_window, entry_width=40, entry_font=('Roboto', 10), entry_bg_color='#E6D5B8',
                         entry_bd=2)  # OrderID

app.set_label(main_window, label_text='Customer Name:', label_font=('Roboto', 11, 'bold'), label_bg='#1B1A17',
              label_fg='white')
customer = app.set_entry(main_window, entry_width=40, entry_font=('Roboto', 10), entry_bg_color='#E6D5B8',
                         entry_bd=2)  # Customer

app.set_label(main_window, label_text='Customer Phone:', label_font=('Roboto', 11, 'bold'), label_bg='#1B1A17',
              label_fg='white')
customer_phone = app.set_entry(main_window, entry_width=40, entry_font=('Roboto', 10), entry_bg_color='#E6D5B8',
                               entry_bd=2)  # CustomerPhone

app.set_label(main_window, label_text='Customer Email:', label_font=('Roboto', 11, 'bold'), label_bg='#1B1A17',
              label_fg='white')
customer_email = app.set_entry(main_window, entry_width=40, entry_font=('Roboto', 10), entry_bg_color='#E6D5B8',
                               entry_bd=2)  # CustomerEmail

app.set_label(main_window, label_text='Product Quantity (>):', label_font=('Roboto', 11, 'bold'), label_bg='#1B1A17',
              label_fg='white')
prod_qt_from = app.set_entry(main_window, entry_width=40, entry_font=('Roboto', 10), entry_bg_color='#E6D5B8',
                             entry_bd=2)  # ProdQT From

app.set_label(main_window, label_text='Product Quantity (<):', label_font=('Roboto', 11, 'bold'), label_bg='#1B1A17',
              label_fg='white')
prod_qt_to = app.set_entry(main_window, entry_width=40, entry_font=('Roboto', 10), entry_bg_color='#E6D5B8',
                           entry_bd=2)  # ProdQT To

app.set_label(main_window, label_text='Product Name:', label_font=('Roboto', 11, 'bold'), label_bg='#1B1A17',
              label_fg='white')
prod_name = app.set_entry(main_window, entry_width=40, entry_font=('Roboto', 10), entry_bg_color='#E6D5B8',
                          entry_bd=2)  # ProdName

app.set_label(main_window, label_text='Customer Country:', label_font=('Roboto', 11, 'bold'), label_bg='#1B1A17',
              label_fg='white')
customer_country = app.set_entry(main_window, entry_width=40, entry_font=('Roboto', 10), entry_bg_color='#E6D5B8',
                                 entry_bd=2)  # CustomerCountry

app.set_label(main_window, label_text='Customer City:', label_font=('Roboto', 11, 'bold'), label_bg='#1B1A17',
              label_fg='white')
customer_city = app.set_entry(main_window, entry_width=40, entry_font=('Roboto', 10), entry_bg_color='#E6D5B8',
                              entry_bd=2)  # CustomerCity

app.set_label(main_window, label_text='Shipping Address:', label_font=('Roboto', 11, 'bold'), label_bg='#1B1A17',
              label_fg='white')
shipping_address = app.set_entry(main_window, entry_width=40, entry_font=('Roboto', 10), entry_bg_color='#E6D5B8',
                                 entry_bd=2)  # ShippingAddress

app.set_label(main_window, label_text='Order Price (>):', label_font=('Roboto', 11, 'bold'), label_bg='#1B1A17',
              label_fg='white')
order_price_from = app.set_entry(main_window, entry_width=40, entry_font=('Roboto', 10), entry_bg_color='#E6D5B8',
                                 entry_bd=2)  # OrderPrice From

app.set_label(main_window, label_text='Order Price (<):', label_font=('Roboto', 11, 'bold'), label_bg='#1B1A17',
              label_fg='white')
order_price_to = app.set_entry(main_window, entry_width=40, entry_font=('Roboto', 10), entry_bg_color='#E6D5B8',
                               entry_bd=2)  # OrderPrice To

app.set_label(main_window, label_text='Supplier:', label_font=('Roboto', 11, 'bold'), label_bg='#1B1A17',
              label_fg='white')
supplier = app.set_entry(main_window, entry_width=40, entry_font=('Roboto', 10), entry_bg_color='#E6D5B8',
                         entry_bd=2)  # Supplier

# app.set_label(main_window, label_text='Date (>):', label_font=('Comic Sans', 12))
# supplier = app.set_entry(main_window, entry_width=40, entry_font=('Comic Sans', 11))  # Date From
#
# app.set_label(main_window, label_text='Date (<):', label_font=('Comic Sans', 12))
# supplier = app.set_entry(main_window, entry_width=40, entry_font=('Comic Sans', 11))  # Date To

app.set_label(main_window, label_text='Export to (full path):', label_font=('Roboto', 11, 'bold'), label_bg='#1B1A17', label_fg='white')
path = app.set_entry(main_window, entry_width=40, entry_font=('Roboto', 10), entry_bg_color='#E6D5B8', entry_bd=2)  # Path

app.set_button(main_window, btn_text='Export', btn_font=('Roboto', 10, 'bold'), padding_x=50,
               btn_background='#F0A500', btn_foreground='white', btn_active_bg='black', btn_active_fg='#FFC947',
               btn_bd=2,
               btn_command=ft.partial(app.convert_attributes_RepExp,
                                      order_id, customer, customer_phone, customer_email,
                                      prod_qt_from, prod_qt_to, prod_name, customer_country,
                                      customer_city, shipping_address, order_price_from,
                                      order_price_to, supplier, path))
app.set_button(main_window, btn_text='Clear', btn_font=('Roboto', 10, 'bold'), padding_x=57,
               btn_background='#FF1818', btn_foreground='white', btn_active_bg='black', btn_active_fg='#FFC947',
               btn_bd=2,
               btn_command=ft.partial(app.clear_entries_RepExp, order_id, customer, customer_phone, customer_email,
                                      prod_qt_from, prod_qt_to, prod_name, customer_country,
                                      customer_city, shipping_address, order_price_from,
                                      order_price_to, supplier, path))

main_window.mainloop()





