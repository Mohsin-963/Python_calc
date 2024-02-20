import tkinter
from tkinter import *

root=Tk()
root.title("CALCULATOR 1.4")
root.geometry("570x620+600+110")
root.resizable(False,False)
root.configure(bg="#17161b")

#Variable for equations
equation =""
#"show" the value on "label_result".
#This will change the "text" of "Label_result" to "equation" which is (equation + concatination + value). # new value will be concatinated.
def show(value):
	global equation
	equation+=value
	label_result.config(text=equation)

#Clear funtion to clear the label text.
def clear():
	global equation
	equation=""
	label_result.config(text=equation)
def B_K():
        global equation
        if equation !="":
        	#deleting one char and converting list back into string.
                x=list(equation)
                L=len(x)
                L-=1
                del x[L]
                i=0
                L-=1
                equation=""
                while L>0:
                	equation+= str(x[i])
                	i+=1
                	L-=1
                label_result.config(text=equation)
        else:
                pass
#Calculate function to do actual calculations.
def calculate():
	global equation
	result =""
	if equation !="":
		try:
			result=eval(equation)
		except:
			result="error"
			equation=""
	label_result.config(text=result)

#Declaration of Label. this will show our result and input from the user.
label_result= Label(root, width=19,bd=4, height=2,text="",bg="#37161b",fg="#fff",font=("arial",30))
label_result.pack()
#Must be placed after label_result is "packed".
label_result.place(x=20,y=9)

#button for the Backspace, removes 1 char per click. Aligned with the Label's right.
Button(root,text="BK",width=3, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#3697f5",command=lambda: B_K()).place(x=480,y=20)

#first Row
Button(root,text="CA",width=5, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#a697f5",command=lambda: clear()).place(x=10,y=115)
Button(root,text="/",width=5, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("/")).place(x=150,y=115)
Button(root,text="%",width=5, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("%")).place(x=290,y=115)
Button(root,text="X",width=5, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("*")).place(x=430,y=115)

#Second Row
Button(root,text="7",width=5, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("7")).place(x=10,y=215)
Button(root,text="8",width=5, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("8")).place(x=150,y=215)
Button(root,text="9",width=5, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("9")).place(x=290,y=215)
Button(root,text="-",width=5, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("-")).place(x=430,y=215)

#Third315
Button(root,text="4",width=5, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("4")).place(x=10,y=315)
Button(root,text="5",width=5, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("5")).place(x=150,y=315)
Button(root,text="6",width=5, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("6")).place(x=290,y=315)
Button(root,text="+",width=5, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("+")).place(x=430,y=315)

#Forth Row
Button(root,text="1",width=5, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("1")).place(x=10,y=415)
Button(root,text="2",width=5, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("2")).place(x=150,y=415)
Button(root,text="3",width=5, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("3")).place(x=290,y=415)

#Fifth Row... 0 width has been increased.
# '=' height increasd. border to 5 to assist.
Button(root,text="0",width=11, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show("0")).place(x=10,y=515)
Button(root,text=".",width=5, height=1,activebackground="#2a2d36", font=("arial",30,"bold"), bd=1, fg="#fff",bg="#2a2d36",command=lambda: show(".")).place(x=290,y=515)
Button(root,text="=",width=5, height=3,activebackground="#2a2d36", font=("arial",30,"bold"), bd=5, fg="#fff",bg="#444444",command=lambda: calculate()).place(x=430,y=415)

root.mainloop()
