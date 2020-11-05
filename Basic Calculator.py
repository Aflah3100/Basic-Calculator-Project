#BASIC CALCULATOR CODE AREA.

#IMPORT SECTIONS
from tkinter import *

#********************************CREATING WINDWS FOR THE CALCULATOR*************************


root=Tk()
root.geometry('355x475')
root.title('BASIC CALCULATOR')
root.configure(bg='light blue')
root.resizable(width=False,height=False)



#CREATING FRAME FOR THE CALCULATOR


main_frame=Frame(root,relief='raised',bg='#20B2AA')
main_frame.pack()

#CREATING DISPLAY FIELD
equation=StringVar()

display_text=Entry(main_frame,textvariable=equation,justify='right',relief='raised',font=('arial',20,'bold'),bg='#8DB6CD',insertwidth=4,bd=2)
display_text.grid(row=0,column=0,columnspan=4,ipady=25,pady=20,ipadx=8)

#FUNCTION DECLARATION AREA
expression=""

def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)

def cancelpress():
    global expression
    equation.set("0")
    expression=""

def equalpress():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except:
        ZeroDivisionError
        equation.set("ERROR!")

def pressoff():
    global expression
    equation.set("")
    expression=""

def pressonn():
    global expression
    equation.set("WELCOME!!!")
    expression=""

def pressclean():
    global expression
    equation.set("CLEANED!!!")
    expression=""






#CREATING BUTTONS

button_7=Button(main_frame,text='7',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :press(7))
button_7.grid(row=1,column=0)

button_8=Button(main_frame,text='8',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :press(8))
button_8.grid(row=1,column=1)

button_9=Button(main_frame,text='9',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :press(9))
button_9.grid(row=1,column=2)

button_4=Button(main_frame,text='4',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :press(4))
button_4.grid(row=2,column=0)

button_5=Button(main_frame,text='5',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :press(5))
button_5.grid(row=2,column=1)

button_6=Button(main_frame,text='6',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :press(6))
button_6.grid(row=2,column=2)

button_1=Button(main_frame,text='1',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :press(1))
button_1.grid(row=3,column=0)

button_2=Button(main_frame,text='2',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :press(2))
button_2.grid(row=3,column=1)

button_3=Button(main_frame,text='3',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :press(3))
button_3.grid(row=3,column=2)

button_0=Button(main_frame,text='0',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :press(0))
button_0.grid(row=4,column=0)

decimal=Button(main_frame,text='.',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :press('.'))
decimal.grid(row=4,column=1)

button_cancel=Button(main_frame,text='C',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :cancelpress())
button_cancel.grid(row=4,column=2)

button_equal=Button(main_frame,text='=',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :equalpress())
button_equal.grid(row=5,column=0)

button_add=Button(main_frame,text='+',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :press('+'))
button_add.grid(row=1,column=3)

button_subt=Button(main_frame,text='-',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :press('-'))
button_subt.grid(row=2,column=3)

button_multiply=Button(main_frame,text='*',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :press('*'))
button_multiply.grid(row=3,column=3)

button_divide=Button(main_frame,text='/',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :press('/'))
button_divide.grid(row=4,column=3)

button_off=Button(main_frame,text='OFF!',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :pressoff())
button_off.grid(row=5,column=1)

button_onn=Button(main_frame,text='ON',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :pressonn())
button_onn.grid(row=5,column=2)

button_clean=Button(main_frame,text='Clean',font=('times new roman',12,'bold'),relief='ridge',bd=1,fg='black',bg='#20B2AA',width=8,height=3,command=lambda :pressclean())
button_clean.grid(row=5,column=3)













root.mainloop()


#CREATED BY:AFLAH SEDHIQUE
#PUSHED TO GIT HUB(aflah3100@gmail.com)
