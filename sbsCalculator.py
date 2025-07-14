import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("SBS Calculator")
window.geometry("450x550")
window.resizable(False,False)

inputVar = tk.StringVar()

f1 = ttk.Frame(master=window,borderwidth=1,relief="solid")
l1 = ttk.Label(text="Sri B.S Tech",font="calibri 15")

f2 = ttk.Frame(master=window)
f3 = ttk.Frame(master=window)
f4 = ttk.Frame(master=window)
f5 = ttk.Frame(master=window)

display = ttk.Entry(master=f1,font="calibri 25",justify="right",textvariable=inputVar)
b1 = ttk.Button(master=f2,text="1",command=lambda:inputVar.set(inputVar.get()+"1")).pack(side="left",expand=True,fill="both")
b2 = ttk.Button(master=f2,text="2",command=lambda:inputVar.set(inputVar.get()+"2")).pack(side="left",expand=True,fill="both")
b3 = ttk.Button(master=f2,text="3",command=lambda:inputVar.set(inputVar.get()+"3")).pack(side="left",expand=True,fill="both")
b4 = ttk.Button(master=f2,text="+",command=lambda:inputVar.set(inputVar.get()+"+")).pack(side="left",expand=True,fill="both")

b5 = ttk.Button(master=f3,text="4",command=lambda:inputVar.set(inputVar.get()+"4")).pack(side="left",expand=True,fill="both")
b6 = ttk.Button(master=f3,text="5",command=lambda:inputVar.set(inputVar.get()+"5")).pack(side="left",expand=True,fill="both")
b7 = ttk.Button(master=f3,text="6",command=lambda:inputVar.set(inputVar.get()+"6")).pack(side="left",expand=True,fill="both")
b8 = ttk.Button(master=f3,text="-",command=lambda:inputVar.set(inputVar.get()+"-")).pack(side="left",expand=True,fill="both")

b9 = ttk.Button(master=f4,text="7",command=lambda:inputVar.set(inputVar.get()+"7")).pack(side="left",expand=True,fill="both")
b10 = ttk.Button(master=f4,text="8",command=lambda:inputVar.set(inputVar.get()+"8")).pack(side="left",expand=True,fill="both")
b11 = ttk.Button(master=f4,text="9",command=lambda:inputVar.set(inputVar.get()+"9")).pack(side="left",expand=True,fill="both")
b12 = ttk.Button(master=f4,text="x",command=lambda:inputVar.set(inputVar.get()+"*")).pack(side="left",expand=True,fill="both")

b13 = ttk.Button(master=f5,text="c",command=lambda:inputVar.set("")).pack(side="left",expand=True,fill="both")
b14 = ttk.Button(master=f5,text="0",command=lambda:inputVar.set(inputVar.get()+"0")).pack(side="left",expand=True,fill="both")
b15 = ttk.Button(master=f5,text="=",command=lambda:inputVar.set(eval(inputVar.get()))).pack(side="left",expand=True,fill="both")
b16 = ttk.Button(master=f5,text="/",command=lambda:inputVar.set(inputVar.get()+"/")).pack(side="left",expand=True,fill="both")


display.pack(fill="both",expand=True)
f1.pack(expand=True,fill="both")
l1.pack(ipady=10)


f2.pack(expand=True,fill="both")
f3.pack(expand=True,fill="both")
f4.pack(expand=True,fill="both")
f5.pack(expand=True,fill="both")
window.mainloop()