from tkinter import *

#%%
def button_click(number):
    current = myEntry.get()
    myEntry.delete(0, END)
    myEntry.insert(0, str(current) + str(number))
    
def butt_clear():
    myEntry.delete(0, END)

def butt_equal():
    second_number = myEntry.get()
    myEntry.delete(0, END)
    
    if math == "addition":
        myEntry.insert(0, f_num + int(second_number))
    if math == "subtraction":
        myEntry.insert(0, f_num - int(second_number))
    if math == "division":
        myEntry.insert(0, f_num / int(second_number))
    if math == "multiplication":
        myEntry.insert(0, f_num * int(second_number))
    
def butt_add():
    first_number = myEntry.get()
    
    global f_num
    f_num = int(first_number)
    global math
    math = "addition"
    
    myEntry.delete(0, END)
    
def butt_divide():
    first_number = myEntry.get()
    
    global f_num
    f_num = int(first_number)
    global math
    math = "division"
    
    myEntry.delete(0, END)
    
def butt_multiply():
    first_number = myEntry.get()
    
    global f_num
    f_num = int(first_number)
    global math
    math = "multiplication"
    
    myEntry.delete(0, END)
    
def butt_subtract():
    first_number = myEntry.get()
    
    global f_num
    f_num = int(first_number)
    global math
    math = "subtraction"
    
    myEntry.delete(0, END)

#%%

root = Tk()
root.title("Simple Calculator")

myEntry= Entry(root, width= 35, borderwidth= 4)
myEntry.grid(row= 0, column= 0, columnspan=3, padx=10, pady=10)

# Define Buttons
button_1 = Button(root, text="1", padx=40, pady=20, command= lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command= lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command= lambda: button_click(3))

button_4 = Button(root, text="4", padx=40, pady=20, command= lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command= lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command= lambda: button_click(6))

button_7 = Button(root, text="7", padx=40, pady=20, command= lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command= lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command= lambda: button_click(9))

button_0 = Button(root, text="0", padx=40, pady=20, command= lambda: button_click(0))

button_add = Button(root, text="+", padx= 39, pady=20, command= butt_add)
button_subtract = Button(root, text="-", padx= 40, pady=20, command= butt_subtract)
button_divide = Button(root, text="/", padx= 40, pady=20, command= butt_divide)
button_multiply = Button(root, text="*", padx= 40, pady=20, command= butt_multiply)

button_equal = Button(root, text="=", padx= 87, pady=20, command= butt_equal)
button_clear = Button(root, text="CLEAR", padx= 74, pady=20, command= butt_clear)

# Button Location

button_1.grid(row=3 , column= 0)
button_2.grid(row=3 , column= 1)
button_3.grid(row=3 , column= 2)

button_4.grid(row=2 , column= 0)
button_5.grid(row=2 , column= 1)
button_6.grid(row=2 , column= 2)

button_7.grid(row=1 , column= 0)
button_8.grid(row=1 , column= 1)
button_9.grid(row=1 , column= 2)

button_0.grid(row=4 , column= 0)

button_equal.grid(row=4 , column= 1, columnspan=2)
button_clear.grid(row=5 , column= 1,  columnspan=2)

button_add.grid(row=5 , column= 0)
button_subtract.grid(row=6 , column= 0)
button_divide.grid(row=6 , column= 1)
button_multiply.grid(row=6 , column= 2)


root.mainloop()




























