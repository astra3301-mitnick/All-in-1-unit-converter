from tkinter import *

lay=[]
root = Tk()
root.geometry('500x500+100+50')
root.title("Main Window")

def create():

    top = Toplevel()
    lay.append(top)

    top.title("Second Window")
    top.geometry('500x500+100+450')
    msg = Message(top,width=100)
    msg.pack()

    def exit_btn():

        top.destroy()
        top.update()



    btn = Button(top,text='QUIT',bg="yellow", fg="blue", font=("Arial", 14, "bold"), relief=SUNKEN, bd=5,
                    justify=CENTER, highlightbackground="red", overrelief=GROOVE, activebackground="green",
                    activeforeground="blue",command=exit_btn)
    btn.pack()



labelButton = Label(root, text="hey chu i gotcha a tkinter empty window .\n"
                               "so you can now create a new window and quit the created one.\n"
                               "Gotta getcha guys in the nex one \n").pack()
Button(root, text="Create  a new window", command=create).pack(padx=25, pady=25)
mainloop()

































































































































