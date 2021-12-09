from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

            scvalue.set(value)
            screen.update()

    elif text == 'C':
            scvalue.set("")
            screen.update()
    else:
            scvalue.set(scvalue.get()+ text)
            screen.update()



window = Tk()
window.geometry("608x650")
window.minsize(608,650)
window.maxsize(608,652)
window.config(bg="gray")
window.title("calculator XD")




scvalue = StringVar()
scvalue.set("")
f=Frame(window,pad= 20,pady=20)
screen =Entry(f,textvar=scvTalue,font="lucida 50 bold",bg='light blue')

screen.pack(fill=X,pad=20,pady=15)
f.pack()
Y


options1 =["7","8","9","+"]
options2 = ["4","5","6","-"]
option3 = ["1","2","3","*"]
option4 = ["0","C","=","/"]


f=Frame(winwos,bg="black",padx=30,pady=10)

for i in option3:
    b= Button(f,text=i,padx=10,font="lucida 25  bold")
    b.pack(side=LEFT,padx=10,pady=10)
    b.blind("<Button-1>",click)
f.pack()


f=Frame(winwos,bg="black",padx=30,pady=10)

for i in option4:
    b= Button(f,text=i,padx=10,font="lucida 25  bold")
    b.pack(side=LEFT,padx=10,pady=10)
    b.blind("<Button-1>",click)
f.pack()

window.mainloop()
