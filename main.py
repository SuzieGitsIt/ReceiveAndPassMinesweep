from functools import partial
import tkinter as tk                                # Tkinter's Tk class
from tkinter import ttk
from PIL import ImageTk, Image                  # Displaying LAL background photo
import configparser
config = configparser.ConfigParser()

## initalize all global variables and global arrays to call between classes
samp_arr1 = []
samp_arr2 = []
samp_arr3 = []
samp_arr4 = []
samp_arr5 = []
samp_arr6 = []
samp_arr7 = []
samp_arr8 = []
samp_arr9 = []
samp_arr10 = []

##########################################################################################################################################
#################################################      minesweep #1 BUTTONS         ######################################################
##########################################################################################################################################
class Mine1(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Sample #1 Numbers")
        self.geometry('380x450')

        #################################################            BUTTON PRESS STYLE           ################################################
        style = ttk.Style()
        style.theme_use('default')  # alt, default, clam and classic

        style.map('T.TButton', background=[('active', 'pressed', 'white'), ('!active', 'white'),('active', '!pressed', 'grey')])  # active, not active, not pressed
        style.map('T.TButton', relief=[('pressed', 'sunken'), ('!pressed', 'raised')])  # pressed, not pressed
        style.configure('T.TButton', font=('Helvetica', '10'))

        style.map('B.TButton', background=[('active', 'pressed', 'white'), ('!active', 'white'), ('active', '!pressed', 'grey')])  # Press me Button always hot pink when pressed
        style.map('B.TButton', relief=[('pressed', 'sunken'), ('!pressed', 'raised')])  # pressed, not pressed
        style.configure('B.TButton', font=('helvetica', '12', 'bold'))

        style.map('P.TButton', background=[('active', 'pressed', '#FF69B4'), ('!active', 'white'), ('active', '!pressed', 'grey')])  # Press me Button always hot pink when pressed
        style.map('P.TButton', relief=[('pressed', 'sunken'), ('!pressed', 'raised')])  # pressed, not pressed
        style.configure('P.TButton', font=('helvetica', '12', 'bold'))

        style.configure('R.TLabel', font=('helvetica', '12'), foreground='black', background='white')
        style.configure('B.TLabel', font=('helvetica', '12', 'bold'), foreground='black', background='white')

        #################################################           LAL BACKGROUND IMAGE          ################################################
        def resize_image(event):
            new_width = event.width
            new_height = event.height
            bg_img = copy_img.resize((new_width, new_height))
            new_img = ImageTk.PhotoImage(bg_img)
            lal_img.config(image=new_img)
            lal_img.bg_img = new_img  # avoid garbage collection

        # r stands for read, if we wanted to write to the file, we would put 'w'. If we wanted to append, we would put an 'a'
        bg_img = Image.open(r'\\RXS-FS-02\userdocs\shaynes\My Documents\My Pictures\Saved Pictures/white.png')
        copy_img = bg_img.copy()
        new_img = ImageTk.PhotoImage(bg_img)
        lal_img = tk.Label(self, image=new_img, background='white')
        lal_img.bind('<Configure>', resize_image)
        lal_img.place(x=0, y=0, relwidth=1, relheight=1)
        # lal_img.grid(row=0, column=0, sticky='NW')        # grid and pack can't coexist in the same project.
        # lal_img.pack(fill=tk.BOTH, expand=True)           # grid and pack can't coexist in the same project.

        ################################################                 MAIN BODY                ################################################
        counter = 0
        btn_text = (
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20',
            '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38',
            '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56',
            '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74',
            '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92',
            '93', '94', '95', '96', '97', '98', '99', '100')
        btn_ids = []

        def get_samp(n):
            btn_name = (btn_ids[n])  # create 100 unique button names from btn_ids[n]
            btn_name.config(text=f"{btn_text[n]}")  # configure the string of button numbers to the buttons
            print("button name: ", btn_name)  # btn_name = .!window.!button##
            samp_arr1.append(n + 1)  # add n+1 button click to list
            write_samp()

        def write_samp():
            print("samp_arr1: ", ', '.join(map(str, samp_arr1)))
            ttk.Label(self, text="Sample Set: ", style='B.TLabel').place(x=10, y=300)
            ttk.Label(self, text=', '.join(map(str, samp_arr1)), style='R.TLabel').place(x=145, y=310, anchor='w')

        for r in range(10):
            for c in range(10):
                print(counter, r, c)
                btn_grid = ttk.Button(self, width=3, text=btn_text[counter], style='T.TButton',command=partial(get_samp, counter))  # create buttons & assign unique arg (i) to run function (change)
                # btn_grid.bind('<Button 1>', write_samp)
                btn_grid.grid(row=r, column=c)
                btn_ids.append(btn_grid)  # add ID to list
                counter += 1  # update counter for next button text

        def save():
            print("This button is uselss, but makes people feel safe.")

        def clear():
            samp_arr1.clear()
            print("List after .clear() ", samp_arr1)
            tk.Label(self, text="                                                  "
                                "                                                   "
                                "                                                ").place(x=145, y=310, anchor='w')

        btn_sav_minesweep = ttk.Button(self, text='Save', width=5, style='T.TButton', command=save)
        # btn_sav_minesweep.bind('<Button-1>', pink)
        btn_sav_minesweep.place(x=230, y=400)

        btn_exit_minesweep = ttk.Button(self, text='Close', width=5, style='T.TButton', command=self.destroy)
        # btn_exit_minesweep.bind('<Button-1>', pink)
        btn_exit_minesweep.place(x=310, y=400)

        btn_clear = ttk.Button(self, text='Clear', width=5, style='T.TButton', command=clear)
        # btn_sav_minesweep.bind('<Button-1>', pink)
        btn_clear.place(x=150, y=400)

##########################################################################################################################################
############################################        END MINESWEEP POP UP WINDOWS        ##################################################
##########################################################################################################################################
###############################################      Sample Input & Dioptics         #####################################################
##########################################################################################################################################

class Dioptics(tk.Tk):
    def __init__(self):  # Special Method, first argument is self.
        super().__init__()

        self.geometry('1250x625')
        self.title('Main Window')
        ##self.title("Sample Sizes and Dioptics")       # title might have to be main window, from the last statement; if __name__ == "__main__":
        self.configure(background='white')              # Set background color
        self.option_add('*Font', 'Helvetica 11')        # set the font and size for entire Dioptics
        self.option_add('*foreground', 'black')         # set the text color, hex works too '#FFFFFF'
        self.option_add('*background', 'white')         # set the background to white

        #################################################            BUTTON PRESS STYLE           ################################################
        #style = ttk.Style()
        #style.theme_use('default')  # alt, default, clam and classic

        #style.map('T.TButton', background=[('active', 'pressed', 'white'), ('!active', 'grey'),('active', '!pressed', 'grey')])  # active, not active, not pressed
        #style.map('T.TButton', relief=[('pressed', 'sunken'), ('!pressed', 'raised')])  # pressed, not pressed
        #style.configure('T.TButton', font=('Helvetica', '10'))
        
        #style.map('B.TButton', background=[('active', 'pressed', 'white'), ('!active', 'white'),('active', '!pressed','grey')])  # Press me Button always hot pink when pressed
        #style.map('B.TButton', relief=[('pressed', 'sunken'), ('!pressed', 'raised')])  # pressed, not pressed
        #style.configure('B.TButton', font=('helvetica', '12', 'bold'))
        
        #style.map('P.TButton', background=[('active', 'pressed', '#FF69B4'), ('!active', 'white'),('active', '!pressed','grey')])  # Press me Button always hot pink when pressed
        #style.map('P.TButton', relief=[('pressed', 'sunken'), ('!pressed', 'raised')])  # pressed, not pressed
        #style.configure('P.TButton', font=('helvetica', '12', 'bold'))

        #style.configure('R.TLabel', font=('helvetica', '12'), foreground='black', background='white')
        #style.configure('B.TLabel', font=('helvetica', '12', 'bold'), foreground='black', background='white')

        ##################################################           LAL BACKGROUND IMAGE          ################################################
        #def resize_image(event):
        #    new_width = event.width
        #    new_height = event.height
        #    bg_img = copy_img.resize((new_width, new_height))
        #    new_img = ImageTk.PhotoImage(bg_img)
        #    lal_img.config(image=new_img)
        #    lal_img.bg_img = new_img  # avoid garbage collection

        ## r stands for read, if we wanted to write to the file, we would put 'w'. If we wanted to append, we would put an 'a'
        #bg_img = Image.open(r'\\RXS-FS-02\userdocs\shaynes\My Documents\My Pictures\Saved Pictures/white.png')
        #copy_img = bg_img.copy()
        #new_img = ImageTk.PhotoImage(bg_img)
        #lal_img = ttk.Label(self, image=new_img, background='white')
        #lal_img.bind('<Configure>', resize_image)
        #lal_img.place(x=0, y=0, relwidth=1, relheight=1)
        ##lal_img.grid(row=0, column=0, sticky='NW')
        ##lal_img.pack(fill=tk.BOTH, expand=True)

        #####################################                   MAIN BODY                ################################################
        #############################################         STATIC  LABELS          ###################################

        self.lbl_cmd_mc1 = tk.Label(self, text="Are the samples numbered in order?").place(x=150, y=20, anchor='center')
        self.lbl_cmd_mc2 = tk.Label(self, text="If not, click 'Manual' and a new window").place(x=150, y=40, anchor='center')
        self.lbl_cmd_mc3 = tk.Label(self, text="will popup to manually select the sample").place(x=150, y=60, anchor='center')
        self.lbl_cmd_mc4 = tk.Label(self, text="numbers listed in the work order.").place(x=150, y=80, anchor='center')

        self.lbl_cmd_s1 = tk.Label(self, text="Sample Set #1: ").place(x=20, y=125)

        self.lbl_out_dd = tk.Label(self, text="Dioptic Sizes")
        self.lbl_out_dd.config(font='helvetica 12 bold')
        self.lbl_out_dd.place(x=400, y=90, anchor='center')

        entry_s1 = tk.Entry(self, width=10)
        entry_s1.focus_set()  # Places cursor in the first entry box.
        entry_s1.place(x=150, y=125)

        self.lbl_dis_s1 = tk.Label(self, text="# of Samples: ").place(x=500, y=125)

        set = int(0)
        sum_tot = int(0)

        def get_all(entry_s1):
            s1 = entry_s1.get()

        #########      Sample Entry #1       #########
            if s1.isdigit():
                set = int(1)
                try:
                    s1_int = int(s1)
                    sum_tot = s1_int
                except ValueError:  # Close Try 1
                    set = int(0)
            else:   # Close Loop 1
                pass
            print("s1: ", s1)
            
        #btn_pres_cnt = 1  # setting count to 0 to be able to call it a global variable within the function
        def pink(event):
            print("pink")
        #    global btn_pres_cnt  # initializing btn_pres_cnt as a global varaible so that it adds through every iteration
        ##    if (
        ##            btn_pres_cnt == 5 or btn_pres_cnt == 10 or btn_pres_cnt == 15 or btn_pres_cnt == 20 or btn_pres_cnt == 25):  # button turns pink when btn_pres_cnt=100, and =200 and = 300.
        ##        style.map('T.TButton', background=[('active', 'pressed', '#FF69B4'), ('!active', 'white'), (
        ##            'active', '!pressed', 'grey')])  # only the button being pressed turns hot pink
        ##        style.configure('T.Button', font=('Helvetica', '12', 'bold'))
        ##    else:  # else is the normal style
        ##        style.map('T.TButton',
        ##                  background=[('active', 'pressed', 'white'), ('!active', 'white'),
        ##                              ('active', '!pressed', 'grey')])
        ##        style.configure('T.Button', font=('Helvetica', '12', 'bold'))
        #    print('btn_pres_cnt = ', btn_pres_cnt)
        #    btn_pres_cnt += 1  # This is always executed at the end of the if else

        self.btn_no1 = tk.Button(self, text='Manual', width=5, command=self.open_mine1)
        self.btn_no1.bind('<Button-1>', pink)
        self.btn_no1.place(x=250, y=120)

        self.btn_dis = tk.Button(self, text='Display ALL', command=self.display).place(x=10, y=150)

        self.btn_clr1 = tk.Button(self, text='Clear#1', command=self.clear1).place(x=520, y=20)

        self.btn_save = tk.Button(self, text='Save & Close', width=7, command=self.save)
        self.btn_save.bind('<Button-1>', self.display)
        self.btn_save.place(x=525, y=550)

        self.btn_quit = tk.Button(self, text='Quit', width=7, command=self.quit)
        self.btn_quit.place(x=625, y=550)

    def display(self):                          # when the save button is selected in minesweep, it writes to this GUI screen
        samp_arr1.sort(reverse=False)           # sort in ascending order.
        self.lbl_out_s1 = tk.Label(self, text=', '.join(map(str, samp_arr1))).place(x=625, y=135, anchor='w')
        print(f"The array from mine 1 is: ", ', '.join(map(str, samp_arr1)))

    def open_mine1(self):
        mineone = Mine1()
        mineone.grab_set()

    def clear1(self):
        samp_arr1.clear()
        print("List after .clear() ", samp_arr1)
        self.lbl_clr1 = tk.Label(self, text="                                                                     "
                                            "                                                                     "
                                            "                                        ").place(x=95, y=30, anchor='w')

        self.btn_save = tk.Button(self, text='Save & Close', command=self.save).place(x=450, y=150)
        self.btn_save = tk.Button(self, text='Exit', command=self.quit).place(x=550, y=150)

    def save(self):
        print(
            "We don't actually need to do anything with this button. It just makes people comfortable to press save...")
        self.destroy()

    def quit(self):
        print("Exit, info would be saved if we don't quit. And if someone is quitting, they clearly don't want to save the info. So let's clear all info before exiting. first. ")
        clearALL(self)
        self.destroy()

if __name__ == "__main__":
    dio = Dioptics()
    dio.mainloop()
