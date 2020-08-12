from tkinter import *
from tkinter import messagebox
from functions import functions

f=functions()

window = Tk()
window.geometry('300x400')
window.resizable(0,0)
window.configure(bg="#263D42")
window.title('Auto presente')
window.iconbitmap('icon.ico')

frame = Frame(window, bg="#263D42")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)

debug = BooleanVar()
filemenu.add_checkbutton(label="Debug mode", variable=debug,onvalue=True, offvalue=False,command= lambda: f._debug(debug))


filemenu.add_separator()

filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

T_filtro = IntVar()
T_filtro.set(2)
T_filtro.get()
filter_menu = Menu(menubar, tearoff=0)

filter_menu.add_radiobutton(label="Filtro Absoluto",variable=T_filtro, value=1)
filter_menu.add_radiobutton(label="Filtro Parcial",variable=T_filtro, value=2)

filter_menu.add_separator()

CamelCase = BooleanVar()
filter_menu.add_checkbutton(label="Solo CamelCase",variable=CamelCase,onvalue=True, offvalue=False,command= lambda: f._CamelCase(CamelCase))
negativo = BooleanVar()
negativo.set(True)
filter_menu.add_checkbutton(label="Negativos exclullentes",variable=negativo,onvalue=True, offvalue=False,command= lambda: f._Negative(negativo))



menubar.add_cascade(label="Filtros", menu=filter_menu)


name_label = Label(frame, text = "nombre del cotacto o grupo:",font = "helvetica 13")
name_label.pack()
name_box = Entry(frame, font = "helvetica 13", justify = "center")
name_box.pack()

message_label = Label(frame, text = "mensaje a enviar:",font = "helvetica 13")
message_label.pack()
message_box = Entry(frame, font = "helvetica 13", justify ="center")
message_box.pack()

hour_1_label = Label(frame, text = "hora de inicio:",font = "helvetica 13")
hour_1_label.pack()
hour_1_box = Entry(frame,font = "helvetica 13", justify = "center")
hour_1_box.insert(3, ":")
hour_1_box.pack()

hour_2_label = Label(frame, text = "hora final",font = "helvetica 13")
hour_2_label.pack()
hour_2_box = Entry(frame,font = "helvetica 13", justify = "center")
hour_2_box.insert(3, ":")
hour_2_box.pack()

filtro_label = Label(frame, text = "filtro",font = "helvetica 13")
filtro_label.pack()
filtro_box = Entry(frame,font = "helvetica 13", justify = "center")
filtro_box.pack()

send_buttom = Button(frame, text = "programar",font = "helvetica 13",command= lambda: f.send(name_box,message_box,hour_1_box,hour_2_box,filtro_box,T_filtro))
send_buttom.pack()

window.configure(menu=menubar)
window.mainloop()