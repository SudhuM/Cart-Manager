from tkinter import *
from tkinter import messagebox
from tkinter import Event
from tkinter import Listbox

# app initilaization
app = Tk()
app.title("Parts Manager")
app.geometry('550x330')
# keeps
entries = []
# text_variable = StringVar()


# entry addition to the list box with proper checking , whether the users
# filled out all the fields.


def add_entry():

    data = (parts_entry.get(), Customer_entry.get(),
            Retailer_entry.get(), Price_entry.get())

    if showerror(data):
        messagebox.showerror(
            'Empty Fields', 'please enter all the required fileds')

    else:
        entries.append(data)
        list_box.insert(END, Entry_format(entries))

        print(entries)
        clear_entry()

# update elements command .


def update_items():
    data = (parts_entry.get(), Customer_entry.get(),
            Retailer_entry.get(), Price_entry.get())
    if showerror(data):
        messagebox.showerror(
            'Empty Fields', 'please enter all the required fields.')
    else:
        entries.remove(entries[index])
        entries.insert(index, data)
        list_box.insert(END, Entry_format(entries))


# Items will removed when remove is pressed.
# remove the elements from last.
# can be changed - reverse the list befoe poping.


def remove_items():
    # entries.pop()
    entries.remove(value)
    clear_entry()
    Entry_format(entries)

    if len(entries) == 0:
        remove_button['state'] = 'disabled'
        update_button['state'] = 'disabled'


# when button clear is pressed the entered values in the entry will be removed


def clear_entry():
    parts_entry.delete(0, END)
    Customer_entry.delete(0, END)
    Retailer_entry.delete(0, END)
    Price_entry.delete(0, END)


def showerror(data):
    if not all(data):
        return True
    return False


# styling the listbox entry


def Entry_format(t):
    list_box.delete(0, END)
    for i in t:
        # list_box.insert(
        #     END, '{} - {} -{} under {}'.format(i[1], i[2], i[3], i[0]))

        list_box.insert(END, i)
    remove_button['state'] = 'active'
    update_button['state'] = 'active'

# event for getting the selected element data


def onselect(event):
    global value, index
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)

    populate(value)
    # print(index)


# populate the entry values


def populate(value):
    clear_entry()
    parts_entry.insert(0, value[0])
    Customer_entry.insert(0, value[1])
    Retailer_entry.insert(0, value[2])
    Price_entry.insert(0, value[3])


# parts Name
parts_name = Label(app, text='Parts Name')
parts_name.grid(row=0, column=0, padx=5, pady=20, sticky=W)
parts_entry = Entry(app, borderwidth=3)
parts_entry.grid(row=0, column=1, padx=10)

# Customer Name
Customer_name = Label(app, text='Customer')
Customer_name.grid(row=0, column=2, padx=5, sticky=W)
Customer_entry = Entry(app, borderwidth=3)
Customer_entry.grid(row=0, column=3)

# Retailer Name
Retailer_name = Label(app, text='Retailer')
Retailer_name.grid(row=1, column=0, sticky=W, padx=5)
Retailer_entry = Entry(app, borderwidth=3)
Retailer_entry.grid(row=1, column=1, padx=10)

# Price
Price_name = Label(app, text='Price')
Price_name.grid(row=1, column=2, sticky=W, padx=5)
Price_entry = Entry(app, borderwidth=3)
Price_entry.grid(row=1, column=3, pady=20)

# ListBox

list_box = Listbox(app,  height=8, width=50, border=0)

list_box.bind('<<ListboxSelect>>', onselect)
list_box.grid(row=4, column=0, columnspan=3, rowspan=6, padx=20, pady=20)


# scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=4, column=3, pady=30)

# scrollbar configuration with listbox

list_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_box.yview)

# buttons

add_button = Button(app, text="Add", width=10, command=add_entry)
add_button.grid(row=2, column=0, padx=5)

update_button = Button(app, text="Update", width=10,
                       state='disabled', command=update_items)
update_button.grid(row=2, column=1, padx=5)

remove_button = Button(app, text="Remove", width=10,
                       state='disabled', command=remove_items)
remove_button.grid(row=2, column=2, padx=5)

clear_button = Button(app, text="Clear", width=10, command=clear_entry)
clear_button.grid(row=2, column=3, padx=5)

app.mainloop()
