from tkinter import *
from tkinter import ttk
import datetime
import requests

# Name variables :
app_name = 'Web Status'
author = 'Md. Almas Ali'
__version__ = '0.0.1'
back_color = '#ff8943'
output_color = '#'


def Get_Updates():
    l2.config(text='Checking...')
    l2.update()

    # Web status checking code goes here
    linkx = link.get()
    try:
        output = requests.get(linkx)

        l3.config(text=f'Link : {output.url}')
        l3.update()

        l4.config(text=f'Status Code :{output.status_code}')
        l4.update()
        time = datetime.datetime.now()
        timex = time.strftime('%d %B, %Y - %I:%M:%S %p')
        l5.config(text=f'{timex}')
        l5.update()
        
    except:
        l2.config(text='Error')
        l2.update()
    else:
        l2.config(text='OK')
        l2.update()

def charecter_update():
    l6.config(text=f'Charecter: {len(link.get())}')
    l6.update()
    # print(len(link.get()))
    root.after(500, charecter_update)


root = Tk()
root.geometry('700x550')
root.maxsize('700', '550')
root.minsize('700', '550')
root.title(app_name)

f1 = Frame(root, background=back_color)
f1.pack(fill=BOTH)
f2 = Frame(root, background=back_color)
f2.pack(fill=BOTH, expand=True)
f3 = Frame(root, background='white')
f3.pack(fill=X, side=BOTTOM)
f4 = Frame(root, background=back_color, borderwidth=5, relief=RIDGE)
f4.pack(fill=BOTH, expand=True)


link = StringVar()

l1 = Label(f1, text=app_name, font='Arial 30 bold',
           background=back_color, foreground='#fff')
# l1.grid(column=2, row=1)
l1.pack(padx=180)

e1 = Entry(f2, width='30', font='calibri 16', textvariable=link)
e1.grid(column=1, row=2, pady=20, ipadx=120, padx=8, ipady=5)

style = ttk.Style(f2)
style.configure('TButton', font='calibri 12 bold',
                borderwidth=4, background=back_color)
style.map('TButton', foreground=[
          ('active', 'red'), ('!disabled', 'green')], background=[('active', back_color)])

b1 = ttk.Button(f2, text='Check', style='TButton', command=Get_Updates)
b1.grid(column=2, row=2, padx=5, ipady=8)

l2 = Label(f3, text='', font='calibri, 12 bold')
l2.grid(column=1, row=1)

l3 = Label(f4, text='', background=back_color, font='calibri 20 bold', foreground='white')
l3.pack()
l4 = Label(f4, text='', background=back_color, font='calibri 20 bold', foreground='white')
l4.pack()
l5 = Label(f4, text='', background=back_color, font='calibri 20 bold', foreground='white')
l5.pack()

l6 = Label(f3, text='Charecter: 0', font='calibri, 12 bold')
l6.grid(column=2, row=1)
charecter_update()

root.mainloop()
