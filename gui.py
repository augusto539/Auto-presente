import tkinter
from functions import send


window = tkinter.Tk()
#window.geometry('255x300')
#window.resizable(0,0)
window.configure(bg="#263D42")
window.title('Auto presente')
window.iconbitmap('icon.ico')

frame = tkinter.Frame(window, bg="#263D42")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

name_label = tkinter.Label(frame, text = "nombre del cotacto o grupo:",font = "helvetica 13")
name_label.pack()
name_box = tkinter.Entry(frame, font = "helvetica 13", justify = "center")
name_box.pack()

message_label = tkinter.Label(frame, text = "mensaje a enviar:",font = "helvetica 13")
message_label.pack()
message_box = tkinter.Entry(frame, font = "helvetica 13", justify ="center")
message_box.pack()

hour_1_label = tkinter.Label(frame, text = "hora de inicio:",font = "helvetica 13")
hour_1_label.pack()
hour_1_box = tkinter.Entry(frame,font = "helvetica 13", justify = "center")
hour_1_box.insert(3, ":")
hour_1_box.pack()

hour_2_label = tkinter.Label(frame, text = "hora final",font = "helvetica 13")
hour_2_label.pack()
hour_2_box = tkinter.Entry(frame,font = "helvetica 13", justify = "center")
hour_2_box.insert(3, ":")
hour_2_box.pack()

filtro_label = tkinter.Label(frame, text = "filtro",font = "helvetica 13")
filtro_label.pack()
filtro_box = tkinter.Entry(frame,font = "helvetica 13", justify = "center")
filtro_box.pack()

send_buttom = tkinter.Button(frame, text = "programar",font = "helvetica 13",command= lambda: send(name_box,message_box,hour_1_box,hour_2_box,filtro_box))
send_buttom.pack()

window.mainloop()