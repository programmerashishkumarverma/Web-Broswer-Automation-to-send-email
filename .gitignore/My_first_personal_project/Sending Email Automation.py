import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import tkinter.messagebox
import time
import pyautogui as py

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command = lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # label = tk.Label(self, text="This is the start page", font=controller.title_font)
        # label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text='Welcome, To')
        label.config(font=("Courier", 44))
        label.place(x=20, y=20)
        label.pack()

        label2 = tk.Label(self, text='Ultimate Logger')
        label2.config(font=("Courier", 44))
        label2.place(x=20, y=50)
        label2.pack()

        label3 = tk.Label(self, text='Make Sure that your screen Resoulution is 1366x768')
        label3.config(font=("Courier", 30))
        label3.place(x=20, y=500)
        label3.pack()


        next_button = tk.Button(self, text='Next', command=lambda: controller.show_frame('PageOne'))
        next_button.pack()

        label4 = tk.Label(self, text='Made by Ashish', pady=500)
        label4.config(font=("Courier", 20))
        label4.pack()

  




        # button1 = tk.Button(self, text="Go to Page One",
        #                     command=lambda: controller.show_frame("PageOne"))
        # button2 = tk.Button(self, text="Go to Page Two",
        #                     command=lambda: controller.show_frame("PageTwo"))
        # button1.pack()
        # button2.pack()





def Run_fire():
    pass


def askquestionchrome():

    answer = tk.messagebox.askquestion('NOTE', 'Do You Have Any Attachments')

    if answer == 'yes':
        tk.messagebox.showinfo('READ', "when atuomation starts don't do anything to the computer when attachments folder open time span will be open for only 25 sec open your file and submit it and Make Sure your Window Has full size ")

        Run_Chrome_attachment()
    else:
        tk.messagebox.showinfo('READ', "when atuomation starts don't do anything to the computer when attachments folder open time span will be open for only 25 sec open your file and submit it and Make Sure your Window Has full size")
        Run_Chrome()



print(1366/2)
print(768/2)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):

        global Name_entry
        global password
        global t
        global s
        global m

        tk.Frame.__init__(self, parent)
        self.controller = controller
        name_label = tk.Label(self, text='Email')
        name_label.config(font=("Courier", 30))
        name_label.config(font=("Courier", 30))
        name_label.grid(row=0, column=0)
        Name_entry = tk.Entry(self)
        Name_entry.grid(row=0, column=1)

        passwordl= tk.Label(self, text='Password')
        passwordl.config(font=("Courier", 30))
        passwordl.grid(row=1, column=0)
        password = tk.Entry(self)
        password.grid(row=1, column=1)

        to= tk.Label(self, text='To')
        to.config(font=("Courier", 30))
        to.grid(row=2, column=0)
        t = tk.Entry(self)
        t.grid(row=2, column=1)

        subject= tk.Label(self, text='Subject')
        subject.config(font=("Courier", 30))
        subject.grid(row=3, column=0)
        s = tk.Entry(self)
        s.grid(row=3, column=1)

        M= tk.Label(self, text='Message')
        M.config(font=("Courier", 30))
        M.grid(row=4, column=0)
        m = tk.Entry(self)
        m.grid(row=4, column=1)

        button = tk.Button(self, text='Submit', command=lambda: controller.show_frame('PageTwo'))
        button.grid(row=5, column=1)




        button = tk.Button(self, text='Submit', command=lambda: controller.show_frame('PageTwo'))
        button.grid(row=5, column=1)


# class Chrome:
#     global Name_entry
#
#     email = Name_entry.get()
#
def Run_Chrome_attachment():
        # https://accounts.google.com/signin/v2/identifier?hl=en&service=local&flowName=GlifWebSignIn&flowEntry=ServiceLogin
    global Name_entry

    global password
    global t
    global s
    global m
    email = Name_entry.get()
    passw = password.get()
    To = t.get()
    subject = s.get()
    message = m.get()

    py.click(25, 738)
    time.sleep(1)
    py.click(88, 696)
    time.sleep(1)
    py.typewrite('Google Chrome')
    time.sleep(1)
    py.click(111, 226)
    time.sleep(20)
    py.click(1349,46)
    py.click(1164, 121)
    time.sleep(5)
    py.click(443,47)
    py.typewrite('https://accounts.google.com/signin/v2/identifier?hl=en&service=local&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    py.typewrite(['enter'])
    time.sleep(10)
    py.click(559,364)
    py.typewrite(email)
    time.sleep(0.1)
    py.click(816,536)
    time.sleep(10)
    py.click(559,375)
    py.typewrite(passw)
    py.click(819,448)
    time.sleep(10)
    py.click(1217,94)
    time.sleep(0.1)
    py.click(1090,388)
    time.sleep(10)
    py.click(81, 189)
    time.sleep(4)
    py.click(909,316)
    py.typewrite(To)
    time.sleep(1)
    py.click(880,357)
    py.typewrite(subject)
    time.sleep(1)
    py.click(817,400)
    py.typewrite(message)
    time.sleep(1)
    py.click(969,706)
    time.sleep(25)
    py.click(881,705)

def Run_Chrome():
        # https://accounts.google.com/signin/v2/identifier?hl=en&service=local&flowName=GlifWebSignIn&flowEntry=ServiceLogin
    global Name_entry

    global password
    global t
    global s
    global m
    email = Name_entry.get()
    passw = password.get()
    To = t.get()
    subject = s.get()
    message = m.get()

    py.click(25, 738)
    time.sleep(1)
    py.click(88, 696)
    time.sleep(1)
    py.typewrite('Google Chrome')
    time.sleep(1)
    py.click(111, 226)
    time.sleep(20)
    py.click(1349,46)
    py.click(1164, 121)
    time.sleep(5)
    py.click(443,47)
    py.typewrite('https://accounts.google.com/signin/v2/identifier?hl=en&service=local&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    py.typewrite(['enter'])
    time.sleep(10)
    py.click(559,364)
    py.typewrite(email)
    time.sleep(0.1)
    py.click(816,536)
    time.sleep(10)
    py.click(559,375)
    py.typewrite(passw)
    py.click(819,448)
    time.sleep(10)
    py.click(1217,94)
    time.sleep(0.1)
    py.click(1090,388)
    time.sleep(10)
    py.click(81, 189)
    time.sleep(4)
    py.click(909,316)
    py.typewrite(To)
    time.sleep(1)
    py.click(880,357)
    py.typewrite(subject)
    time.sleep(1)
    py.click(817,400)
    py.typewrite(message)
    time.sleep(1)
    py.click(881,705)











        # button = tk.Button(self, text="Go to the start page",
        #                    command=lambda: controller.show_frame("StartPage"))
        # button.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Choose Your WebBroswer")
        label.place(x=100, y=100)
        label.config(font=("Courier", 30))
        label.pack()


        Chrome = tk.Button(self, text='Chrome', command=askquestionchrome)
        Chrome.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.geometry('1366x768')
    app.mainloop()
