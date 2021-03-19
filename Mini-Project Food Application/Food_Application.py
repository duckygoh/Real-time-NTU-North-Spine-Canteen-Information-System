import tkinter as tk
import datetime as dt
import pygame
import pyttsx3
import calendar
import urllib.request
import re
import pickle
import threading
from datetime import datetime
from tkinter import messagebox
from tkcalendar import DateEntry
from bs4 import BeautifulSoup

# CREATED BY HARISH
# FUNCTION TO FETCH MENU FROM TXT
def read_menu():
    file_name = "menu.txt"
    fileObject = open(file_name, 'rb')
    global menu
    menu = pickle.load(fileObject)
    fileObject.close()
    return menu

read_menu();

# CREATED BY HARISH
# FUNCTION TO FETCH STORE INFORMATION FROM TXT
def read_store_data():
    file_name = "store.txt"
    fileObject = open(file_name, 'rb')
    global store_list
    global operating_hours1
    global queue_time_calculator
    global operating_hours2
    global menu_switch_time
    
    store_list = pickle.load(fileObject)
    operating_hours1 = pickle.load(fileObject)
    queue_time_calculator = pickle.load(fileObject)
    operating_hours2 = pickle.load(fileObject)
    menu_switch_time = pickle.load(fileObject)
    fileObject.close()
    return menu_switch_time, store_list, operating_hours1, queue_time_calculator, operating_hours2
    
read_store_data();    

### CODE FOR THE PROGRAM TO SWITCH FRAMES AND SETTING THE LANDING FRAME ###
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

### PROPERTIES OF THE LANDING PAGE ###
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        pygame.init()
        pygame.mixer.music.load("voices/landing.mp3")
        pygame.mixer.music.play() 
        header_frame = tk.Frame()
        header_frame.place(relwidth=1.0, relheight=1.0)
        background_image=tk.PhotoImage(file = "image/bg.gif")
        background_label = tk.Label(header_frame, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        tk.Label(header_frame, text="Welcome to NTU North Spine", font=('Fixedsys', 17, "bold"), width = 30).pack(side="top", fill="both", pady=5)
        photo_burger = tk.PhotoImage(file="image/burger.png")
        photo_burger.image = photo_burger
        view_menu_btn = tk.Button(header_frame, image = photo_burger, text="  View Current Menu!", command=lambda: master.switch_frame(Today_Stores_Button), height=50, width=200, compound="left").pack(pady= 20)
        photo_menu = tk.PhotoImage(file="image/menu.png")
        photo_menu.image = photo_menu
        view_menu_btn = tk.Button(header_frame, image = photo_menu, text="      View All Menu!", command=lambda: master.switch_frame(All_Store_Button), height=50, width=200, compound="left").pack(pady= 20)
        photo_calendar = tk.PhotoImage(file="image/calendar.png")
        photo_calendar.image = photo_calendar
        date_time_btn = tk.Button(header_frame, image = photo_calendar, text=" View by Date and Time!", command=lambda: master.switch_frame(DateTime_Page), height=50, width=200, compound="left").pack(pady = 20)
        photo_clock = tk.PhotoImage(file="image/clock.png")
        photo_clock.image = photo_clock
        op_hour_btn = tk.Button(header_frame, image = photo_clock, text="         Operating Hours!", command=lambda: master.switch_frame(Operating_Hours_Button), height=50, width=200, compound="left").pack(pady = 20)
        photo_queue = tk.PhotoImage(file="image/line.png")
        photo_queue.image = photo_queue
        queue_btn = tk.Button(header_frame, image = photo_queue, text="         Queue Calculator!", command=lambda: master.switch_frame(Calc), height=50, width=200, compound="left").pack(pady = 20)
        photo_exit = tk.PhotoImage(file="image/logout.png")
        photo_exit.image = photo_exit
        exit_btn = tk.Button(header_frame, image = photo_exit, text="           Exit         ", command=lambda self=self:quit(App), height=50, width=200, compound="left").pack(pady = 20)
            
### CODE FOR THE STORE PAGE ###
class StorePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        pygame.init()
        pygame.mixer.music.load("voices/select_store.mp3") 
        pygame.mixer.music.play()
        header_frame = tk.Frame()
        header_frame.place(relwidth=1.0, relheight=1.0)
        background_image=tk.PhotoImage(file = "image/bg.gif")
        background_label = tk.Label(header_frame, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        tk.Label(header_frame, text="Select a Store!", font=('Fixedsys', 17, "bold"), width = 55).pack(side="top", fill="x", pady=5)

# VIEW CURRENT STORES MENU BASED ON SYSTEM TIME
class Today_Stores_Button(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        pygame.init()
        pygame.mixer.music.load("voices/select_store.mp3") 
        pygame.mixer.music.play() 
        header_frame = tk.Frame()
        header_frame.place(relwidth=1.0, relheight=1.0)
        background_image=tk.PhotoImage(file = "image/bg.gif")
        background_label = tk.Label(header_frame, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        tk.Label(header_frame, text="View Current Menu", font=('Fixedsys', 17, "bold"),width = 55).pack(side="top", fill="x", pady=5)
        (tk.Label(master, text= 'Select Store', font=('Fixedsys', 10))).place(relheight = 0.025, relwidth = 0.12, relx = 0.05, rely = 0.10)
          
        # CREATED BY OWEN CHIANG
        def assign_store(selection):
            # FETCH CURRENT SYSTEM TIME AND FORMAT
            current_time = int((dt.datetime.now()).strftime("%H%M"))
            # FETCH CURRENT SYSTEM DATE AND FORMAT
            current_day= (dt.datetime.now()).strftime("%A")
            # ASSIGN OLD OR EVEN DAY
            if (current_day == 'Tuesday'or current_day == 'Thursday'or current_day == 'Saturday'):
                oddeven = 'even'
            else:
                oddeven= 'odd'
            # ASSIGN AM OR PM
            if(int(menu_switch_time[selection])> current_time):
                am_pm_select= 'am'
            else:
                am_pm_select= 'pm'
            # DISPLAY THE RIGHT MENU IF DEFINED TIME AND DATE FALLS IN THE OPENING HOUR OF THE STORE
            if int(operating_hours2[selection][current_day]['Opening'])<= current_time < int(operating_hours2[selection][current_day]['Closing']):
                show_menu = menu[selection][oddeven][am_pm_select]
                
            else:
                show_menu = 'Store is currently closed \n store operating hours are\n' + operating_hours1[selection]                          
                            
            op_display = tk.Label(text = show_menu , font=('Fixedsys', 20, "bold"))
            op_display.place(relheight = 0.4, relwidth = 0.6, relx = 0.2, rely = 0.20)
        
        variable = tk.StringVar(header_frame)
        variable.set("Select Store")
        
        global store_sel

        selection = tk.OptionMenu(header_frame, variable, *store_list ,command = assign_store)
        selection.place(relheight = 0.05, relwidth = 0.6, relx = 0.2, rely = 0.10) 
        no_selection = tk.Label(text = " " , font=('Fixedsys', 20, "bold"))
        no_selection.place(relheight = 0.4, relwidth = 0.6, relx = 0.2, rely = 0.20)   
        tk.Button(header_frame, text="Go back to start page", command=lambda: master.switch_frame(StartPage)).place(relheight = 0.05, relwidth = 0.6, relx = 0.2, rely = 0.70)

class All_Store_Button(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        pygame.init()
        pygame.mixer.music.load("voices/select_store.mp3")
        pygame.mixer.music.play()
        header_frame = tk.Frame()
        header_frame.place(relwidth=1.0, relheight=1.0)
        background_image=tk.PhotoImage(file = "image/bg.gif")
        background_label = tk.Label(header_frame, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        tk.Label(header_frame, text="View All Menu", font=('Fixedsys', 17, "bold"),width = 55).pack(side="top", fill="x", pady=5)
        
        (tk.Label(master, text= 'Select Store', font=('Fixedsys', 10))).place(relheight = 0.025, relwidth = 0.12, relx = 0.05, rely = 0.10)
          
        # CREATED BY OWEN CHIANG
        def assign_store(selection):
            # DISPLYING ALL POSSIBLE STORE MENU
            show_menu1 = 'Monday, Wednesday and Friday AM Menu\n' +menu[selection]['odd']['am']
            show_menu2 = 'Monday, Wednesday and Friday PM Menu\n' +menu[selection]['odd']['pm']
            show_menu3 = 'Tuesday, Tuesday and Saturday AM Menu\n' +menu[selection]['even']['am']
            show_menu4 = 'Tuesday, Tuesday and Saturday OM Menu\n' +menu[selection]['even']['pm']           
                            
            op_display = tk.Label(text = show_menu1 , font=('Fixedsys', 12, "bold"))
            op_display.place(relheight = 0.3, relwidth = 0.4, relx = 0.1, rely = 0.20)

            op_display = tk.Label(text = show_menu2 , font=('Fixedsys', 12, "bold"))
            op_display.place(relheight = 0.3, relwidth = 0.4, relx = 0.5, rely = 0.20)

            op_display = tk.Label(text = show_menu3 , font=('Fixedsys', 12, "bold"))
            op_display.place(relheight = 0.3, relwidth = 0.4, relx = 0.1, rely = 0.50)

            op_display = tk.Label(text = show_menu4 , font=('Fixedsys', 12, "bold"))
            op_display.place(relheight = 0.3, relwidth = 0.4, relx = 0.5, rely = 0.50)

        
        variable = tk.StringVar(header_frame)
        variable.set("Select Store")
        global store_sel
        selection = tk.OptionMenu(header_frame, variable, *store_list ,command = assign_store)
        selection.place(relheight = 0.05, relwidth = 0.6, relx = 0.2, rely = 0.10)
        tk.Button(header_frame, text="Go back to start page", command=lambda: master.switch_frame(StartPage)).place(relheight = 0.05, relwidth = 0.6, relx = 0.2, rely = 0.90)

# VIEW OPERATING HOURS OF STORE BASED ON USER SELECTION
class Operating_Hours_Button(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        pygame.init()
        pygame.mixer.music.load("voices/select_store.mp3") 
        pygame.mixer.music.play() 
        header_frame = tk.Frame()
        header_frame.place(relwidth=1.0, relheight=1.0)
        background_image=tk.PhotoImage(file = "image/bg.gif")
        background_label = tk.Label(header_frame, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        tk.Label(header_frame, text="Store Operating Hours", font=('Fixedsys', 17, "bold"),width = 55).pack(side="top", fill="x", pady=5)

        # DONE BY RAYMOND GOH
        # DISPLAYING OPERATING HOURS BASED ON THE STORE SELECTED VIA DROPDOWN MENU
        def assign_store(selection3):
            op_hours =operating_hours1[selection3]
            op_display = tk.Label(text = op_hours , font=('Fixedsys', 20, "bold"))
            op_display.place(relheight = 0.4, relwidth = 0.6, relx = 0.2, rely = 0.20)

        # SETTING DEFAULT VALUE FOR THE DROPDOWN ELEMENT
        variable = tk.StringVar(header_frame)
        variable.set("Select Store")
        global store_sel
        selection3 = tk.OptionMenu(header_frame, variable,*store_list ,command = assign_store)
        selection3.place(relheight = 0.05, relwidth = 0.6, relx = 0.2, rely = 0.10)
        
        no_selection = tk.Label(text = " " , font=('Fixedsys', 20, "bold"))
        no_selection.place(relheight = 0.4, relwidth = 0.6, relx = 0.2, rely = 0.20)
        tk.Button(header_frame, text="Go back to start page", command=lambda: master.switch_frame(StartPage)).place(relheight = 0.05, relwidth = 0.6, relx = 0.2, rely = 0.70)


# DISPLAY MENU BASED ON USER INPUT DATE AND TIME
class DateTime_Page(tk.Frame):
    def __init__(self, master):
        # MAKE ICONS FOR THE PAGE
        tk.Frame.__init__(self, master) 
        pygame.mixer.music.load("voices/date_time.mp3")
        pygame.mixer.music.play() 
        header_frame = tk.Frame()
        header_frame.place(relwidth=1.0, relheight=1.0)
        background_image=tk.PhotoImage(file = "image/bg.gif")
        background_label = tk.Label(header_frame, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        tk.Label(header_frame, text="Date & Time Selection", font=('Fixedsys', 17, "bold"),width = 55).pack(side="top", fill="x", pady=5)
        (tk.Label(master, text= 'Enter Time \n 24 hour format', font=('Fixedsys', 10))).place(relheight = 0.05, relwidth = 0.12, relx = 0.05, rely = 0.10)
        (tk.Label(master, text= 'Select Date', font=('Fixedsys', 10))).place(relheight = 0.025, relwidth = 0.12, relx = 0.05, rely = 0.20)
        (tk.Label(master, text= 'Select Store', font=('Fixedsys', 10))).place(relheight = 0.025, relwidth = 0.12, relx = 0.05, rely = 0.30)
 
        # CREATED BY RAYMOND GOH
        # FUNCTION TO LIMIT THE ENTRYBOX TO ONLY NUMERICAL CHARACTERS
        class int_only(tk.Entry):
            def __init__(self, master=None, **kwargs):
                self.var = tk.StringVar()
                tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
                self.old_value = ''
                self.var.trace('w', self.check)
                self.get, self.set = self.var.get, self.var.set
            def check(self, *args):
                if self.get().isdigit(): 
                    # THE CURRENT VALUE IS ONLY DIGITS; ALLOW THIS
                    self.old_value = self.get()
                else:
                    # THERE'S NON-DIGIT CHARACTERS IN THE INPUT; REJECT THIS 
                    self.set(self.old_value)

        def date_time_compare():
            # CREATED BY OWEN CHIANG
            def print_sel(e):
                get_date = cal.get_date()
                get_date = get_date.strftime('%m/%d/%Y')
                month, day , year = (int(x) for x in get_date.split('/'))
                ans = dt.date(year, month, day)
                global current_day2
                check_date(ans)
                current_day2 = ans.strftime("%A")

            # CREATED BY OWEN CHIANG
            # CHECK FOR PUBLIC HOLIDAY
            def check_date(ans):
                if ans in holiday_list:
                    messagebox.showerror( "It's a public holiday.","The north spine canteen is closed. \n Select another date.")
                    cal.set_date(datetime.today())

            # CREATED BY OWEN CHIANG
            def assign_store(selection2):
                try:
                    time_check = str(int(time_input.get()))
                    min_list = ["6","7","8","9"]
                    if time_check[2] in min_list:
                        messagebox.showerror("Input Error", "Please input value between 0000 to 2359!")
                        return None
                    # CHECK USER TIME INPUT IS BETWEEN 0000 AND 2359
                    if int(time_input.get()) > 2359 or int(time_input.get()) < 0:
                        messagebox.showerror("Input Error", "Please input value between 0000 to 2359!")
                        return None
                    # IF INPUT IS VALID, FETCH TIME INPUT
                    else:
                        current_time2=int(time_input.get())
                    # ASSIGN ODD OR EVEN DAY
                    if (current_day2 == 'Tuesday' or current_day2 =="Thursday" or current_day2 =="Saturday"): 
                        oddeven2= 'even'
                    else:
                        oddeven2= 'odd'
                    # ASSIGN AM OR PM
                    if(int(menu_switch_time[selection2])> current_time2):
                        am_pm_select2= 'am'
                    else:
                        am_pm_select2= 'pm'
                    
                    global show_menu2
                    # CHECK IF LENGTH IS IN THE RIGHT FORMAT
                    if len(time_input.get()) != 4:
                        show_menu2 = "Time Invalid!"
                        messagebox.showerror("Input Error", "Enter Valid Time!")
                        op_display = tk.Label(text = show_menu2 , font=('Fixedsys', 20, "bold"))
                        op_display.place(relheight = 0.4, relwidth = 0.6, relx = 0.2, rely = 0.40)
                    else:
                        # SHOW MENU IF ALL INPUTS ARE CORRECT
                        if (int(operating_hours2[selection2][current_day2]['Opening'])<= current_time2 < int(operating_hours2[selection2][current_day2]['Closing'])):
                            show_menu2 = menu[selection2][oddeven2][am_pm_select2]

                        # SHOW OPENING HOURS IF STORE IS CLOSED BASED ON INPUT TIME
                        else:
                            show_menu2 = "Store is currently closed \n store operating hours are \n" +  operating_hours1[selection2]

                    op_display = tk.Label(text = show_menu2 , font=('Fixedsys', 20, "bold"))
                    op_display.place(relheight = 0.4, relwidth = 0.6, relx = 0.2, rely = 0.40)

                # IF WRONG/NO INPUT, PRINT ENTER ALL FIELDS
                except:
                    error_display = tk.Label(text = 'Please enter all fields' , font=('Fixedsys', 20, "bold"))
                    error_display.place(relheight = 0.4, relwidth = 0.6, relx = 0.2, rely = 0.40)
            
            variable = tk.StringVar(header_frame)
            variable.set("Select Store")
            global store_sel
            store_sel = tk.OptionMenu(header_frame, variable, *store_list ,command = assign_store)
            store_sel.place(relheight = 0.05, relwidth = 0.6, relx = 0.2, rely = 0.30)
            
            no_selection = tk.Label(text = " " , font=('Fixedsys', 20, "bold"))
            no_selection.place(relheight = 0.4, relwidth = 0.6, relx = 0.2, rely = 0.40)

            time_input = int_only(header_frame, width=25, font=('Fixedsys', 17, "bold"))
            time_input.place(relheight = 0.05, relwidth = 0.6, relx = 0.2, rely = 0.1)
            
            cal = DateEntry(header_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
            cal.place(relwidth = 0.2, relx = 0.4, rely = 0.20)
            cal.bind("<<DateEntrySelected>>", print_sel)

        date_time_compare();
        tk.Button(header_frame, text="Go back to start page", command=lambda: master.switch_frame(StartPage)).place(relheight = 0.05, relwidth = 0.6, relx = 0.2, rely = 0.90)

### CODE FOR THE QUEUE CALCULATOR
class Calc(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        pygame.mixer.music.load("voices/queue.mp3")
        pygame.mixer.music.play() 
        header_frame = tk.Frame()
        header_frame.place(relwidth=1.0, relheight=1.0)
        background_image=tk.PhotoImage(file = "image/bg.gif")
        background_label = tk.Label(header_frame, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        tk.Label(header_frame, text="Queue Calculator", font=('Fixedsys', 17, "bold"), width = 30).pack(side="top", fill="both", pady=5)

        # CREATED BY RAYMOND GOH
        # FUNCTION TO FETCH THE RESPECTIVE WAITING TIME IN MINS BASED ON THE STORE SELECTED
        def countit(selection):
            global queue_time          
            queue_time = int(queue_time_calculator[selection])
            global storesel
            storesel= selection
            return queue_time

        # SETTING THE DEFAULT DROPDOWN SELECTION 
        variable = tk.StringVar(header_frame)
        variable.set("Select Store")

        w = tk.OptionMenu(header_frame, variable, *queue_time_calculator.keys(), command=countit)
        w.place(relheight = 0.1, relwidth = 0.6, relx = 0.2, rely = 0.25)
        
        # CREATED BY RAYMOND GOH
        # FUNCTION TO LIMIT THE ENTRYBOX TO ONLY NUMERICAL CHARACTERS
        class only_int(tk.Entry):
            def __init__(self, master=None, **kwargs):
                self.var = tk.StringVar()
                tk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
                self.old_value = ''
                self.var.trace('w', self.check)
                self.get, self.set = self.var.get, self.var.set
            def check(self, *args):
                if self.get().isdigit(): 
                    # THE CURRENT VALUE IS ONLY DIGITS; ALLOW THIS
                    self.old_value = self.get()
                else:
                    # THERE'S NON-DIGIT CHARACTERS IN THE INPUT; REJECT THIS 
                    self.set(self.old_value)

        queue_input = only_int(header_frame, width=25, font=('Fixedsys', 17, "bold"))
        queue_input.place(relheight = 0.1, relwidth = 0.6, relx = 0.2, rely = 0.1)

        # CREATED BY RAYMOND GOH 
        # CATCHING USER INPUT HERE 
        def result():
            try:
                # CATCHING USER IF THEY ENTER VALUE LESS THAN 1 AND MORE THAN 50
                if int(queue_input.get()) > 50 or int(queue_input.get()) < 1:
                    messagebox.showerror("Input Error", "Please input value between 1 to 50!")
                    # RESET THE ENTRYBOX VALUE TO 1
                    queue_input.set("1")
                    return None
                queue_input_out = queue_time * int(queue_input.get())
            # CATCHING USER IF STORE NOT SELECTED 
            except NameError:
                messagebox.showerror("Input Error", "Please select store!")
                return None
            # CATCHING USER IF NO VALUE IS BEING INPUT
            except:
                messagebox.showerror("Input Error", "Please input value!")
                return None

            ### COMPUTATION OF THE TOTAL QUEUE TIME ACCORDING TO THE STORE SELECTED WITH LENGTH OF THE QUEUE ###
            # FETCHING CURRENT SYSTEM TIME
            now = dt.datetime.now()
            # ADDING NUMBER OF MINS TO CURRENT SYSTEM TIME ACCORDING TO LENGTH OF QUEUE
            now_plus = now + dt.timedelta(minutes = queue_input_out)
            # FORMATTING THE TIME OUTPUT
            now_final = int(now_plus.strftime('%H'))*100+int(now_plus.strftime('%M'))
            now_final_covt = str(int(now_plus.strftime('%H'))*100+int(now_plus.strftime('%M')))
            # ADDING A COLON IN THE TIME FORMAT
            if len(now_final_covt) == 4:
                now_final_covt = now_final_covt[:2] + ':' + now_final_covt[2:]
            else:
                now_final_covt = now_final_covt[:1] + ':' + now_final_covt[1:]
            # STRING TO DISPLAY OUTPUT BACK TO THE USER
            final_form = "Estimated queuing time will be\n" + str(queue_input_out) + " mins\n" \
                         + "Join the queue now to place order at\n" + now_final_covt

            # FORMATTING THE DAY
            current_day= (dt.datetime.now()).strftime("%A")
            # CHECK IF THE TIME IS WITHIN OPERATING HOURS OF THE SELECTED STORE UPON ORDERING OF FOOD
            if (int(operating_hours2[storesel][current_day]['Opening'])<= now_final < int(operating_hours2[storesel][current_day]['Closing'])):
                overtimecheck= " "
                def display_good():
                    display = tk.Label(header_frame, text = final_form , font=('Fixedsys', 16, "bold"))
                    display.place(relheight = 0.2, relwidth = 0.6, relx = 0.2, rely = 0.40)
                #CODE FOR THE TEXT TO SPEECH FUNCTION TO READ THE TOTAL QUEUE TIME IN MINS
                def voice_good():
                    engine = pyttsx3.init()
                    engine.setProperty('rate',180)  #180 words per minute
                    engine.setProperty('volume',0.9)
                    engine.say("Estimated queuing time will be\n" + str(queue_input_out) + " mins\n")
                    engine.runAndWait()

                # CREATED BY RAYMOND GOH
                # USE THREADING TO RUN FUNCTIONS AT THE SAME TIME
                task_display = threading.Thread(target = display_good)
                task_display.start()
                task_speak = threading.Thread(target = voice_good)
                task_speak.start()
                
            # IF ORDER TIME BEYOND OPERATING HOURS, RUN THIS
            else:
                overtimecheck= "\nToo late! Store is closed\n or will close before you can place your order!"
                #CODE FOR THE TEXT TO SPEECH FUNCTION TO READ THE TOTAL QUEUE TIME IN MINS
                def display_bad():
                    display = tk.Label(header_frame, text = overtimecheck, font=('Fixedsys', 16, "bold"))
                    display.place(relheight = 0.2, relwidth = 0.6, relx = 0.2, rely = 0.40)
                def voice_bad():
                    engine = pyttsx3.init()
                    engine.setProperty('rate',180)  #180 words per minute
                    engine.setProperty('volume',0.8) 
                    engine.say("Too late! Store is closed or will close before you can place your order!")
                    engine.runAndWait()

                task_display = threading.Thread(target = display_bad)
                task_display.start()
                task_speak = threading.Thread(target = voice_bad)
                task_speak.start()

        button_calc =tk.Button(header_frame, text ="Calculate", font=('Fixedsys', 16, "bold"), command=result)
        button_calc.place(relheight = 0.1, relwidth = 0.6, relx = 0.2, rely = 0.65)
        tk.Button(header_frame, text="Go Back to Main Page", font = ('Fixedsys', 14, "bold"),
                  command=lambda: master.switch_frame(StartPage)).place(relheight = 0.1, relwidth = 0.4, relx = 0.3, rely = 0.85)
    

# CREATED BY RAYMOND GOH 
# FUNCTION TO HARVEST DATA FROM MOM'S WEBSITE TO FETCH PUBLIC HOLIDAY LIST
holiday_list = []

def fetch_from_mom():
    url = "https://www.mom.gov.sg/newsroom/press-releases/2018/0404-public-holidays-for-2019"
    # CONNECT THE PROGRAM WITH MOM'S WEBSITE
    page = urllib.request.urlopen(url)

    soup = BeautifulSoup(page, 'html.parser')

    ph_list = []
    # FOR LOOP TO FETCH ALL DATA FROM THE TABLE OF THE SITE
    for link in soup.findAll('td'):
        if "*" in link.text:
            link = link.text.replace("*", "") # REMOVE ASTERISKS FROM SOME OF THE DATES
            ph_list.append(link)
        else:
            ph_list.append(link.text)

    global holiday_list

    # FOR LOOP TO GET ONLY DATE OF PUBLIC HOLIDAY FROM THE TABLE
    # APPEND ALL PUBLIC HOLIDAY TO A LIST
    for element in ph_list:
        if not element.isalpha():
            if "2019" in element:
                holiday_list.append(datetime.strptime(element, '%d %b %Y').date())


#### INITIATING THE PROGRAM, SETTING PROGRAM TITLE AND WINDOW SIZE OF THE PROGRAM ###
if __name__ == "__main__":
    try:
        print("\nPlease be patience while the application loads, it is in the midst of harvesting data upon launching.\nIf you are concerned about this, please disable/comment out the code from line 530 to 535.")
        print("Fetching will skip if there is no internet connectivity.")
        fetch_from_mom()
    except:
        pass
    app = App()
    app.title("Food System")
    app.geometry("1000x700")
    app.mainloop()
    
