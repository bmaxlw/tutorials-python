import GUI as gf
from tkinter import *


app = gf.Application()

main_window = app.set_window('loader_logo.png', window_title='RepExp v1.0. Alpha', window_width_height='380x670')


app.set_label(main_window, label_text='Order ID:', label_font=('Comic Sans', 12))
order_id = app.set_entry(main_window, entry_width=40, entry_font=('Comic Sans', 11))  # OrderID

app.set_label(main_window, label_text='Customer Name:', label_font=('Comic Sans', 12))
customer = app.set_entry(main_window, entry_width=40, entry_font=('Comic Sans', 11))  # Customer

app.set_label(main_window, label_text='Customer Phone:', label_font=('Comic Sans', 12))
customer_phone = app.set_entry(main_window, entry_width=40, entry_font=('Comic Sans', 11))  # CustomerPhone

app.set_label(main_window, label_text='Customer Email:', label_font=('Comic Sans', 12))
customer_email = app.set_entry(main_window, entry_width=40, entry_font=('Comic Sans', 11))  # CustomerEmail

app.set_label(main_window, label_text='Product Quantity (>):', label_font=('Comic Sans', 12))
prod_qt_from = app.set_entry(main_window, entry_width=40, entry_font=('Comic Sans', 11))  # ProdQT From

app.set_label(main_window, label_text='Product Quantity (<):', label_font=('Comic Sans', 12))
prod_qt_to = app.set_entry(main_window, entry_width=40, entry_font=('Comic Sans', 11))  # ProdQT To

app.set_label(main_window, label_text='Product Name:', label_font=('Comic Sans', 12))
prod_name = app.set_entry(main_window, entry_width=40, entry_font=('Comic Sans', 11))  # ProdName

app.set_label(main_window, label_text='Shipping Address:', label_font=('Comic Sans', 12))
shipping_address = app.set_entry(main_window, entry_width=40, entry_font=('Comic Sans', 11))  # ShippingAddress

app.set_label(main_window, label_text='Order Price (>):', label_font=('Comic Sans', 12))
order_price_from = app.set_entry(main_window, entry_width=40, entry_font=('Comic Sans', 11))  # OrderPrice From

app.set_label(main_window, label_text='Order Price (<):', label_font=('Comic Sans', 12))
order_price_to = app.set_entry(main_window, entry_width=40, entry_font=('Comic Sans', 11))  # OrderPrice To

app.set_label(main_window, label_text='Supplier:', label_font=('Comic Sans', 12))
supplier = app.set_entry(main_window, entry_width=40, entry_font=('Comic Sans', 11))  # Supplier

# app.set_label(main_window, label_text='Date (>):', label_font=('Comic Sans', 12))
# supplier = app.set_entry(main_window, entry_width=40, entry_font=('Comic Sans', 11))  # Date From
#
# app.set_label(main_window, label_text='Date (<):', label_font=('Comic Sans', 12))
# supplier = app.set_entry(main_window, entry_width=40, entry_font=('Comic Sans', 11))  # Date To

app.set_label(main_window, label_text='Path:', label_font=('Comic Sans', 12))
path = app.set_entry(main_window, entry_width=40, entry_font=('Comic Sans', 11))  # Path

app.set_button(main_window, btn_text='EXPORT', btn_font=('Comic Sans', 12), padding_x=50)
app.set_button(main_window, btn_text='CLEAR', btn_font=('Comic Sans', 12), padding_x=57)

main_window.mainloop()

