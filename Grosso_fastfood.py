# Author Name: Martin Grosso
# Date: 8/3/2022
# Program Name: Grosso_fastfood.py
# Purpose: Menu GUI

import tkinter
import tkinter.messagebox


class MenuGui:

    def __init__(self):
        # Create main window
        self.message = None
        self.main_window = tkinter.Tk()

        # Create menu, order button, and quit button frames
        self.menu_frame = tkinter.Frame(self.main_window)
        self.orderquitbutton_frame = tkinter.Frame(self.main_window)
        self.okquitbutton_frame = tkinter.Frame(self.main_window)

        # Create intVar objects for checkbuttons
        self.hamburger_value = tkinter.IntVar()
        self.cheeseburger_value = tkinter.IntVar()
        self.baconcheeseburger_value = tkinter.IntVar()
        self.hotdog_value = tkinter.IntVar()
        self.fries_value = tkinter.IntVar()
        self.shake_value = tkinter.IntVar()
        self.soda_value = tkinter.IntVar()

        # Set intVar objets to zero
        self.hamburger_value.set(0)
        self.cheeseburger_value.set(0)
        self.baconcheeseburger_value.set(0)
        self.hotdog_value.set(0)
        self.fries_value.set(0)
        self.shake_value.set(0)
        self.soda_value.set(0)

        # Create the checkbutton widgets for menu frame
        self.hamburger = tkinter.Checkbutton(self.menu_frame,
                                             text="Hamburger \t\t ($3.59)", anchor="w",
                                             variable=self.hamburger_value)

        self.cheeseburger = tkinter.Checkbutton(self.menu_frame,
                                                text="Cheeseburger \t\t ($3.97)", anchor="w",
                                                variable=self.cheeseburger_value)

        self.baconcheeseburger = tkinter.Checkbutton(self.menu_frame,
                                                     text="Bacon cheeseburger \t ($4.35)", anchor="w",
                                                     variable=self.baconcheeseburger_value)

        self.hotdog = tkinter.Checkbutton(self.menu_frame,
                                          text="Hotdog \t\t\t ($1.95)",
                                          variable=self.hotdog_value)

        self.fries = tkinter.Checkbutton(self.menu_frame,
                                         text="Fries \t\t\t ($2.79)",
                                         variable=self.fries_value)

        self.shake = tkinter.Checkbutton(self.menu_frame,
                                         text="Shake \t\t\t ($3.15)",
                                         variable=self.shake_value)

        self.soda = tkinter.Checkbutton(self.menu_frame,
                                        text="Soda \t\t\t ($1.86)",
                                        variable=self.soda_value)
        # Pack the checkbuttons
        self.hamburger.pack(anchor="w")
        self.cheeseburger.pack(anchor="w")
        self.baconcheeseburger.pack(anchor="w")
        self.hotdog.pack(anchor="w")
        self.fries.pack(anchor="w")
        self.shake.pack(anchor="w")
        self.soda.pack(anchor="w")

        # Create special instructions textbox
        self.specialinstructions_label = tkinter.Label(self.orderquitbutton_frame,
                                                       text='Special Instructions:')
        self.specialinstructions_entry = tkinter.Entry(self.orderquitbutton_frame,
                                                       width=30)

        # Pack special instructions textbox
        self.specialinstructions_label.pack(side="left", anchor="w")
        self.specialinstructions_entry.pack(side="right", anchor="w")

        # Create order and quit buttons
        self.order_button = tkinter.Button(self.okquitbutton_frame,
                                           text="Order",
                                           command=self.show)
        self.quit_button = tkinter.Button(self.okquitbutton_frame,
                                          text="Quit",
                                          command=self.main_window.destroy)

        # Pack order and quit button
        self.order_button.pack(side="left")
        self.quit_button.pack(side="right")

        # Pack the frames
        self.menu_frame.pack()
        self.orderquitbutton_frame.pack()
        self.okquitbutton_frame.pack()

        # Begin the mainloop
        tkinter.mainloop()

    # show function
    def show(self):

        # Create total variable
        total = 0
        # Initiate self message, user ordered
        self.message = 'You ordered: \n'
        self.message += "------------------------------------------\n"

        # If statements for checkboxes
        if self.hamburger_value.get() == 1:
            self.message = self.message + 'Hamburger \t\t ($3.59) \n'
            total += 3.59

        if self.cheeseburger_value.get() == 1:
            self.message = self.message + 'Cheeseburger \t\t ($3.97) \n'
            total += 3.97

        if self.baconcheeseburger_value.get() == 1:
            self.message = self.message + 'Bacon Cheeseburger \t ($4.35) \n'
            total += 4.35

        if self.hotdog_value.get() == 1:
            self.message = self.message + 'Hotdog \t\t\t ($1.95) \n'
            total += 1.95

        if self.fries_value.get() == 1:
            self.message = self.message + 'Fries \t\t\t ($2.79) \n'
            total += 2.79

        if self.shake_value.get() == 1:
            self.message = self.message + 'Shake \t\t\t ($3.15) \n'
            total += 3.15

        if self.soda_value.get() == 1:
            self.message = self.message + 'Soda \t\t\t ($1.86) \n'
            total += 1.86

        # Print total of checkboxes chosen by user and special instructions
        self.message += "------------------------------------------\n"
        self.message += "Total \t\t\t $%2.2f \n" % total
        self.message += "***Special instructions: " + self.specialinstructions_entry.get() + "***"
        tkinter.messagebox.showinfo('Order', self.message)


# Create instance of menu gui
menu_gui = MenuGui()
