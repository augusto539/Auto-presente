import tkinter
from functions import main

def send():
    name = name_box.get()
    message = message_box.get()
    hour = hour_box.get()
    main(name,message,hour)

window = tkinter.Tk()
window.geometry('250x200')
window.resizable(0,0)
window.configure(bg="#263D42")
window.title('Auto presente')
window.iconbitmap('icon.ico')

frame = tkinter.Frame(window, bg="#263D42")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

name_label = tkinter.Label(frame, text = "nombre del cotacto o grupo:")
name_label.pack()
name_box = tkinter.Entry(frame, font = "helvetica 10", justify = "center")
name_box.pack()

message_label = tkinter.Label(frame, text = "mensaje a enviar:")
message_label.pack()
message_box = tkinter.Entry(frame, font = "helvetica 10", justify ="center")
message_box.pack()

hour_label = tkinter.Label(frame, text = "hora a enviar:")
hour_label.pack()
hour_box = tkinter.Entry(frame,font = "helvetica 10", justify = "center")
hour_box.pack()

send_buttom = tkinter.Button(frame, text = "programar",command=send)
send_buttom.pack()

window.mainloop()