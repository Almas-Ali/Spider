'''\
Spider - A Web Status Checking GUI Application.
Designed And Developed By Md. Almas Ali

Website: https://almasali.net
Email: almaspr3@gmail.com
'''


from tkinter import *
from tkinter import ttk
import datetime
import requests
import os

# Name variables :
app_name = 'Spider'
author = 'Md. Almas Ali'
__version__ = '0.0.2'
back_color = '#15222a'
output_color = '#'
headers = "'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'"



def web_status():
    '''Web Status Section.'''
    # Name variables :
    sub_title = 'Web Status - '

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

    root = Toplevel()
    root.geometry('700x550')
    root.maxsize('700', '550')
    root.minsize('700', '550')
    root.title(sub_title+app_name)

    f1 = Frame(root, background=back_color)
    f1.pack(fill=BOTH)
    f2 = Frame(root, background=back_color)
    f2.pack(fill=BOTH, expand=True)
    f3 = Frame(root, background='white')
    f3.pack(fill=X, side=BOTTOM)
    f4 = Frame(root, background=back_color, borderwidth=5, relief=RIDGE)
    f4.pack(fill=BOTH, expand=True)

    link = StringVar()

    l1 = Label(f1, text=sub_title[:-3], font='Arial 30 bold',
               background=back_color, foreground='#fff')
    # l1.grid(column=2, row=1)
    l1.pack(padx=180)

    e1 = Entry(f2, width='30', font='calibri 16', textvariable=link)
    e1.grid(column=1, row=2, pady=20, ipadx=120, padx=8, ipady=5)
    e1.insert(0, 'https://')

    style = ttk.Style(f2)
    style.configure('TButton', font='calibri 12 bold',
                    borderwidth=4, background=back_color)
    style.map('TButton', foreground=[
        ('active', 'red'), ('!disabled', 'green')], background=[('active', back_color)])

    b1 = ttk.Button(f2, text='Check', style='TButton', command=Get_Updates)
    b1.grid(column=2, row=2, padx=5, ipady=8)

    l2 = Label(f3, text='', font='calibri, 12 bold')
    l2.grid(column=1, row=1)

    l3 = Label(f4, text='', background=back_color,
               font='calibri 20 bold', foreground='white')
    l3.pack()
    l4 = Label(f4, text='', background=back_color,
               font='calibri 20 bold', foreground='white')
    l4.pack()
    l5 = Label(f4, text='', background=back_color,
               font='calibri 20 bold', foreground='white')
    l5.pack()

    l6 = Label(f3, text='Charecter: 0', font='calibri, 12 bold')
    l6.grid(column=2, row=1)
    charecter_update()

    root.mainloop()


def wp_checker():
    '''Wordpress Checker'''
    # Name variables :
    sub_title = 'WP Checker - '

    def Get_Updates():
        l2.config(text='Checking...')
        l2.update()

        # WP Checker checking code goes here
        linkx = link.get()
        try:
            try:
                output = requests.get(os.path.join(linkx, '/wp-login.php'), headers=headers)
            except:
                try:
                    output = requests.get(os.path.join(linkx, '/wp-content/'), headers=headers)
                except:
                    try:
                        output = requests.get(os.path.join(linkx, '/wp-content/theme/'), headers=headers)
                    except:
                        try:
                            output = requests.get(os.path.join(linkx, '/wp-admin/'), headers=headers)
                        except:
                            try:
                                output = requests.get(os.path.join(linkx, '/wp-corn.php'), headers=headers)
                            except:
                                output = ''

            print(output)

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

    root = Toplevel()
    root.geometry('700x550')
    root.maxsize('700', '550')
    root.minsize('700', '550')
    root.title(sub_title+app_name)

    f1 = Frame(root, background=back_color)
    f1.pack(fill=BOTH)
    f2 = Frame(root, background=back_color)
    f2.pack(fill=BOTH, expand=True)
    f3 = Frame(root, background='white')
    f3.pack(fill=X, side=BOTTOM)
    f4 = Frame(root, background=back_color, borderwidth=5, relief=RIDGE)
    f4.pack(fill=BOTH, expand=True)

    link = StringVar()

    l1 = Label(f1, text=sub_title[:-3], font='Arial 30 bold',
               background=back_color, foreground='#fff')
    # l1.grid(column=2, row=1)
    l1.pack(padx=180)

    e1 = Entry(f2, width='30', font='calibri 16', textvariable=link)
    e1.grid(column=1, row=2, pady=20, ipadx=120, padx=8, ipady=5)
    e1.insert(0, 'https://')

    style = ttk.Style(f2)
    style.configure('TButton', font='calibri 12 bold',
                    borderwidth=4, background=back_color)
    style.map('TButton', foreground=[
        ('active', 'red'), ('!disabled', 'green')], background=[('active', back_color)])

    b1 = ttk.Button(f2, text='Check', style='TButton', command=Get_Updates)
    b1.grid(column=2, row=2, padx=5, ipady=8)

    l2 = Label(f3, text='', font='calibri, 12 bold')
    l2.grid(column=1, row=1)

    l3 = Label(f4, text='', background=back_color,
               font='calibri 20 bold', foreground='white')
    l3.pack()
    l4 = Label(f4, text='', background=back_color,
               font='calibri 20 bold', foreground='white')
    l4.pack()
    l5 = Label(f4, text='', background=back_color,
               font='calibri 20 bold', foreground='white')
    l5.pack()

    l6 = Label(f3, text='Charecter: 0', font='calibri, 12 bold')
    l6.grid(column=2, row=1)
    charecter_update()

    root.mainloop()


root = Tk()
root.geometry('700x550')
root.maxsize('700', '550')
root.minsize('700', '550')
root.title(app_name)

f1 = Frame(root, background=back_color)
f1.pack(fill=BOTH)
f2 = Frame(root, background=back_color)
f2.pack(fill=BOTH, expand=True)


l1 = Label(f1, text=app_name, font='Arial 30 bold',
           background=back_color, foreground='#fff')
l1.pack(padx=180)

l2 = Label(f1, text='A Web Scanner Utility', font='Arial 12 bold',
           background=back_color, foreground='#fff')
l2.pack(padx=180)


style = ttk.Style(f2)
style.configure('TButton', font='calibri 12 bold',
                    borderwidth=4, background=back_color)
style.map('TButton', foreground=[
            ('active', 'red'), ('!disabled', 'green')], background=[('active', back_color)])


b1 = ttk.Button(f2, text='Web Status', style='TButton', command=web_status)
b1.grid(column=2, row=2, padx=5, ipady=8, pady=20)

b2 = ttk.Button(f2, text='WP Checker', style='TButton', command=wp_checker)
b2.grid(column=3, row=2, padx=5, ipady=8, pady=20)



root.mainloop()
