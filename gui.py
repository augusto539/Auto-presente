from tkinter import *
from tkinter import messagebox
from functions import functions
from perfiles import perfiles

P = perfiles()
P.inicio()
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

# -------------------------------    FILE MENU      --------------------------------------------------------------------------

filemenu = Menu(menubar, tearoff=0)
debug = BooleanVar()

filemenu.add_checkbutton(label="Debug mode", variable=debug,onvalue=True, offvalue=False,command= lambda: f._debug(debug))

filemenu.add_separator()

filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

# -------------------------------    filtro MENU      --------------------------------------------------------------------------

filter_menu = Menu(menubar, tearoff=0)

T_filtro = IntVar()
T_filtro.set(2)
T_filtro.get()

CamelCase = BooleanVar()

negativo = BooleanVar()
negativo.set(True)

filter_menu.add_radiobutton(label="Filtro Absoluto",variable=T_filtro, value=1)
filter_menu.add_radiobutton(label="Filtro Parcial",variable=T_filtro, value=2)

filter_menu.add_separator()

filter_menu.add_checkbutton(label="Solo CamelCase",variable=CamelCase,onvalue=True, offvalue=False,command= lambda: f._CamelCase(CamelCase))
filter_menu.add_checkbutton(label="Negativos exclullentes",variable=negativo,onvalue=True, offvalue=False,command= lambda: f._Negative(negativo))

menubar.add_cascade(label="Filtros", menu=filter_menu)

# -------------------------------    prsets MENU      --------------------------------------------------------------------------

perfiles = Menu(menubar,tearoff=0)
cargar = Menu(menubar,tearoff=0)
Eliminar = Menu(menubar,tearoff=0)

perfiles.add_cascade(label="Cargar",menu=cargar)

cargar.add_command(label=P.nombres[0], command= lambda: _list(P.ips[0]))
cargar.add_separator()
cargar.add_command(label=P.nombres[1], command= lambda: _list(P.ips[1]))
cargar.add_separator()
cargar.add_command(label=P.nombres[2], command= lambda: _list(P.ips[2]))
cargar.add_separator()
cargar.add_command(label=P.nombres[3], command= lambda: _list(P.ips[3]))
cargar.add_separator()
cargar.add_command(label=P.nombres[4], command= lambda: _list(P.ips[4]))

perfiles.add_command(label="Guardar", command= lambda: save(cargar,name_box.get(),message_box.get(),hour_1_box.get(),hour_2_box.get(),filtro_box.get()))

perfiles.add_cascade(label="Eliminar",menu=Eliminar)

Eliminar.add_command(label=P.nombres[0], command= lambda: eliminar(P.ips[0],P.nombres[0]))
Eliminar.add_separator()
Eliminar.add_command(label=P.nombres[1], command= lambda: eliminar(P.ips[1],P.nombres[1]))
Eliminar.add_separator()
Eliminar.add_command(label=P.nombres[2], command= lambda: eliminar(P.ips[2],P.nombres[2]))
Eliminar.add_separator()
Eliminar.add_command(label=P.nombres[3], command= lambda: eliminar(P.ips[3],P.nombres[3]))
Eliminar.add_separator()
Eliminar.add_command(label=P.nombres[4], command= lambda: eliminar(P.ips[4],P.nombres[4]))

menubar.add_cascade(label="Perfiles", menu=perfiles)

# -----------------------------------------------------------------------------------------------------------------------------------------

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

def save(cargar,name_box,message_box,hour_1_box,hour_2_box,filtro_box):
    save_window = Tk()
    save_window.geometry('250x100')
    save_window.resizable(0,0)
    save_window.configure(bg="#263D42")
    save_window.title('Auto presente')
    save_window.iconbitmap('icon.ico')

    S_frame = Frame(save_window, bg="#263D42")
    S_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    S_name_label = Label(S_frame, text = "Name",font = "helvetica 13")
    S_name_label.pack()
    S_name_box = Entry(S_frame, font = "helvetica 13", justify = "center")
    S_name_box.pack()

    save_buttom = Button(S_frame, text="Save",font="helvetica 13",command= lambda: quit_save(cargar,save_window,S_name_box.get(),name_box,message_box,hour_1_box,hour_2_box,filtro_box))
    save_buttom.pack()

    save_window.configure(menu=menubar)
    save_window.mainloop()

def quit_save(cargar,save_window,S_name_box,name_box,message_box,hour_1_box,hour_2_box,filtro_box):
    P.gurdar(S_name_box,name_box,message_box,hour_1_box,hour_2_box,filtro_box)
    window.update()
    save_window.destroy()

def eliminar(ip,nombre):

    resultado = messagebox.askokcancel(title='Auto messenger', message=f"are you sure to delete the {nombre} profile?")

    if resultado == True:
        P.eliminar(ip)



def _list(ip):
    _list = P._cargar(ip)

    name_box.delete(first=0,last=1000)
    message_box.delete(first=0,last=1000)
    hour_1_box.delete(first=0,last=1000)
    hour_2_box.delete(first=0,last=1000)
    filtro_box.delete(first=0,last=1000)


    name_box.insert(0,_list[1])
    message_box.insert(0,_list[2])
    hour_1_box.insert(0,_list[3])
    hour_2_box.insert(0,_list[4])
    filtro_box.insert(0,_list[5])
    

window.configure(menu=menubar)
window.mainloop()