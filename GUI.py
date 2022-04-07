from tkinter import *

# widgets => GUI elements: buttons, textboxes, labels, images
# windows => containers to contain widgets


# [06.04.2022]: Creates a tkinter empty window with basic changeable configurations
def set_window(window_logo,                     # 'logo.png'
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


# [06.04.2022]: Creates a tkinter label inside a declared window
def set_label(window,                            # window to put label on
              label_text='Hello World!',          # displayed text of the label
              label_font=('Arial', 20, 'bold'),  # a tuple as in the example
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


def set_button(window,
               btn_text='Click me!',
               btn_command=None,
               btn_font=('Arial', 20, 'bold'),
               btn_foreground='black',
               btn_background='white',
               btn_active_fg='white',
               btn_active_bg='black'):
    button = Button(master=window,
                    text=btn_text,
                    command=btn_command,
                    font=btn_font,
                    fg=btn_foreground,
                    bg=btn_background,
                    activeforeground=btn_active_fg,
                    activebackground=btn_active_bg
                    )
    button.pack()


class Clicker:
    i = 0

    def click_one(self):
        self.i += 1
        return self.i


c = Clicker()
main_window = set_window(window_logo='logo.png')
set_label(main_window, label_text=f'{c.click_one()}', padding_x=100, padding_y=10)

btn = set_button(main_window, btn_command=c.click_one)
main_window.mainloop()
