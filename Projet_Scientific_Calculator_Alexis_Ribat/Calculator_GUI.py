from tkinter import*
import math

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
    
def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("0")
    
def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = sumup
    
    
def Pourcentage():
    global operator
    sumup = eval(operator)/100
    text_Input.set(sumup)
    operator = ""

def ChangeSign():
    global operator
    operator = - float(operator)
    text_Input.set(operator)
    #operator = ""
    
def b1surx():
    global operator
    operator = float(1/(float(operator)))
    text_Input.set(operator)
    #operator = ""
    
    
def Rnd():
    global operator
    
    operator = round((float(operator)),2)
    text_Input.set(operator)
    #operator = ""
    
def Factorial():
    global operator
    operator = math.factorial(float(operator))
    text_Input.set(operator)
    #operator = ""
    
def M_sub():
    global operator
    operator = math.factorial(float(operator))
    text_Input.set(operator)
    #operator = ""
    
def Log():
    global operator
    operator = math.log10(float(operator))
    text_Input.set(operator)
    #operator = ""
    
def Ln():
    global operator
    operator = math.log2(float(operator))
    text_Input.set(operator)
    #operator = ""
    
def Expo():
    global operator
    operator = math.log2(float(operator))
    text_Input.set(operator)
    #operator = ""
    
def Squarex():
    global operator
    operator = math.sqrt(float(operator))
    text_Input.set(operator)
    #operator = ""
    
def Cosx():
    global operator
    operator = math.cos(float(operator))
    text_Input.set(operator)
    #operator = ""
    
def Sinx():
    global operator
    operator = math.sin(float(operator))
    text_Input.set(operator)
    #operator = ""
    
def Tanx():
    global operator
    operator = math.tan(float(operator))
    text_Input.set(operator)
    #operator = ""
    
def Acosx():
    global operator
    operator = math.acos(float(operator))
    text_Input.set(operator)
    #operator = ""
    
def Asinx():
    global operator
    operator = math.asin(float(operator))
    text_Input.set(operator)
    #operator = ""
    
def Atanx():
    global operator
    operator = math.atan(float(operator))
    text_Input.set(operator)
    #operator = ""


#==============================================================

cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()



txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable = text_Input, bd = 30, insertwidth = 4,
                   bg = "powder blue", justify = 'right').grid(columnspan = 4)
                   
                   
#==============================row 2===============================

btnsinus = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="sin", bg ="powder blue", command=Sinx).grid(row=2, column=0)
              
btcosinus = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="cos", bg ="powder blue", command=Cosx).grid(row=2, column=1)
              
btntan = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="tan", bg ="powder blue", command=Tanx).grid(row=2, column=2)
              
btne = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="e", bg ="powder blue", command=lambda:btnClick(math.e)).grid(row=2, column=3)

#==============================row 3===============================

btnarcsinus = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="sin-1", bg ="powder blue", command=Asinx).grid(row=3, column=0)
              
btnarcosinus = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="cos-1", bg ="powder blue", command=Acosx).grid(row=3, column=1)
              
btnarctan = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="tan-1", bg ="powder blue", command=Atanx).grid(row=3, column=2)
              
btnpi = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="n", bg ="powder blue", command=lambda:btnClick(math.pi)).grid(row=3, column=3)
              

#==============================row 4===============================

btnfactiorielle = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="n!", bg ="powder blue", command=Factorial).grid(row=4, column=0)
              
btnlog = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="log", bg ="powder blue", command=Log).grid(row=4, column=1)
             
btnsquarex = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="Vx", bg ="powder blue", command=Squarex).grid(row=4, column=2)
              
btnln = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="ln", bg ="powder blue", command=Ln).grid(row=4, column=3)
              

#==============================row 5===============================


btnpar1 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="(", bg ="powder blue", command=lambda:btnClick("(")).grid(row=5, column=0)

btnpar2 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text=")", bg ="powder blue", command=lambda:btnClick(")")).grid(row=5, column=1)
              
btn1surx = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="1/x", bg ="powder blue", command=b1surx).grid(row=5, column=2)
                   
                   
btnPourcentage = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="%", bg ="powder blue", command=Pourcentage).grid(row=5, column=3)
              
              
#==============================row 6===============================

btn7 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="7", bg ="powder blue", command=lambda:btnClick(7)).grid(row=6, column=0)
   
btn8 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="8", bg ="powder blue", command=lambda:btnClick(8)).grid(row=6, column=1)
              
btn9 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="9", bg ="powder blue", command=lambda:btnClick(9)).grid(row=6, column=2)
   
Addition = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="+", bg ="white", command=lambda:btnClick("+")).grid(row=6, column=3)   

                                             
#==============================row 7===============================

btn4 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="4", bg ="powder blue", command=lambda:btnClick(4)).grid(row=7, column=0)
   
btn5 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="5", bg ="powder blue", command=lambda:btnClick(5)).grid(row=7, column=1)
              
btn6 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="6", bg ="powder blue", command=lambda:btnClick(6)).grid(row=7, column=2)

Substraction = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="-", bg ="white", command=lambda:btnClick("-")).grid(row=7, column=3) 
                              
#==============================row 8===============================

btn3 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="3", bg ="powder blue", command=lambda:btnClick(3)).grid(row=8, column=0)
   
btn2 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="2", bg ="powder blue", command=lambda:btnClick(2)).grid(row=8, column=1)
              
btn1 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="1", bg ="powder blue", command=lambda:btnClick(1)).grid(row=8 , column=2)

Multiply = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="*", bg ="white", command=lambda:btnClick("*")).grid(row=8, column=3)
                          

#==============================row 9===============================
btn0 = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="0", bg ="powder blue", command=lambda:btnClick(0)).grid(row=9, column=0)
 
btnpoint = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text=".", bg ="powder blue", command=lambda:btnClick(".")).grid(row=9 , column=1)

btnExp = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="EXP", bg ="powder blue", command=lambda:btnClick(".")).grid(row=9 , column=2)
 
Division = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="/", bg ="white", command=lambda:btnClick("/")).grid(row=9, column=3)

              
#==============================row 10==============================

btnChangeSign = Button(cal, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="+/-", bg ="white", command=ChangeSign).grid(row=10, column=0)
              
btnRnd = Button(cal, padx=12, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="RND", bg ="white", command=Rnd).grid(row=10, column=1)

btnClear = Button(cal, padx=16, bd=8, fg="white", font=('arial', 20, 'bold'),
              text="C", bg ="red", command=btnClearDisplay).grid(row=10, column=2)
    

btnEquals = Button(cal, padx=16, bd=8, fg="white", font=('arial', 20, 'bold'),
              text="=", bg ="red", command=btnEqualsInput).grid(row=10, column=3)
              


cal.mainloop()